# python native modules

# third-party modules
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.designer.window.window_ui import Ui_MainWindow

from plot_tool.view.signal_dialog import SignalDialog
from plot_tool.view.transfer_dialog import TransferDialog
from plot_tool.view.plotter_dialog import PlotterDialog

from plot_tool.data.magnitudes import get_magnitude_from_string

from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from plot_tool.data.plotter import GraphPlotter
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.view.plotter_figure_view import GraphPlotterFigureView

from plot_tool.user.session import Session


class Window(QMainWindow, Ui_MainWindow):
    """ Application Window """

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Data reference
        self.session = Session()

        # Components
        self.views = []
        self.canvas = []

        # Slot and signal connections
        self.actionSignals.triggered.connect(self.onSignalsAction)
        self.actionTransfer_Function.triggered.connect(self.onTransferAction)
        self.actionfrom_Excel_2.triggered.connect(self.onFromExcelAction)
        self.actionfrom_LTSpice_IV_2.triggered.connect(self.onFromLTSpiceAction)

        self.addButton.clicked.connect(self.onAdd)
        self.deleteButton.clicked.connect(self.onDelete)
        self.plotterList.currentItemChanged.connect(self.onSelection)

        # Show()
        self.show()

    def verifySelection(self) -> bool:
        selectedIndex = self.plotterList.currentIndex().row()
        if selectedIndex < 0:
            QMessageBox.warning(self,
                                "Error message",
                                "No GraphPlotter selected! You must create or select one first.")
            return False
        else:
            return True

    def updatePlotterList(self):
        self.plotterList.clear()
        self.plotterList.addItems([plotter_model.name for plotter_model in self.session.plotter_models])

    def onSelection(self):
        selectedIndex = self.plotterList.currentIndex().row()
        if selectedIndex >= 0:
            self.visorView.setModel(self.session.plotter_models[selectedIndex])
            self.canvasList.setCurrentWidget(self.canvas[selectedIndex])

    def onAdd(self):
        dialog = PlotterDialog()
        if dialog.exec():

            if dialog.name.text() in [plotter_model.name for plotter_model in self.session.plotter_models]:
                QMessageBox.warning(self, "Error message",
                                    "Error detected adding a new graph. Name already used!")
            else:
                plotterData = GraphPlotter(get_magnitude_from_string(dialog.xMagnitude.currentText()))
                plotterModel = GraphPlotterModel(plotterData, name=dialog.name.text())
                plotterView = GraphPlotterFigureView(plotterModel)
                figureCanvas = FigureCanvas(plotterView)

                plotterView.setFigureCanvas(figureCanvas)
                self.session.addPlotterModel(plotterModel)
                self.canvas.append(figureCanvas)
                self.views.append(plotterView)
                self.canvasList.setCurrentIndex(self.canvasList.addWidget(figureCanvas))

                self.updatePlotterList()

    def onDelete(self):
        if len(self.session.plotter_models):
            if QMessageBox.question(self, "Deleting graph", "Are you sure you want to delete?",
                                    QMessageBox.Ok | QMessageBox.Cancel):
                selectedIndex = self.plotterList.currentIndex().row()

                # Look for the objects
                plotter_model = self.session.plotter_models[selectedIndex]
                plotter_view = self.views[selectedIndex]
                canvas = self.canvas[selectedIndex]

                # Remove them from the GUI
                self.canvasList.removeWidget(canvas)

                # Remove them from the data references
                self.canvas.remove(canvas)
                self.views.remove(plotter_view)
                self.session.plotter_models.remove(plotter_model)

                # Update plotter list and resets selection
                self.updatePlotterList()

    def onFromExcelAction(self):
        if not self.verifySelection():
            return

        # Code here please!

    def onFromLTSpiceAction(self):
        if not self.verifySelection():
            return

        # Code here please!

    def onTransferAction(self):
        if not self.verifySelection():
            return

        transferDialog = TransferDialog()
        if transferDialog.exec():
            graphFunctions = transferDialog.getGraphFunction()
            for graphFunction in graphFunctions:
                if not self.session.plotter_models[self.plotterList.currentIndex().row()].addGraph(graphFunction):
                    QMessageBox.warning(self,
                                        "Error message",
                                        "Cannot add new graph. Name already used or invalid x magnitude")

    def onSignalsAction(self):
        if not self.verifySelection():
            return

        signalDialog = SignalDialog()
        if signalDialog.exec():
            graphFunctions = signalDialog.getGraphFunction()
            for graphFunction in graphFunctions:
                if not self.session.plotter_models[self.plotterList.currentIndex().row()].addGraph(graphFunction):
                    QMessageBox.warning(self,
                                        "Error message",
                                        "Cannot add new graph. Name already used or invalid x magnitude")


def main():
    app = QApplication([])
    window = Window()
    app.exec()


if __name__ == "__main__":
    main()
