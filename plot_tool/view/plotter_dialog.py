# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

# plot-tool modules
from plot_tool.designer.plotter_dialog.plotter_dialog import Ui_Dialog

from plot_tool.data.magnitudes import GraphMagnitude


class PlotterDialog(QDialog, Ui_Dialog):
    """ Plotter Dialog """

    def __init__(self, *args, **kwargs):
        super(PlotterDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setting up the view
        self.xMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])

        # Setting slots
        self.xMagnitude.currentTextChanged.connect(self.updateStatus)
        self.name.textChanged.connect(self.updateStatus)

    def updateStatus(self):
        if len(self.name.text()):
            self.buttonBox.setEnabled(True)
        else:
            self.buttonBox.setEnabled(False)


if __name__ == "__main__":
    app = QApplication([])
    dialog = PlotterDialog()
    dialog.exec()
    app.exec()
