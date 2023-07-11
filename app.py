import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QTextEdit,QPushButton)

from PyQt5.uic import loadUi

from generator_key_gui import Ui_Form

from key import KeyEngine

class UIKeyGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.textEditKeyDuration.setPlainText("1682000990") 
        self.ui.cleanButton.clicked.connect(self.onclickClearFields)
        self.ui.generateKeyButton.clicked.connect(self.onClickGenerateKey)
       


    def onClickGenerateKey(self):
        id =        self.ui.textEditDeviceId.toPlainText()
        duration =  self.ui.textEditKeyDuration.toPlainText()
        keyEngineGenerator = KeyEngine(id , duration)
        key =  keyEngineGenerator.create()
        self.ui.plainTextKey.insertPlainText(key)


    def onclickClearFields(self):
        self.ui.textEditDeviceId.setPlainText("")
        self.ui.textEditKeyDuration.setPlainText("")
        self.ui.plainTextKey.setPlainText("")


    def onCLickSendKeyMail(self):
        self.plainTextKey.toPlainText()


app = QApplication(sys.argv)
ui = UIKeyGenerator()
ui.show()

app.exec()