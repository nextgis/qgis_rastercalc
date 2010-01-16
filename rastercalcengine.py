# -*- coding: utf-8 -*-

#******************************************************************************
#
# RasterCalc
# ---------------------------------------------------------
# Raster manipulation plugin.
# 
# Based on rewritten rasterlang plugin (C) 2008 by Barry Rowlingson
#
# Copyright (C) 2009 GIS-Lab (http://gis-lab.info) and
# Alexander Bruy (alexander.bruy@gmail.com)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing
# to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.
#
#******************************************************************************

from __future__ import division

import re
import numpy

from pyparsing import Word, alphas, ParseException, Literal, CaselessLiteral, \
     Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums, \
     Regex

import rastercalcutils as rasterUtils

exprStack = []
rasterList = set()

def rasterName():
  return Word( "[" + alphas, alphanums + "_-" + "]" )

def pushFirst( str, loc, toks ):
    global exprStack
    exprStack.append( toks[0] )

def getBand( data, n ):
  n = n - 1
  if len( data.shape ) == 3:
    return data[ int( n ) ]
  if len( data.shape ) == 2 and n == 1:
    return data
  if len( data.shape ) == 2:
    if n == 0:
      return data
    else:
      raise ValueError, "can't get band " + str( n ) + " from single-band raster"
  raise ValueError, "array must be with 2 or 3 dimensions"

def assignVar( str, loc, toks ):
    global rasterList
    rasterList.add( toks[ 0 ] )
    return toks[ 0 ]

def returnVar( layerName ):
  global rasterList
  return rasterUtils.getRaster( layerName )

# define grammar
point = Literal( '.' )
e = CaselessLiteral( 'E' )
plusorminus = Literal( '+' ) | Literal( '-' )
number = Word( nums ) 
integer = Combine( Optional( plusorminus ) + number )
floatnumber = Combine( integer +
                       Optional( point + Optional( number ) ) +
                       Optional( e + integer )
                     )

ident = Word( "[" + alphas, alphanums + "_-" + "]" )

plus  = Literal( "+" )
minus = Literal( "-" )
mult  = Literal( "*" )
div   = Literal( "/" )
lpar  = Literal( "(" ).suppress()
rpar  = Literal( ")" ).suppress()
addop  = plus | minus
multop = mult | div
expop = Literal( "^" )
assign = Literal( "=" )
band = Literal( "@" )

expr = Forward()
atom = ( ( e | floatnumber | integer | ident.setParseAction( assignVar ) ).setParseAction(pushFirst) | 
         ( lpar + expr.suppress() + rpar )
       )
        
factor = Forward()
factor << atom + ( ( band + factor ).setParseAction( pushFirst ) | ZeroOrMore( ( expop + factor ).setParseAction( pushFirst ) ) )
        
term = factor + ZeroOrMore( ( multop + factor ).setParseAction( pushFirst ) )
expr << term + ZeroOrMore( ( addop + term ).setParseAction( pushFirst ) )
bnf = expr

pattern =  bnf + StringEnd()

# map operator symbols to corresponding arithmetic operations
opn = { "+" : ( lambda a,b: numpy.add( a, b ) ),
        "-" : ( lambda a,b: numpy.subtract( a, b ) ),
        "*" : ( lambda a,b: numpy.multiply( a, b ) ),
        "/" : ( lambda a,b: numpy.divide( a, b ) ),
        "^" : ( lambda a,b: numpy.power( a, b) ) }

# Recursive function that evaluates the stack
def evaluateStack( s ):
  op = s.pop()
  if op in "+-*/^":
    op2 = evaluateStack( s )
    op1 = evaluateStack( s )
    return opn[op]( op1, op2 )
  elif op == "PI":
    return math.pi
  elif op == "E":
    return math.e
  elif re.search('^[\[a-zA-Z][a-zA-Z0-9_\-\]]*$',op):
    return returnVar( op )
  elif op == "@":
    num = evaluateStack( s )
    lay = evaluateStack( s )
    return getBand( lay, num )
  elif re.search('^[-+]?[0-9]+$',op):
    return long( op )
  else:
    return float( op )

