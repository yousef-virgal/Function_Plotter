import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QMessageBox
from PySide2.QtGui  import QPalette, QColor, QIcon

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
        self.setWindowIcon(QIcon("./assets/appIcon.png"))
        
        self.screen = QWidget()
        self.popupScreen = QMessageBox()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout =  QVBoxLayout()
        
        self.graph = GraphComponent(self, width=5, height=4, dpi=100)
        
        self.minEditLine = EditLine(id="min", labelText="Minimum value for x:", editTextIntialValue="0", inputChangeHandler=self.minInputChangeHandler)
        self.maxEditLine = EditLine(id="max", labelText="Maximum value for x:", editTextIntialValue="0", inputChangeHandler=self.maxInputChangeHandler)
        self.functionEditText = EditLine(id="function", labelText="Enter Function",  inputChangeHandler=self.functionChangeHandler, allowOnlyNumbers=False)
        self.plotButton = PlotButton(buttonText="Plot", buttonHandler=self.plotButtonClickHandler)
        self.clearButton = PlotButton(buttonText="Clear", buttonHandler=self.clearButtonClickHandler)

        self.verticalLayout.addWidget(self.minEditLine)
        self.verticalLayout.addWidget(self.maxEditLine)
        self.verticalLayout.addWidget(self.functionEditText)
        self.verticalLayout.addWidget(self.plotButton)
        self.verticalLayout.addWidget(self.clearButton)

        self.horizontalLayout.addLayout(self.verticalLayout,3)
        self.horizontalLayout.addWidget(self.graph,7)

        self.popupScreen.setWindowTitle("Error")
        self.popupScreen.setIcon(QMessageBox.Critical)

        self.screen.setLayout(self.horizontalLayout)
        palette = self.screen.palette()
        palette.setColor(QPalette.Window, QColor(237, 233, 232))
        self.screen.setPalette(palette)
        self.screen.setAutoFillBackground(True)
        self.setCentralWidget(self.screen)
    
    def minInputChangeHandler(self, newText):
        """
        A function that handels the change of the minmium edit line
        
        Arguments:
            newText: the new value of the editline
        Returns:
            None
        """
        self.min = self.getNumber(newText)
    
    def maxInputChangeHandler(self, newText):
        """
        A function that handels the change of the maxmium edit line
        
        Arguments:
            newText: the new value of the editline
        Returns:
            None
        """
        self.max = self.getNumber(newText)

    def functionChangeHandler(self,newText):
        """
        A function that handels the change of the function edit line
        
        Arguments:
            newText: the new value of the editline 
        Returns:
            None
        """
        self.function = newText
    
    def plotButtonClickHandler(self):
        """
        A function that handels the click on the plot button

        Arguments:
            None
        Returns:
            None
        """
        if self.min > self.max:
            self.popupScreen.setText("Minimum value greater than Maximum value")
            self.popupScreen.exec_()
            return
        try :
            tokenizer = Tokenizer()
            tokenizer.setText(self.function.strip())
            parser = Parser()
            parser.setTokens(tokenizer.tokenize())
            tree = parser.parse()
            self.graph.updateGraph(self.min,self.max,tree,self.computeFunction)
        except Exception as e:
            self.popupScreen.setText(f"{e}")
            self.popupScreen.exec_()

    def computeFunction(self,xArray,tree):
        """
        A function that traverses a tree to compute a function applied on xArray

        Arguments:
            xArray: a numpy array that represent the list of x values that we want to apply the function on
            tree: the head of a tree structure that repsesnts the function 
        Returns:
            a numpy array  of the function applied on the xArray
        """
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
        
    def getNumber(self, text:str):
        """
        This function retuns the integer representation of the text that is taken as input
         Arguments:
            text: a string representation of a number
        Returns:
            The integer representation of the string argument 
        """
        if text == "-" or text == "":
            return 0
        else:
            return int(text)
    def clearButtonClickHandler(self):
        self.graph.clearGraph()
app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()
