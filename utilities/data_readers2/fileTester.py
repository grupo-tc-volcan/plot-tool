from utilities.data_readers2.dataReader import DataReader
from utilities.data_readers2.view.browserDialog import App
from utilities.data_readers2.view.spreadsheetDialog import SpreadsheetDialog

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
DEBUG = False


def main():
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

    '''
    input_data = myFile.import_file_data(ui.xAxis_,ui.yAxis_)
    xData = list(input_data[0])
    yData = list(input_data[1])
    '''
    print("ui functions")
    print(ui.functions)
    # return(ui.functions)

    #return(ui.xMagnitude_, ui.yMagnitude_,  input_data[0],input_data[1])

'''
def main():
    gf = []
    gf = testing()
    print("GF:")
    print(gf)
    print(gf[0].name)
'''

main()