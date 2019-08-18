from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


from LTSpice_feature.designer.file_select_dialog.FileSelectDialog_ui import Ui_Dialog
from LTSpice_feature.view.browserDialog import App
from LTSpice_feature.reader.ltspice_reader_interface import LTSpiceReaderInterface

# Luqui's stuff
from plot_tool.data.magnitudes import get_magnitude_from_string
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog


class FileSelectDialog(GraphFunctionDialog, Ui_Dialog):

    fileBrowser = App
    isMc = False
    data = dict()

    def __init__(self, *args, **kwargs):
        super(FileSelectDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.okButton.setEnabled(False)

        self.filepathPTE.setPlaceholderText("Type a path or browse")
        self.filepathPTE.setReadOnly(False)

        self.browseButton.setEnabled(True)
        self.browseButton.released.connect(self.browseButtonClicked)

        self.mcCheckBox.stateChanged.connect(self.changeHandler)

        self.loadFilePB.setEnabled(True)
        self.loadFilePB.released.connect(self.fileLoaderHandler)

        self.dataSelectionGB.setEnabled(False)

        self.functionSettingGB.setEnabled(False)

        self.functionList.setEnabled(False)

        self.addButton.setEnabled(False)

        self.deleteButton.setEnabled(False)

    def browseButtonClicked(self):
        filePath = self.fileBrowser.openFileNameDialog(self)
        if filePath is not None:
            self.filepathPTE.clear()
            self.filepathPTE.insertPlainText(filePath)

    def fileLoaderHandler(self):

        if len(self.filepathPTE.text()):
            try:
                ltspicereader = LTSpiceReaderInterface(self.filepathPTE.text(),self.isMc)
                self.data = ltspicereader.get_data()
                print(self.data["y_axis_0"])
            except:
                print("error")
        print(self.plainTextEdit.toPlainText())
"""
    def changeHandler(self):
        if self.mcCheckBox.isChecked():
            self.isMc = True
        else:
            self.isMc = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    dialog = FileSelectDialog()
    dialog.show()
    sys.exit(app.exec())

