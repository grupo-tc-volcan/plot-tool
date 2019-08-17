import time
from PyQt5.QtWidgets import QApplication
from utilities.data_readers.designer.csvDialog_ui import Ui_Dialog
from utilities.data_readers.dataReader import DataReader
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from PyQt5 import QtCore, QtGui, QtWidgets

class CsvDialog(QtWidgets.QDialog, Ui_Dialog):
    '''Csv Dialog'''

    def __init__(self, dr_, *args, **kwargs):
    #def __init__(self, *args, **kwargs):
        super(CsvDialog, self).__init__(*args, **kwargs)
        self.dr = dr_
        self.setupUi(self)

        self.plainTextEdit.insertPlainText("Insert name")
        self.comboBox_3.addItems([magnitude.value for magnitude in GraphMagnitude]) #x magnitude
        self.comboBox_4.addItems([magnitude.value for magnitude in GraphMagnitude])# y magnitude
        self.comboBox.addItems(self.dr.get_file_data_names())#x axis
        self.comboBox_2.addItems(self.dr.get_file_data_names())#y axis

        self.comboBox_3.currentIndexChanged.connect(self.onChanges)
        self.comboBox_4.currentIndexChanged.connect(self.onChanges)
        self.comboBox.currentIndexChanged.connect(self.onChanges)
        self.comboBox_2.currentIndexChanged.connect(self.onChanges)


        #self.buttonBox.setEnabled(False)
        self.plainTextEdit.textChanged.connect(self.onChanges)
        #print(self.dr.get_file_data_names)
        #self.initUI()

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



    def onChanges(self):
        print("onChanges")
        #print("Text changed...>>> " + self.plainTextEdit.toPlainText())
        #self.inputText = self.inputText + self.plainTextEdit.toPlainText()
        print("input:")
        #print(self.plainTextEdit.currentText())

        #self.myText = self.plainTextEdit.toPlainText()
        self.myText = self.plainTextEdit.toPlainText()
        print(self.myText)
        print("comboBox_3")
        print(self.comboBox_3.currentText())
        #self.plainTextEdit.insertPlainText(self.myText)
        #self.buttonBox.setEnabled(True)
        '''
        if len(self.plainTextEdit.text()):
            print("T")
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
