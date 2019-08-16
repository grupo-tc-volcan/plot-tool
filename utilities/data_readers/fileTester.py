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

    '''
    #app = QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog = CsvDialog(myFile)
    Dialog.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    #app.exec()
    

    input_data = myFile.import_file_data(x_col_name, x_col_number, y_col_name, y_col_number)
    '''
    print("hola1")
    app2 = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CsvDialog(myFile)#Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app2.exec_())
    print("hola2")
    input_data = myFile.import_file_data(x_col_name, x_col_number, y_col_name, y_col_number)
    '''
    if DEBUG:
        print("data received:")
        print(input_data[0])
        print(input_data)
        print("data type:")
        print(type(input_data))
    '''

def hola():
    app2 = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app2.exec_())

main()