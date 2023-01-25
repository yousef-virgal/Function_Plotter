from PySide2.QtWidgets import QWidget, QPushButton

class PlotButton(QPushButton):
    def __init__(self, buttonHandler, buttonText="") :
        super(PlotButton, self).__init__()

        self.buttonHandler = buttonHandler
        self.buttonText = buttonText

        self.setText(self.buttonText)
        self.clicked.connect(self.buttonHandler)


