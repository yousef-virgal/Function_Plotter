from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PySide2.QtGui import QIntValidator


class EditLine(QWidget):

    def __init__(self, id, inputChangeHandler, labelText="", minAcceptedValue=-10_000, maxAcceptedValue=10_000) :
        super(EditLine, self).__init__()

        self.inputChangeHandler = inputChangeHandler
        self.text = labelText
        self.id = id 

        self.layout = QHBoxLayout()
        self.label = QLabel()
        self.editText = QLineEdit()

        self.label.setText(labelText)
        self.editText.setValidator(QIntValidator(minAcceptedValue,maxAcceptedValue))
        self.editText.setText("0")
        self.editText.textChanged.connect(inputChangeHandler)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.editText)

        self.setLayout(self.layout)