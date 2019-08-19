from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidgetItem

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
    ltSpiceReader = None
    data = dict()
    previousFilePath = ''

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
        self.addButton.released.connect(self.addVar)

        self.deleteButton.setEnabled(False)
        self.deleteButton.released.connect(self.deleteVar)

    def browseButtonClicked(self):
        filePath = self.fileBrowser.openFileNameDialog(self)
        if filePath is not None:
            self.filepathPTE.clear()
            self.filepathPTE.insert(filePath)

    def fileLoaderHandler(self):
        if len(self.filepathPTE.text()) and (self.filepathPTE.text() != self.previousFilePath):
            self.previousFilePath = self.filepathPTE.text()
            try:
                self.ltSpiceReader = LTSpiceReaderInterface(self.filepathPTE.text(), self.isMc)
                self.data = self.ltSpiceReader.get_y_axis_labels()
            except:
                QtWidgets.QMessageBox.critical(self, 'Fatal Error', 'There was an error while reading '
                                               + self.filepathPTE.text()
                                               + ' please check if the path and file '
                                                 'formatting are correct and try again')
                return

            self.yAxis.clear()
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
                                                            ', ' + GraphMagnitude.Decibel.value)

        if not self. okButton.isEnabled():
            self.okButton.setEnabled(True)
        if not self.deleteButton.isEnabled():
            self.deleteButton.setEnabled(True)

    def deleteVar(self):
        item = self.functionList.takeItem(self.functionList.currentRow())
        self.ltSpiceReader.remove_function_from_list(item.text())
        if self.okButton.isEnabled() and not self.functionList.count():
            self.okButton.setDisabled(True)
            self.deleteButton.setDisabled(True)

    def getGraphFunction(self) -> list:
        return self.ltSpiceReader.get_functions()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    dialog = FileSelectDialog()
    dialog.show()
    sys.exit(app.exec())

