# python native modules

# third-party modules
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.designer.window.window_ui import Ui_MainWindow

from plot_tool.view.signal_dialog import SignalDialog

from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from plot_tool.data.plotter import GraphPlotter
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.view.plotter_figure_view import GraphPlotterFigureView


class Window(QMainWindow, Ui_MainWindow):
    """ Application Window """

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Data reference
        self.plotterData = GraphPlotter(GraphMagnitude.Time)
        self.plotterModel = GraphPlotterModel(self.plotterData)
        self.plotterView = GraphPlotterFigureView(self.plotterModel)

        self.figureCanvas = FigureCanvas(self.plotterView)
        self.plotterView.setFigureCanvas(self.figureCanvas)

        self.gridLayout.addWidget(self.figureCanvas)

        self.visorView.setModel(self.plotterModel)

        # Slot and signal connections
        self.actionSignals.triggered.connect(self.onSignalsAction)

        # Show()
        self.show()

    def onSignalsAction(self):
        signalDialog = SignalDialog()
        if signalDialog.exec():
            graphFunctions = signalDialog.getGraphFunction()
            for graphFunction in graphFunctions:
                self.plotterModel.addGraph(graphFunction)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec()
