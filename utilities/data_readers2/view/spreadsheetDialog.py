#from utilities.data_readers2.Drafts.spreadsheet_dialog import Ui_Dialog
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from utilities.data_readers2.designer.spreadsheet_dialog import Ui_Dialog
from utilities.data_readers2.dataReader import DataReader
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class SpreadsheetDialog(QtWidgets.QDialog, Ui_Dialog, DataReader):
    '''SpreadsheetDialog'''
    def __init__(self, dr_, *args, **kwargs):
        super(SpreadsheetDialog, self).__init__(*args, **kwargs)
        self.dr = dr_
        self.setupUi(self)

        self.xMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])  # x magnitude
        self.yMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])  # y magnitude
        self.xAxis.addItems(self.dr.get_file_data_names())  # x axis
        self.yAxis.addItems(self.dr.get_file_data_names())  # y axis

        self.xMagnitude.currentIndexChanged.connect(self.onChanges)
        self.yMagnitude.currentIndexChanged.connect(self.onChanges)
        self.xAxis.currentIndexChanged.connect(self.onChanges)
        self.yAxis.currentIndexChanged.connect(self.onChanges)

        self.name.textChanged.connect(self.onChanges)
        self.functionList.currentItemChanged.connect(self.onSelection)
        self.addButton.clicked.connect(self.onAdd)
        self.deleteButton.clicked.connect(self.onDelete)

        self.addButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.okButton.setEnabled(False)

        self.functions = list()
        self.functionsNames = list()


    def onSelection(self):
        selectedIndex = self.functionList.currentIndex().row()
        if selectedIndex >= 0:
            self.deleteButton.setEnabled(True)


    def onAdd(self):
        self.addButton.setEnabled(False)
        if self.name_ in self.functionsNames:
            QMessageBox.warning(self,
                                "Error message",
                                "Error detected adding a new function. Name already used!")
        else:
            self.input_data = self.dr.import_file_data(self.xAxis_, self.yAxis_)
            self.xData = list(self.input_data[0])
            self.yData = list(self.input_data[1])
            self.gValues = GraphValues(list(self.input_data[0]), list(self.input_data[1]))
            self.newFunction = GraphFunction(self.name_, self.gValues, self.xMagnitude_, self.yMagnitude_)
            self.functions.append(self.newFunction)
            self.functionsNames.append(self.newFunction.name)
            self.updateFunctionList()
            self.okButton.setEnabled(True)


    def updateFunctionList(self):
        selectedIndex = self.functionList.currentIndex()
        self.functionList.clear()
        self.functionList.addItems(self.functionsNames)
        self.functionList.setCurrentIndex(selectedIndex)
        if len(self.functionList) == 0:
            self.okButton.setEnabled(False)

    def onDelete(self):
        selectedIndex = self.functionList.currentIndex().row()
        selectedItem = self.functionList.currentRow()
        self.deleteButton.setEnabled(False)
        if selectedIndex >= 0:
            self.functionsNames.remove(self.functionsNames[selectedIndex])
            self.functions.remove(self.functions[selectedIndex])
            self.updateFunctionList()
            print("functions names:")
            print(self.functionsNames)
            print("functions:")
            for i in self.functions:
                print(i.name)

    def onChanges(self):
        self.myText = self.name.text()
        self.xMagnitude_ = self.xMagnitude.currentText()
        self.yMagnitude_ = self.yMagnitude.currentText()
        self.name_ = self.name.text()
        self.xAxis_ = self.xAxis.currentText()
        self.yAxis_ = self.yAxis.currentText()
        if len(self.name.text()):
            if self.xAxis.currentText() != self.yAxis.currentText():
                self.addButton.setEnabled(True)
            else:
                self.addButton.setEnabled(False)
        else:
            self.addButton.setEnabled(False)


