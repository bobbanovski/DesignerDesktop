# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloader.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(151, 149)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.urledit = QtWidgets.QLineEdit(Dialog)
        self.urledit.setObjectName("urledit")
        self.verticalLayout.addWidget(self.urledit)
        self.savelocation = QtWidgets.QLineEdit(Dialog)
        self.savelocation.setObjectName("savelocation")
        self.verticalLayout.addWidget(self.savelocation)
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setObjectName("browse")
        self.verticalLayout.addWidget(self.browse)
        self.download = QtWidgets.QPushButton(Dialog)
        self.download.setObjectName("download")
        self.verticalLayout.addWidget(self.download)
        self.progress = QtWidgets.QProgressBar(Dialog)
        self.progress.setProperty("value", 0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.urledit.setPlaceholderText(_translate("Dialog", "URL"))
        self.savelocation.setPlaceholderText(_translate("Dialog", "save location"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.download.setText(_translate("Dialog", "Download"))

