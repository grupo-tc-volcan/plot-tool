
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import csv
import os

class DataReader:
    def __init__(self, _file_path):
        self.file_path = _file_path


    def get_file_data_names(self):
        '''
        This function receives a data-stored-file's path and returns the names
        of its data columns.
        :param file_path: Path of the file from which data names will be returned.
        :return: The names of each of the data columns.
        '''
        base = os.path.basename(self.file_path)
        if os.path.splitext(base)[1] == ".csv":
            self.data = pd.read_csv(self.file_path, delimiter=";", encoding="utf-8", decimal=",")
        elif os.path.splitext(base)[1] == ".txt":
            self.data = pd.read_csv(self.file_path, sep='[,\t]', encoding="latin_1", decimal=".")
        elif (os.path.splitext(base)[1] == ".xls") or (os.path.splitext(base)[1] == ".xlsx"):
            self.data = pd.read_excel(self.file_path)#('xlsTest.xlsx')  # , sheetname='Sheet1')

        self.data_names = list(self.data.columns.values)  # returns an array of index

        #Checking which columns contain numbers and which ones don't,
        #in order to save only the data_names corresponding to numeric values:
        for i in list(self.data.columns.values):
            col = self.data.loc[:, i]
            for j in col:
                if ((type(j) is not float) and (type(j) is not int)):
                    if i in self.data_names:
                        self.data_names.remove(i)
        return (self.data_names)

    def import_file_data(self, x_col_name, y_col_name):
        '''
        Imports x and y values from a data file. The x and y columns returned
        are specified by the received parameters.
        :param file_path: Path of the file from which data will be imported.
        :param x_col_name: Name of the file's column that contains the x values.
        :param y_col_name: Name of the file's column that contains the y values.
        :return: x and y values (tuple (?)).
        '''
        self.data.sort_values(by=x_col_name, axis='index', inplace=True, ascending=True, na_position='last')
        self.data = self.data.reset_index(drop=True)
        x = self.data.loc[:, x_col_name]
        y = self.data.loc[:, y_col_name]
        return (x, y)