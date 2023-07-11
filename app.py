import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QTextEdit,QPushButton,QDialog,QDateEdit, QTimeEdit)

from PyQt5.QtCore import QDateTime

from PyQt5.uic import loadUi

from generator_key_gui import Ui_Form

from key import KeyEngine

from custom_dialogs import CustomDialog

import logging

from time_conversor import TimeConversor

from smtp import Mail

class UIKeyGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        logging.basicConfig(filename='UIKeyGenerator.log', encoding='utf-8', level=logging.DEBUG)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cleanButton.clicked.connect(self.onclickClearFields)
        self.ui.generateKeyButton.clicked.connect(self.onClickGenerateKey)
        self.ui.sendKeyButton.clicked.connect(self.onCLickSendKeyMail)
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
       


    def onClickGenerateKey(self):
        id =        self.ui.textEditDeviceId.toPlainText()
        dateFrom  = self.ui.dateTimeEdit.dateTime().toPyDateTime()
        email =  self.ui.textEditMail.toPlainText()
        

        if id != "" and email !="" :
            keyEngineGenerator = KeyEngine(id , TimeConversor.getTimeStamp(dateFrom))
            key =  keyEngineGenerator.create()
            self.ui.plainTextKey.insertPlainText(key)
        else:
            self.errorDialogEmptyFields()


    def onclickClearFields(self):
        self.ui.textEditMail.setPlainText("")
        self.ui.textEditDeviceId.setPlainText("")
        self.ui.plainTextKey.setPlainText("")


    def onCLickSendKeyMail(self):
        mailer = self.ui.textEditMail.toPlainText()
        newKey = self.ui.plainTextKey.toPlainText()
        mail = Mail()
        mail.sendMail(mailer, newKey)
        
    
    def errorDialogEmptyFields(self):
        dlg = CustomDialog()
        dlg.exec()




app = QApplication(sys.argv)
ui = UIKeyGenerator()
ui.show()

app.exec()