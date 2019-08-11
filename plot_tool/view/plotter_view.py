# python native modules

# third-party modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QSizePolicy

# plot-tool modules


class GraphPlotterView(FigureCanvas):
    """ GraphPlotter View """

    def __init__(self,
                 parent=None, width=5, height=5):
        super(GraphPlotterView, self).__init__(Figure(figsize=(width, height)))
        self.setParent(parent)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Plotter View")
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.canvas = GraphPlotterView(self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
