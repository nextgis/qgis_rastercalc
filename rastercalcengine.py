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

from pyparsing import Word, alphas, ParseException, Literal, CaselessKeyword, \
     Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums, \
     Regex

import rastercalcutils as rasterUtils

exprStack = []
rasterNames = set()

def rasterName():
  return Combine( "[" + Word( alphas + nums, alphanums + "._-" ) + "]" )

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
    global rasterNames
    rasterNames.add( toks[ 0 ] )
    return toks[ 0 ]

def returnRaster( layerName ):
  return rasterUtils.getRaster( layerName )

def returnBand( layerName, bandNum, row, size, count ):
  return rasterUtils.getRasterBand( layerName, bandNum, row, size, count )

# conditional operators
def equal( raster, compare, replace ):
  tmp = numpy.equal( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

def greater( raster, compare, replace ):
  tmp = numpy.greater( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

def less( raster, compare, replace ):
  tmp = numpy.less( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

def not_equal( raster, compare, replace ):
  tmp = numpy.not_equal( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

def greater_equal( raster, compare, replace ):
  tmp = numpy.greater_equal( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

def less_equal( raster, compare, replace ):
  tmp = numpy.less_equal( raster, compare )
  numpy.putmask( raster, tmp, replace )
  return raster

# define grammar
point = Literal( '.' )
colon = Literal( ',' )

e = CaselessKeyword( 'E' )
plusorminus = Literal( '+' ) | Literal( '-' )
number = Word( nums )
integer = Combine( Optional( plusorminus ) + number )
floatnumber = Combine( integer +
                       Optional( point + Optional( number ) ) +
                       Optional( e + integer )
                     )

ident = Combine( "[" + Word( alphas + nums, alphanums + "._-" ) + "]" )
fn = Word( alphas )

plus  = Literal( "+" )
minus = Literal( "-" )
mult  = Literal( "*" )
div   = Literal( "/" )
lpar  = Literal( "(" ).suppress()
rpar  = Literal( ")" ).suppress()

greater_op       = Combine(Literal(">") + ~Literal("="))
greater_equal_op = Combine(Literal(">") + Literal("="))
less_op          = Combine(Literal("<") + ~Literal("="))
less_equal_op    = Combine(Literal("<") + Literal("="))

addop  = plus | minus
multop = mult | div
compop = less_op | greater_op | less_equal_op | greater_equal_op
expop = Literal( "^" )
assign = Literal( "=" )
band = Literal( "@" )

expr = Forward()
atom = ( ( e | floatnumber | integer | ident.setParseAction( assignVar ) | fn + lpar + expr + rpar | fn + lpar + expr + colon + expr + colon + expr + rpar ).setParseAction(pushFirst) |
         ( lpar + expr.suppress() + rpar )
       )

factor = Forward()
factor << atom + ( ( band + factor ).setParseAction( pushFirst ) | ZeroOrMore( ( expop + factor ).setParseAction( pushFirst ) ) )

term = factor + ZeroOrMore( ( multop + factor ).setParseAction( pushFirst ) )
addterm = term + ZeroOrMore( ( addop + term ).setParseAction( pushFirst ) )
expr << addterm + ZeroOrMore( ( compop + addterm ).setParseAction( pushFirst ) )
bnf = expr

pattern =  bnf + StringEnd()

# map operator symbols to corresponding arithmetic operations
opn = { "+" : ( lambda a,b: numpy.add( a, b ) ),
        "-" : ( lambda a,b: numpy.subtract( a, b ) ),
        "*" : ( lambda a,b: numpy.multiply( a, b ) ),
        "/" : ( lambda a,b: numpy.divide( a, b ) ),
        "^" : ( lambda a,b: numpy.power( a, b) ),
        "<" : ( lambda a,b: numpy.less( a, b) ),
        ">" : ( lambda a,b: numpy.greater( a, b) ),
        "<=" : ( lambda a,b: numpy.less_equal( a, b) ),
        ">=" : ( lambda a,b: numpy.greater_equal( a, b) ) }

func = { "sin": numpy.sin,
         "asin": numpy.arcsin,
         "cos": numpy.cos,
         "acos": numpy.arccos,
         "tan": numpy.tan,
         "atan": numpy.arctan,
         "exp": numpy.exp,
         "log": numpy.log,
         "eq": equal,
         "ne": not_equal,
         "lt": less,
         "gt": greater,
         "le": less_equal,
         "ge": greater_equal }

# Recursive function that evaluates the stack
def evaluateStack( s, row, size, count ):
  op = s.pop()
  if op in "+-*/^<>" or op in ['>=','<=']:
    op2 = evaluateStack( s, row, size, count )
    op1 = evaluateStack( s, row, size, count )
    return opn[op]( op1, op2 )
  elif op == "PI":
    return math.pi
  elif op == "E":
    return math.e
  elif op in func:
    if op in [ "eq", "ne", "gt", "lt", "ge", "le" ]:
      replace = evaluateStack( s, row, size, count )
      compare = evaluateStack( s, row, size, count )
      inRaster = evaluateStack( s, row, size, count )
      return func[ op ]( inRaster, compare, replace )
    # function with one argument
    op1 = evaluateStack( s, row, size, count )
    return func[ op ]( op1 )
  elif re.search('^[\[a-zA-Z][a-zA-Z0-9_\-\]]*$',op):
    return op
  elif op == "@":
    num = evaluateStack( s, row, size, count )
    lay = evaluateStack( s, row, size, count )
    return returnBand( lay, num, row, size, count )
  elif re.search('^[-+]?[0-9]+$',op):
    return long( op )
  else:
    return float( op )
