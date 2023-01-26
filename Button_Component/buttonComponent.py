from PySide2.QtWidgets import QWidget, QPushButton
from PySide2.QtGui import QCursor
from PySide2.QtCore import Qt

class PlotButton(QPushButton):
    def __init__(self, buttonHandler, buttonText="") :
        super(PlotButton, self).__init__()

        self.buttonHandler = buttonHandler
        self.buttonText = buttonText

        self.setText(self.buttonText)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("QPushButton{  border: 2px solid gray;"
                                         "border-radius: 5px; background-color:#6699CC; font-size:22px;}")
        self.clicked.connect(self.buttonHandler)


