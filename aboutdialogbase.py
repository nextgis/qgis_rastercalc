# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialogbase.ui'
#
# Created: Sat Jan 16 22:37:05 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AboutDialogBase(object):
    def setupUi(self, AboutDialogBase):
        AboutDialogBase.setObjectName("AboutDialogBase")
        AboutDialogBase.resize(294, 222)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AboutDialogBase)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lblVersion = QtGui.QLabel(AboutDialogBase)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.verticalLayout.addWidget(self.lblVersion)
        self.label_3 = QtGui.QLabel(AboutDialogBase)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(AboutDialogBase)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialogBase)

    def retranslateUi(self, AboutDialogBase):
        AboutDialogBase.setWindowTitle(QtGui.QApplication.translate("AboutDialogBase", "About RasterCalc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialogBase", "RasterCalc", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("AboutDialogBase", "Version x.x.x", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AboutDialogBase", "Performs raster algebra operations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AboutDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Developers:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Alexander Bruy</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        Maxim Dubinin</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Homepage:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        <a href=\"http://gis-lab.info/qa/rastercalc.html\"><span style=\" text-decoration: underline; color:#0000ee;\">http://gis-lab.info/qa/rastercalc.html</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        <a href=\"http://gis-lab.info/qa/rastercalc-eng.html\"><span style=\" text-decoration: underline; color:#0000ee;\">http://gis-lab.info/qa/rastercalc-eng.html</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

