# python native modules
import pickle

# third-party modules
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QListWidgetItem


# plot-tool modules
from plot_tool.designer.window.window_ui import Ui_MainWindow

from plot_tool.view.signal_dialog import SignalDialog
from plot_tool.view.transfer_dialog import TransferDialog
from plot_tool.view.plotter_dialog import PlotterDialog
from plot_tool.view.about_dialog import AboutDialog

from plot_tool.data.magnitudes import get_magnitude_from_string

from plot_tool.data.plotter import GraphPlotter
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.view.plotter_figure_view import GraphPlotterFigureView
from plot_tool.view.function_visor_view import GraphFunctionVisorView

from plot_tool.user.session import Session

from plot_tool.view.spreadsheet_dialog import spreadsheet_sv
from plot_tool.view.ltspice_dialog import LTSpiceDialog


# noinspection PyPep8Naming
class Window(QMainWindow, Ui_MainWindow):
    """ Application Window """

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("PlotTool 1.0")
        self.showMaximized()

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
        self.actionas_Image.triggered.connect(self.onImageExportAction)
        self.actionAbout.triggered.connect(self.onAboutAction)

        self.actionSave_2.triggered.connect(self.onSaveAction)
        self.actionOpen_2.triggered.connect(self.onOpenAction)

        self.addButton.clicked.connect(self.onAdd)
        self.deleteButton.clicked.connect(self.onDelete)
        self.plotterList.currentItemChanged.connect(self.onPlotterSelection)
        self.functionList.itemSelectionChanged.connect(self.onFunctionSelection)

        # Show()
        self.show()

    def onSaveAction(self):
        # Verifying there is a plotter selected
        selectedIndex = self.plotterList.currentIndex().row()
        if selectedIndex >= 0:
            # Requesting the saving file path
            file_path = QFileDialog.getSaveFileName()
            file_path = file_path[0]
            file = open(file_path, "wb")

            # Data saving
            plotter_data = self.session.plotter_models[selectedIndex].plotter
            pickle.dump(plotter_data, file)
        else:
            QMessageBox.warning(self,
                                "Error message",
                                "No GraphPlotter found! Create or select one first.")

    def onOpenAction(self):
        # Requesting the opening file path
        try:
            file_path = QFileDialog.getOpenFileName()
            file_path = file_path[0]
            file = open(file_path, "rb")

            # Loading data
            plotter_data = pickle.load(file)
        except:
            QMessageBox.warning(
                self,
                "Error message",
                "File error detected when loading data. Corrupt or wrong file."
            )
            return

        # Loading data to the GUI Application
        self.addPlotter(plotter_data)
        plotterModel = self.session.getPlotterModel(plotter_data)
        plotterModel.addGraphModels()
        plotterModel.addAxesModels()
        plotterModel.adjustSizeOfXAxis()
        plotterModel.adjustSizeOfYAxis()

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
        # Saving the current index...
        selectedIndex = self.plotterList.currentIndex()

        # Clear and adds all new items
        self.plotterList.clear()
        self.plotterList.addItems([plotter_model.name for plotter_model in self.session.plotter_models])

        # Restore the index
        self.plotterList.setCurrentIndex(selectedIndex)

    def updateFunctionList(self):
        # Checking if there is any GraphPlotter selected
        selectedIndex = self.plotterList.currentIndex().row()

        if selectedIndex >= 0:
            self.functionList.clear()

            # Getting all the GraphFunction models from the Plotter selected
            items = [GraphFunctionVisorView(None, graphModel)
                     for graphModel in self.session.plotter_models[selectedIndex].graphModels]

            # Creating the ListWidgetItems and adding them to the list
            for item in items:
                widgetItemWrapper = QListWidgetItem(self.functionList)
                widgetItemWrapper.setSizeHint(item.sizeHint())
                self.functionList.addItem(widgetItemWrapper)
                self.functionList.setItemWidget(widgetItemWrapper, item)

    def onFunctionSelection(self):
        # Verifying if there is any Function selected
        selectedItems = self.functionList.selectedItems()
        selectedItems = [self.functionList.itemWidget(selectedItem) for selectedItem in selectedItems]
        selectedModels = [selectedItem.model for selectedItem in selectedItems]

        # Setting the property view up
        if len(selectedModels) > 0:
            self.propertiesView.setModel(selectedModels)
        else:
            self.propertiesView.setEnabled(False)

    def onPlotterSelection(self):
        # Verifying if there is any Plotter selected
        selectedIndex = self.plotterList.currentIndex().row()
        if selectedIndex >= 0:

            # Getting the model of the selected plotter by index
            model = self.session.plotter_models[selectedIndex]

            # Setting up the current selected model
            if model != self.visorView.model:
                self.visorView.setModel(self.session.plotter_models[selectedIndex])
                self.canvasList.setCurrentWidget(self.canvas[selectedIndex])
                model.adjustSizeOfXAxis()
                model.adjustSizeOfYAxis()

            # Loading its GraphFunctions
            self.updateFunctionList()

    def onAdd(self):
        dialog = PlotterDialog()
        if dialog.exec():

            if dialog.name.text() in [plotter_model.name for plotter_model in self.session.plotter_models]:
                QMessageBox.warning(self,
                                    "Error message",
                                    "Error detected adding a new graph. Name already used!")
            else:
                # Creating model, view, data instances
                plotterData = GraphPlotter(get_magnitude_from_string(dialog.xMagnitude.currentText()),
                                           dialog.name.text())
                self.addPlotter(plotterData)

    def addPlotter(self, plotterData: GraphPlotter):
        # Creating instances
        plotterModel = GraphPlotterModel(plotterData)
        plotterView = GraphPlotterFigureView(plotterModel)
        figureCanvas = FigureCanvas(plotterView)

        # Connections between objects
        plotterModel.hasChanged.connect(self.updatePlotterList)
        plotterView.setFigureCanvas(figureCanvas)
        self.session.addPlotterModel(plotterModel)
        self.canvas.append(figureCanvas)
        self.views.append(plotterView)
        self.canvasList.setCurrentIndex(self.canvasList.addWidget(figureCanvas))

        # Update list status
        self.updatePlotterList()

    def onDelete(self):
        if len(self.session.plotter_models):
            if QMessageBox.question(self,
                                    "Deleting graph",
                                    "Are you sure you want to delete?",
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
                self.visorView.removeModel()

                # Update plotter list and resets selection
                self.updatePlotterList()

    def onImageExportAction(self):
        if not self.verifySelection():
            return

        dialog = QFileDialog()
        dialog.setDefaultSuffix(".png")
        dialog.setAcceptMode(QFileDialog.AcceptSave)

        if dialog.exec():
            file_path = dialog.selectedFiles()
            if len(file_path) > 1:
                QMessageBox.warning(self,
                                    "Error message",
                                    "Only one .png image will be saved!")
            else:
                plotter_view = self.views[self.plotterList.currentIndex().row()]
                plotter_view.savefig(
                    file_path[0],
                    dpi=600,
                    format="png"
                )

    @staticmethod
    def onAboutAction():
        dialog = AboutDialog()
        dialog.exec()

    def onFromExcelAction(self):
        if not self.verifySelection():
            return

        functions = spreadsheet_sv()
        if functions is not None:
            for function in functions:
                if not self.session.plotter_models[self.plotterList.currentIndex().row()].addGraph(function):
                    QMessageBox.warning(self,
                                        "Error message",
                                        "Cannot add new graph. " +
                                        "Name already used, invalid x magnitude or maximum graphs exceeded (20)")

    def onFromLTSpiceAction(self):
        if self.verifySelection():
            self.loadFunctionsFromDialog(LTSpiceDialog())

    def onTransferAction(self):
        if self.verifySelection():
            self.loadFunctionsFromDialog(TransferDialog())

    def loadFunctionsFromDialog(self, dialog):
        if dialog.exec():
            graphFunctions = dialog.getGraphFunction()
            for graphFunction in graphFunctions:
                if not self.session.plotter_models[self.plotterList.currentIndex().row()].addGraph(graphFunction):
                    QMessageBox.warning(self,
                                        "Error message",
                                        "Cannot add new graph. " +
                                        "Name already used, invalid x magnitude or maximum graphs exceeded (20)")
                    break

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
                                        "Cannot add new graph. " +
                                        "Name already used, invalid x magnitude or maximum graphs exceeded (20)")


def main():
    app = QApplication([])
    window = Window()
    app.exec()


if __name__ == "__main__":
    main()
