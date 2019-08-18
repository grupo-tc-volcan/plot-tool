from utilities.data_readers2.Drafts.spreadsheet_dialog import Ui_Dialog
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from utilities.data_readers2.dataReader import DataReader


class SpreadsheetDialog(QtWidgets.QDialog, Ui_Dialog, DataReader):
    '''Csv Dialog'''

    def __init__(self, dr_, *args, **kwargs):
        # def __init__(self, *args, **kwargs):
        super(SpreadsheetDialog, self).__init__(*args, **kwargs)
        self.dr = dr_
        self.setupUi(self)

        # self.name.setText("insert name")
        self.xMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])  # x magnitude
        self.yMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])  # y magnitude
        self.xAxis.addItems(self.dr.get_file_data_names())  # x axis
        self.yAxis.addItems(self.dr.get_file_data_names())  # y axis

        self.xMagnitude.currentIndexChanged.connect(self.onChanges)
        self.yMagnitude.currentIndexChanged.connect(self.onChanges)
        self.xAxis.currentIndexChanged.connect(self.onChanges)
        self.yAxis.currentIndexChanged.connect(self.onChanges)

        self.addButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.okButton.setEnabled(False)
        #self.name.textChanged(self.onChanges)
        self.name.textChanged.connect(self.onChanges)
        # print(self.dr.get_file_data_names)
        # self.initUI()

        self.functionList.currentItemChanged.connect(self.onSelection)

        self.addButton.clicked.connect(self.onAdd)
        self.deleteButton.clicked.connect(self.onDelete)
        #self.okButton.clicked.connect(self.onOk)
        self.functions = list()
        self.functionsNames = list()

    '''
    def setupUi(self, Reader):
        Reader.setObjectName("Reader")
    '''

    '''
    def initUI(self):
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    '''

    def onSelection(self):
        selectedIndex = self.functionList.currentIndex().row()

        if selectedIndex >= 0:
            self.deleteButton.setEnabled(True)

        #self.deleteButton.setEnabled(True)

    def onAdd(self):
        self.addButton.setEnabled(False)

        if self.name_ in self.functionsNames:
            QMessageBox.warning(self,
                                "Error message",
                                "Error detected adding a new function. Name already used!")
        else:
            self.input_data = self.dr.import_file_data(self.xAxis_, self.yAxis_)
            self.xData = list(self.input_data[0])
            print("x TYPE:")
            print(self.xData)
            print(type(self.xData))
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

    def onDelete(self):
        selectedIndex = self.functionList.currentIndex().row()
        selectedItem = self.functionList.currentRow()
        print("selected index:")
        print(selectedIndex)
        print(type(selectedIndex))
        print("selected item:")
        print(selectedItem)
        print(type(selectedItem))
        self.deleteButton.setEnabled(False)
        print("LEN FUNC LIST")
        print(len(self.functionList))
        if len(self.functionList) == 0:
            self.okButton.setEnabled(False)


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
        print("onChanges")
        # print("Text changed...>>> " + self.plainTextEdit.toPlainText())
        # self.inputText = self.inputText + self.plainTextEdit.toPlainText()
        # print(self.plainTextEdit.currentText())

        #self.myText = self.plainTextEdit.toPlainText()
        #self.name.setText(self.name.text())

        self.myText = self.name.text()
        #print(self.name.text())
        print(self.myText)
        print("xMagnitude:")
        print(self.xMagnitude.currentText())

        self.xMagnitude_ = self.xMagnitude.currentText()
        self.yMagnitude_ = self.yMagnitude.currentText()
        self.name_ = self.name.text()
        self.xAxis_ = self.xAxis.currentText()
        self.yAxis_ = self.yAxis.currentText()
        print(self.xAxis_)

        if len(self.name.text()):
            print("LEN")
            if self.xAxis.currentText() != self.yAxis.currentText():
                print("DISTINTOS")
                self.addButton.setEnabled(True)
                #return



