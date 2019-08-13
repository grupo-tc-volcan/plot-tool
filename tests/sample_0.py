"""
Sample 0: Creates a QTApplication, builds the MainWindow and runs it.
"""

# python native modules

# third-party modules
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from numpy import arange
from numpy import sin
from numpy import pi

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues

from plot_tool.model.function_model import GraphFunctionModel
from plot_tool.view.function_line import GraphFunctionLineView


class SampleWidget(QWidget):
    """ Sample Widget
    Sample widget used to create a random signal as a GraphFunction
    when the PushButton is pressed and then tests the interaction between
    several models.
    """

    def __init__(self, parent=None, *args, **kwargs):
        super(SampleWidget, self).__init__(parent, *args, **kwargs)

        self.graph = None
        self.graph_model = None
        self.graph_view = None

        # Window settings
        self.setWindowTitle("Sample Widget")

        # Components
        self.sampleButton = QPushButton("Sample Button")
        self.sampleButton.clicked.connect(self.onSampleButtonClick)

        self.visibleButton = QPushButton("Visible Toggle")
        self.visibleButton.clicked.connect(self.toggleVisibility)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.axes = Axes(self.figure, [0.1, 0.1, 0.8, 0.8])

        self.figure.add_axes(self.axes)

        # Layout management
        self.boxLayout = QHBoxLayout()
        self.buttonBoxLayout = QVBoxLayout()

        self.buttonBoxLayout.addWidget(self.sampleButton)
        self.buttonBoxLayout.addWidget(self.visibleButton)

        self.boxLayout.addLayout(self.buttonBoxLayout)
        self.boxLayout.addWidget(self.canvas)

        self.setLayout(self.boxLayout)

        # Run the widget
        self.show()

    def toggleVisibility(self, event):
        if self.graph_model is not None:
            self.graph_model.isVisible = False if self.graph_model.isVisible else True

    def updateCanvas(self):
        self.canvas.draw()

    def onSampleButtonClick(self, event):

        time_interval = arange(0, 2 * pi, 2 * pi / 100)
        value_interval = [sin(t) for t in time_interval]

        self.graph = GraphFunction(
            "Sample Function",
            GraphValues(list(time_interval), value_interval),
            GraphMagnitude.Time,
            GraphMagnitude.Voltage
        )

        self.graph_model = GraphFunctionModel(self.graph)
        self.graph_view = GraphFunctionLineView(self.graph_model)

        self.graph_model.hasChanged.connect(self.updateCanvas)
        self.axes.add_line(self.graph_view)
        self.updateCanvas()


if __name__ == "__main__":
    app = QApplication([])
    window = SampleWidget()
    app.exec()
