import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QLabel

from Edit_line_Component.editLineComponent import EditLine
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function Ploter")
        self.screen = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout =  QVBoxLayout()

        self.label1 = QLabel()
        self.label1.setText("Hello from label 1")
        
        self.label2 = QLabel()
        self.label2.setText("Hello from label 2")

        
        self.minEditLine = EditLine(id="min", labelText="minimum value for x", inputChangeHandler=self.inputChangeHandler)

        self.maxEditLine = EditLine(id="max", labelText="maximum value for x", inputChangeHandler=self.inputChangeHandler)

        self.verticalLayout.addWidget(self.minEditLine)
        self.verticalLayout.addWidget(self.maxEditLine)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.label1)
        self.horizontalLayout.addWidget(self.label2)

        

        self.screen.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.screen)
    
    def inputChangeHandler(self, newText):
        print(newText)

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()
