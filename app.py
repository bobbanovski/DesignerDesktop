from PyQt5.QtWidgets import *

import sys
import pydownloader

class MainProgram(QDialog, pydownloader.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.progress.setValue(50)
        self.urledit.setText("http://www.google.com")

app = QApplication(sys.argv)
mainprogram = MainProgram()
mainprogram.show()
app.exec_()
