import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class GraphComponent(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(GraphComponent, self).__init__(self.fig)
    
    def updateGraph(self, xMin, xMax, tree,function):
        xAxis = np.linspace(xMin,xMax,1_000)
        yAxis = function(xAxis,tree)

        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.plot(xAxis, yAxis)
        self.fig.canvas.draw()