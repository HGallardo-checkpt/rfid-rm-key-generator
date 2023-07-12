from PyQt5 import QtCore

from PyQt5.QtWidgets import QDialog , QLabel, QVBoxLayout,QDialogButtonBox

class CustomDialog(QDialog):
    def __init__(self,message):
        super().__init__()

        self.setWindowTitle("Error!")

        QBtn = QDialogButtonBox.Ok

        self.resize(225, 112)
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()

        message = QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
 