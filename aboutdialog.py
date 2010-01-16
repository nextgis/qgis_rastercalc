# -*- coding: utf-8 -*-

#******************************************************************************
#
# RasterCalc
# ---------------------------------------------------------
# Raster manipulation plugin.
# 
# Based on rewritten rasterlang plugin (C) 2008 by Barry Rowlingson
# and modified example SimpleCalc from pyparsing module
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

import webbrowser

from aboutdialogbase import Ui_AboutDialogBase

import resources

class AboutDialog( QDialog, Ui_AboutDialogBase ):
  def __init__( self ):
    QDialog.__init__( self )
    self.setupUi( self )

    self.lblLogo.setPixmap( QPixmap( ":/rastercalc.png" ) )
    self.lblVersion.setText( "Version 0.1.5" )

    self.btnHelp = self.buttonBox.button( QDialogButtonBox.Help )
    QObject.connect( self.btnHelp, SIGNAL( "clicked()" ), self.openWebHelp )

    self.textEdit.setText( self.getAboutInfo() )

  def openWebHelp( self ):
    overrideLocale = QSettings().value( "locale/overrideFlag", QVariant( False ) ).toBool()
    if not overrideLocale:
      localeFullName = QLocale.system().name()
    else:
      localeFullName = QSettings().value( "locale/userLocale", QVariant( "" ) ).toString()
    localeShortName = localeFullName[ 0:2 ]
    if localeShortName in [ "ru", "uk" ]:
      webbrowser.open( "http://gis-lab.info/qa/rastercalc.html" )
    else:
      webbrowser.open( "http://gis-lab.info/qa/rastercalc-eng.html" )

  def getAboutInfo( self ):
    return self.tr( """
    The goal of RasterCalc is to provide easy to use and powerfull tool for raster algebra. Only layers with same grid size and extent are supported.

    If you would like to report a bug, make suggestion or have a question about the plugin, feel free to contact with authors:
          http://gis-lab.info/contacts
          or alexander.bruy@gmail.com

    LICENSING INFORMATION
    RasterCalc is copyright (C) 2010 Maxim Dubinin and Alexander Bruy
    Some code adapted from RasterLang (C) 2008 Barry Rowlingson

    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
    
    This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    A copy of the GNU General Public License is available on the World Wide Web at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
    """ )
