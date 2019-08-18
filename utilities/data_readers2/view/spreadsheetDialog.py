import time
from PyQt5.QtWidgets import QApplication
from utilities.data_readers2.designer.spreadsheet_dialog import Ui_Dialog
from utilities.data_readers2.dataReader import DataReader
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from PyQt5 import QtCore, QtGui, QtWidgets


class SpreadsheetDialog(QtWidgets.QDialog, Ui_Dialog):
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

        self.addButton.clicked.connect(self.onAdd)
        self.deleteButton.clicked.connect(self.onDelete)

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

    def onAdd(self):
        pass

    def onDelete(self):
        pass

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
                if self.addButton.
                return
        #self.okButton.setEnabled(False)

        '''
        if len(self.plainTextEdit.text()):
            #self.received = self.plainTextEdit.0
            if self.comboBox_3.currentText() != self.comboBox_4.currentText():

                if self.waveformsInput.currentText() == "Sinusoidal":
                    if self.sinAmplitude.value() != 0.0 and self.sinFrequency.value() != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Step":
                    if self.stepAmplitude.value() != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Square":
                    if self.squareAmplitude.value() != 0.0 \
                            and self.squareFrequency.value() != 0.0 and self.squareDuty != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Triangle":
                    if self.triangleAmplitude.value() != 0.0 \
                            and self.triangleFrequency.value() != 0.0 and self.triangleSymmetry != 0.0:
                        self.buttonBox.setEnabled(True)
                        return


        self.buttonBox.setEnabled(False)
        '''

