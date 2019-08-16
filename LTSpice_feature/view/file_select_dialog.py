from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from LTSpice_feature.designer.file_select_dialog.FileSelectWindow_ui import *

# Luqui's stuff
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues


class ShittyLTSpiceReader(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(ShittyLTSpiceReader, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.buttonBox.setEnabled(False)

        self.plainTextEdit.setPlaceholderText("Type a path or browse")
        self.plainTextEdit.textChanged.connect(self.changeHandler)

        self.BrowseButton.setEnabled(True)
        self.BrowseButton.released.connect(self.changeHandler)

        self.checkBox.stateChanged.connect(self.changeHandler)

    def changeHandler(self):
       print(asdjkabsdkj)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    dialog = ShittyLTSpiceReader()
    dialog.show()
    sys.exit(app.exec())

