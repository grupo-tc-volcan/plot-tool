from utilities.data_readers2.dataReader import DataReader
from utilities.data_readers2.view.browserDialog import App
from utilities.data_readers2.view.spreadsheetDialog import SpreadsheetDialog

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
DEBUG = False


def testing():
    '''
    #file_path = "xlsTest.xlsx"
    #file_path = "txtTest2.txt"
    #file_path = "csvTest.csv"
    #x_col_name = "Freq."
    x_col_name = "Freq"
    x_col_number = 0
    y_col_name = "Amplitude"
    #y_col_name = "I(L1)"
    y_col_number = 1
    '''
    app = QApplication(sys.argv)
    ex = App()
    file_path = ex.openFileNameDialog()

    myFile = DataReader(file_path)
    data_columns = myFile.get_file_data_names()


    app2 = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SpreadsheetDialog(myFile)
    ui.show()
    app2.exec_()

    print("ui.xAxis:")
    print(ui.xAxis_)
    print(ui.xMagnitude_)
    print("ui.yAxis:")
    print(ui.yAxis_)
    print(ui.yMagnitude_)
    print("ui.name:")
    print(ui.name_)
    #input_data = myFile.import_file_data(x_col_name, x_col_number, y_col_name, y_col_number)
    input_data = myFile.import_file_data(ui.xAxis_,ui.yAxis_)
    print(input_data)
    print("data type:")
    print(type(input_data))
    print(input_data[0])
    xData = list(input_data[0])
    yData = list(input_data[1])
    print("data TYPE:")
    print(type(xData))
    print(ui.functions)
    return(ui.functions)
    #return(ui.xMagnitude_, ui.yMagnitude_,  input_data[0],input_data[1])


def main():
    gf = []
    gf = testing()
    print("GF:")
    print(gf)
    print(gf[0].name)
main()