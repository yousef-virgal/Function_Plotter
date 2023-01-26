from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit
from PySide2.QtGui import QIntValidator, QFont


class EditLine(QWidget):

    def __init__(self, id, inputChangeHandler, labelText="", editTextIntialValue="" ,minAcceptedValue=-10_000, maxAcceptedValue=10_000, allowOnlyNumbers=True) :
        super(EditLine, self).__init__()

        self.inputChangeHandler = inputChangeHandler
        self.text = labelText
        self.id = id 

        self.layout = QHBoxLayout()
        self.label = QLabel()
        self.editText = QLineEdit()

        self.label.setText(labelText)
        if allowOnlyNumbers:
            self.editText.setValidator(QIntValidator(minAcceptedValue,maxAcceptedValue))
        self.editText.setText(editTextIntialValue)
        self.editText.textChanged.connect(inputChangeHandler)

        self.editText.setStyleSheet("QLineEdit {  border: 2px solid gray;"
                                         "border-radius: 5px;}")
        self.label.setFont(QFont("Arial font",9))
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.editText)

        self.setLayout(self.layout)