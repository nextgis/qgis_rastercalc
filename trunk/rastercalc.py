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

import resources

class RasterCalcPlugin( object ):
  def __init__( self, iface ):
    self.iface = iface
    self.iface = iface
    try:
      self.QgisVersion = unicode( QGis.QGIS_VERSION_INT )
    except:
      self.QgisVersion = unicode( QGis.qgisVersion )[ 0 ]

    # For i18n support
    userPluginPath = QFileInfo( QgsApplication.qgisUserDbFilePath() ).path() + "/python/plugins/rastercalc"
    systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/rastercalc"

    overrideLocale = QSettings().value( "locale/overrideFlag", QVariant( False ) ).toBool()
    if not overrideLocale:
      localeFullName = QLocale.system().name()
    else:
      localeFullName = QSettings().value( "locale/userLocale", QVariant( "" ) ).toString()

    if QFileInfo( userPluginPath ).exists():
      translationPath = userPluginPath + "/i18n/rastercalc_" + localeFullName + ".qm"
    else:
      translationPath = systemPluginPath + "/i18n/rastercalc_" + localeFullName + ".qm"

    self.localePath = translationPath
    self.translator = QTranslator()
    self.translator.load( self.localePath )
    QCoreApplication.installTranslator( self.translator )
      

  def initGui( self ):
    if int( self.QgisVersion ) < 1:
      QMessageBox.warning( self.iface.mainWindow(), "RasterCalc",
                           QCoreApplication.translate( "RasterCalc", "Quantum GIS version detected: " ) + unicode( self.QgisVersion ) + ".xx\n" +
                           QCoreApplication.translate( "RasterCalc", "This version of RasterCalc requires at least QGIS version 1.0.0\nPlugin will not be enabled." ) )
      return None

    self.action = QAction( QIcon( ":/rastercalc.png" ), "RasterCalc", self.iface.mainWindow() )
    QObject.connect( self.action, SIGNAL( "activated()" ), self.run )
    self.iface.addToolBarIcon( self.action )
    self.iface.addPluginToMenu( "RasterCalc", self.action )

  def unload( self ):
    self.iface.removePluginMenu( "RasterCalc", self.action )
    self.iface.removeToolBarIcon( self.action )

  def run( self ):
    # check is all necessary modules are available
    try:
      import pyparsing
    except ImportError, e:
      QMessageBox.information( self.iface.mainWindow(), QCoreApplication.translate( "RasterCalc", "Plugin error" ), QCoreApplication.translate( "RasterCalc", "Couldn't import Python module 'pyparsing'. Without it you won't be able to run RasterCalc." ) )
      return

    try:
      import osgeo.gdal
    except ImportError, e:
      QMessageBox.information( self.iface.mainWindow(), QCoreApplication.translate( "RasterCalc", "Plugin error" ), QCoreApplication.translate( "RasterCalc", "Couldn't import Python module 'osgeo.gdal'. Without it you won't be able to run PasterCalc." ) )
      return

    try:
      import numpy
    except ImportError, e:
      QMessageBox.informtion( self.iface.mainWindow(), QCoreApplication.translate( "RasterCalc", "Plugin error" ), QCoreApplication.translate( "RasterCalc", "Couldn't import Python module 'numpy'. Without it you won't be able to run RasterCalc." ) )
      return

    import rastercalcdialog
      
    dlg = rastercalcdialog.RasterCalcDialog()
    dlg.exec_()

