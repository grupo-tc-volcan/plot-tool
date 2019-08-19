import time
from utilities.data_readers.dataReader import DataReader
from utilities.data_readers.view.browserDialog import App
from utilities.data_readers.view.csvDialog import CsvDialog
from utilities.data_readers.designer.csvDialog_ui import Ui_Dialog

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
DEBUG = False


def main():
    #file_path = "xlsTest.xlsx"
    #file_path = "txtTest2.txt"
    #file_path = "csvTest.csv"
    #x_col_name = "Freq."
    x_col_name = "Freq"
    x_col_number = 0
    y_col_name = "Amplitude"
    #y_col_name = "I(L1)"
    y_col_number = 1

    app = QApplication(sys.argv)
    ex = App()
    #sys.exit(app.exec_())
    file_path = ex.openFileNameDialog()
    print(file_path)
    
    myFile = DataReader(file_path)
    data_columns = myFile.get_file_data_names()

    print("hola1")
    app2 = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CsvDialog(myFile)
    #ui.setupUi(Dialog)
    print("HOLA234")
    #Dialog.show()
    ui.show()
    print("HOLA567")
    app2.exec_()
    print("hola2")

    print("ui.xAxis:")
    print(ui.xAxis)
    print(ui.xMagnitude)
    print("ui.yAxis:")
    print(ui.yAxis)
    print(ui.yMagnitude)
    print("ui.name:")
    print(ui.name)
    #input_data = myFile.import_file_data(x_col_name, x_col_number, y_col_name, y_col_number)
    input_data = myFile.import_file_data(ui.xAxis,ui.yAxis)
    print(input_data)
    print("data type:")
    print(type(input_data))
    print(input_data[0])
    xData = input_data[0]
    yData = input_data[1]

    return(ui.xMagnitude, ui.yMagnitude,  input_data[0],input_data[1])


main()