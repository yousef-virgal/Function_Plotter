import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QMessageBox

from Edit_line_Component.editLineComponent import EditLine
from Button_Component.buttonComponent import PlotButton
from Graph_Component.graphComponent import GraphComponent
from Parser.parser import Parser
from Parser.Tokenizer.Tokenizer import Tokenizer
from Parser.nodeTypes import NodeTypes
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.min = 0
        self.max = 0 
        self.function = ""

        self.setWindowTitle("Function Ploter")
        self.screen = QWidget()
        self.popupScreen = QMessageBox()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout =  QVBoxLayout()

        self.graph = GraphComponent(self, width=5, height=4, dpi=100)
        
        self.minEditLine = EditLine(id="min", labelText="minimum value for x", editTextIntialValue="0", inputChangeHandler=self.minInputChangeHandler)
        self.maxEditLine = EditLine(id="max", labelText="maximum value for x", editTextIntialValue="0", inputChangeHandler=self.maxInputChangeHandler)
        self.functionEditText = EditLine(id="function", labelText="Enter Function",  inputChangeHandler=self.functionChangeHandler, allowOnlyNumbers=False)
        self.plotButton = PlotButton(buttonText="Plot", buttonHandler=self.plotButtonClickHandler)

        self.verticalLayout.addWidget(self.minEditLine)
        self.verticalLayout.addWidget(self.maxEditLine)
        self.verticalLayout.addWidget(self.functionEditText)
        self.verticalLayout.addWidget(self.plotButton)

        self.horizontalLayout.addLayout(self.verticalLayout,3)
        self.horizontalLayout.addWidget(self.graph,7)

        self.popupScreen.setWindowTitle("Error")
        self.popupScreen.setIcon(QMessageBox.Critical)

        self.screen.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.screen)
    
    def minInputChangeHandler(self, newText):
        self.min = self.getNumber(newText)
    
    def maxInputChangeHandler(self, newText):
        self.max = self.getNumber(newText)

    def functionChangeHandler(self,newText):
        self.function = newText
    
    def plotButtonClickHandler(self):
        if self.min > self.max:
            self.popupScreen.setText("Minimum value greater than Maximum value")
            self.popupScreen.exec_()
            return
        tokenizer = Tokenizer()
        tokenizer.setText(self.function)
        parser = Parser()
        parser.setTokens(tokenizer.tokenize())
        tree = parser.parse()

        self.graph.updateGraph(self.min,self.max,tree,self.computeFunction)

    def computeFunction(self,xArray,tree):
        if tree.type == NodeTypes.ADD:
            return self.computeFunction(xArray,tree.children[0]) + self.computeFunction(xArray,tree.children[1])
        elif tree.type == NodeTypes.MUL:
            return self.computeFunction(xArray,tree.children[0]) * self.computeFunction(xArray,tree.children[1])
        elif tree.type == NodeTypes.SUB:
            return self.computeFunction(xArray,tree.children[0]) - self.computeFunction(xArray,tree.children[1])
        elif tree.type == NodeTypes.DIV:
            return self.computeFunction(xArray,tree.children[0]) / self.computeFunction(xArray,tree.children[1])
        elif tree.type == NodeTypes.VARIABLE:
            return (xArray**tree.value.powerValue) * tree.value.multiplierValue
        
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
