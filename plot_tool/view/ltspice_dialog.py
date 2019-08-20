# python native modules

# third-party modules
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog
from plot_tool.designer.ltspice_dialog.ltspice_dialog_ui import Ui_Dialog

from utilities.ltspice.ltspice_reader_interface import LTSpiceReaderInterface


# noinspection PyBroadException
class LTSpiceDialog(GraphFunctionDialog, Ui_Dialog):

    isMc = False
    ltSpiceReader = None
    data = dict()
    previousFilePath = ''

    def __init__(self, *args, **kwargs):
        super(LTSpiceDialog, self).__init__(*args, **kwargs)
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
        self.addButton.released.connect(self.addVar)

        self.deleteButton.setEnabled(False)
        self.deleteButton.released.connect(self.deleteVar)

    def browseButtonClicked(self):
        filePath, _ = QFileDialog.getOpenFileName()     # is browse button is clicked, open file browser
        if filePath is not None:
            self.filepathPTE.clear()                    # delete old stinky filepath
            self.filepathPTE.insert(filePath)           # write new filepath for the user to read

    def fileLoaderHandler(self):
        if len(self.filepathPTE.text()) and (self.filepathPTE.text() != self.previousFilePath):
            self.previousFilePath = self.filepathPTE.text()
            try:
                self.ltSpiceReader = LTSpiceReaderInterface(self.filepathPTE.text(), self.isMc)
                self.data = self.ltSpiceReader.get_y_axis_labels()
            except:                                    # if you read the documentation this line will most probably
                QtWidgets.QMessageBox.critical(self,   # never execute (we know,it will execute and you will be sad)
                                               'Fatal Error',
                                               'There was an error while reading '
                                               + self.filepathPTE.text()
                                               + ' please check if the path and file '
                                                 'formatting are correct and try again')
                self.previousFilePath = ''              # this is to let you retry to load the same file that we told
                return                                  # you was incorrect just to make sure

            self.yAxis.clear()          # after loading a CORRECTLY FORMATTED file useful options will be activated
            self.yMagnitude.clear()
            self.functionList.clear()
            self.dataSelectionGB.setEnabled(True)

            self.functionSettingGB.setEnabled(True)

            self.yAxis.addItems(self.data)

            self.functionList.setEnabled(True)

            self.addButton.setEnabled(True)

            if not self.ltSpiceReader.is_bode():
                self.yMagnitude.setEnabled(True)
                self.yMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude
                                          if magnitude == GraphMagnitude.Voltage
                                          or magnitude == GraphMagnitude.Current])
                self.amplitudeCB.setEnabled(False)
                self.phaseCB.setEnabled(False)
            else:
                self.amplitudeCB.setEnabled(True)
                self.phaseCB.setEnabled(True)
                self.yMagnitude.setEnabled(False)

    def changeHandler(self):
        if self.mcCheckBox.isChecked():
            self.isMc = True
        else:
            self.isMc = False

    def addVar(self):
        # You are not meant to understand this, just adds the variable to the list and to a buffer inside the reader
        if not self.ltSpiceReader.is_bode():
            if not self.functionList.findItems(self.yAxis.currentText() + ', ' + self.yMagnitude.currentText()
                                               , QtCore.Qt.MatchExactly):
                self.functionList.addItem(self.yAxis.currentText() + ', ' + self.yMagnitude.currentText())
                self.ltSpiceReader.add_function_to_list(self.yAxis.currentText() + ', ' + self.yMagnitude.currentText())
        else:

            if self.amplitudeCB.isChecked():
                if not self.functionList.findItems(self.yAxis.currentText() + ', ' + GraphMagnitude.Decibel.value
                                                   , QtCore.Qt.MatchExactly):
                    self.functionList.addItem(self.yAxis.currentText() + ', ' + GraphMagnitude.Decibel.value)
                    self.ltSpiceReader.add_function_to_list(self.yAxis.currentText() +
                                                            ', ' + GraphMagnitude.Decibel.value)
            if self.phaseCB.isChecked():
                if not self.functionList.findItems(self.yAxis.currentText() + ', ' + GraphMagnitude.Phase.value
                                                   , QtCore.Qt.MatchExactly):
                    self.functionList.addItem(self.yAxis.currentText() + ', ' + GraphMagnitude.Phase.value)
                    self.ltSpiceReader.add_function_to_list(self.yAxis.currentText() +
                                                            ', ' + GraphMagnitude.Phase.value)

        if not self. okButton.isEnabled():
            self.okButton.setEnabled(True)
        if not self.deleteButton.isEnabled():
            self.deleteButton.setEnabled(True)

    def deleteVar(self):  # deletes selcted variable
        item = self.functionList.takeItem(self.functionList.currentRow())
        self.ltSpiceReader.remove_function_from_list(item.text())
        if self.okButton.isEnabled() and not self.functionList.count():
            self.okButton.setDisabled(True)
            self.deleteButton.setDisabled(True)

    def getGraphFunction(self) -> list:
        return self.ltSpiceReader.get_graph_functions()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    dialog = LTSpiceDialog()
    dialog.show()
    sys.exit(app.exec())
