import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QVBoxLayout, QLabel
from PySide2.QtGui import QPalette, QColor

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

        
        self.label3 = QLabel()
        self.label3.setText("Hello from label 3")

        self.label4 = QLabel()
        self.label4.setText("Hello from label 4")

        self.verticalLayout.addWidget(self.label3)
        self.verticalLayout.addWidget(self.label4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.label1)
        self.horizontalLayout.addWidget(self.label2)

        

        self.screen.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.screen)

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()
