# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialogbase.ui'
#
# Created: Sat Jan 16 16:08:41 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AboutDialogBase(object):
    def setupUi(self, AboutDialogBase):
        AboutDialogBase.setObjectName("AboutDialogBase")
        AboutDialogBase.resize(482, 300)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblLogo = QtGui.QLabel(AboutDialogBase)
        self.lblLogo.setObjectName("lblLogo")
        self.gridLayout.addWidget(self.lblLogo, 0, 0, 2, 1)
        self.label = QtGui.QLabel(AboutDialogBase)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lblVersion = QtGui.QLabel(AboutDialogBase)
        self.lblVersion.setObjectName("lblVersion")
        self.gridLayout.addWidget(self.lblVersion, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.textEdit = QtGui.QTextEdit(AboutDialogBase)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
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
        self.textEdit.setHtml(QtGui.QApplication.translate("AboutDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

