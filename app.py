import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QLabel

from Edit_line_Component.editLineComponent import EditLine
from Button_Component.buttonComponent import PlotButton
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function Ploter")
        self.screen = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout =  QVBoxLayout()

        self.label1 = QLabel()
        self.label1.setText("Hello from label 1")
        
        self.minEditLine = EditLine(id="min", labelText="minimum value for x", editTextIntialValue="0", inputChangeHandler=self.inputChangeHandler)
        self.maxEditLine = EditLine(id="max", labelText="maximum value for x", editTextIntialValue="0", inputChangeHandler=self.inputChangeHandler)
        self.functionEditText = EditLine(id="function", labelText="Enter Function",  inputChangeHandler=self.inputChangeHandler, allowOnlyNumbers=False)
        self.plotButton = PlotButton(buttonText="Plot", buttonHandler=self.plotButtonClickHandler)

        self.verticalLayout.addWidget(self.minEditLine)
        self.verticalLayout.addWidget(self.maxEditLine)
        self.verticalLayout.addWidget(self.functionEditText)
        self.verticalLayout.addWidget(self.plotButton)

        self.horizontalLayout.addLayout(self.verticalLayout,3)
        self.horizontalLayout.addWidget(self.label1,7)

        self.screen.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.screen)
    
    def inputChangeHandler(self, newText):
        print(newText)
    
    def plotButtonClickHandler(self):
        print("Button Clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()
