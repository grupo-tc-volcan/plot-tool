"""
Sample 0: Creates a QTApplication, builds the MainWindow and runs it.
"""

# python native modules

# third-party modules
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

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
from plot_tool.data.plotter import GraphPlotter
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.view.plotter_view import GraphPlotterFigureView


class SampleWidget(QWidget):
    """ Sample Widget
    Sample widget used to create a random signal as a GraphFunction
    when the PushButton is pressed and then tests the interaction between
    several models.
    """

    def __init__(self, parent=None, *args, **kwargs):
        super(SampleWidget, self).__init__(parent, *args, **kwargs)

        # Widget settings
        self.setWindowTitle("Sample Widget")

        # Model and view
        self.plotterData = GraphPlotter(GraphMagnitude.Time)
        self.plotterModel = GraphPlotterModel(self.plotterData)
        self.plotterView = GraphPlotterFigureView(self.plotterModel)

        # Components
        self.newButton = QPushButton("New")
        self.newButton.clicked.connect(self.onNewButton)

        self.drawButton = QPushButton("Draw")
        self.drawButton.clicked.connect(self.onDrawButton)

        self.figureCanvas = FigureCanvas(self.plotterView)
        self.plotterView.setParent(self.figureCanvas)

        # Layout managements
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.addWidget(self.newButton)
        self.verticalLayout.addWidget(self.drawButton)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.figureCanvas)
        self.setLayout(self.horizontalLayout)

        # Show()
        self.show()

    def onDrawButton(self, event=None):
        self.figureCanvas.draw()

    def onNewButton(self, event=None):
        times = list(arange(0, 10, 0.1))
        values = [5*sin(time * 2 * pi / 10) for time in times]

        self.plotterModel.addGraph(
            GraphFunction(
                "NewFunction",
                GraphValues(times, values),
                GraphMagnitude.Time,
                GraphMagnitude.Voltage
            )
        )


if __name__ == "__main__":
    app = QApplication([])
    window = SampleWidget()
    app.exec()
