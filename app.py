import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QLabel

from Edit_line_Component.editLineComponent import EditLine
from Button_Component.buttonComponent import PlotButton
from Graph_Component.graphComponent import GraphComponent
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.min = 0
        self.max = 0 

        self.setWindowTitle("Function Ploter")
        self.screen = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout =  QVBoxLayout()

        self.graph = GraphComponent(self, width=5, height=4, dpi=100)
        
        self.minEditLine = EditLine(id="min", labelText="minimum value for x", editTextIntialValue="0", inputChangeHandler=self.minInputChangeHandler)
        self.maxEditLine = EditLine(id="max", labelText="maximum value for x", editTextIntialValue="0", inputChangeHandler=self.maxInputChangeHandler)
        self.functionEditText = EditLine(id="function", labelText="Enter Function",  inputChangeHandler=self.maxInputChangeHandler, allowOnlyNumbers=False)
        self.plotButton = PlotButton(buttonText="Plot", buttonHandler=self.plotButtonClickHandler)

        self.verticalLayout.addWidget(self.minEditLine)
        self.verticalLayout.addWidget(self.maxEditLine)
        self.verticalLayout.addWidget(self.functionEditText)
        self.verticalLayout.addWidget(self.plotButton)

        self.horizontalLayout.addLayout(self.verticalLayout,3)
        self.horizontalLayout.addWidget(self.graph,7)

        self.screen.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.screen)
    
    def minInputChangeHandler(self, newText):
        self.min = self.getNumber(newText)
    
    def maxInputChangeHandler(self, newText):
        self.max = self.getNumber(newText)
    
    def plotButtonClickHandler(self):
        print("clicked")
        self.graph.updateGraph(self.min,self.max,None)

    def getNumber(self, text):
        if text == "-" or text == "":
            return 0
        else:
            return int(text)

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()
