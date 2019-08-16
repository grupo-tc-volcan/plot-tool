
import pandas as pd
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
            print(self.data)
        elif os.path.splitext(base)[1] == ".txt":
            print("es un txt")
            self.data = pd.read_csv(self.file_path, sep='[,\t]', encoding="latin_1", decimal=".")
            print(self.data)
        elif (os.path.splitext(base)[1] == ".xls") or (os.path.splitext(base)[1] == ".xlsx"):
            self.data = pd.read_excel('xlsTest.xlsx')  # , sheetname='Sheet1')
            # print("Column headings:")
            # print(df.columns)
            print(self.data)
        # self.data_names = list(self.data.columns)
        self.data_names = list(self.data.columns.values)  # returns an array of index
        # self.data_names = list(self.data.columns.values.tolist())
        print(self.data_names)
        return (self.data_names)

    def import_file_data(self, x_col_name, x_col_number, y_col_name, y_col_number):
        '''
        Imports x and y values from a data file. The x and y columns returned
        are specified by the received parameters.

        :param file_path: Path of the file from which data will be imported.
        :param x_col_name: Name of the file's column that contains the x values.
        :param x_col_number: Number of the file's column that contains the x values.
        :param y_col_name: Name of the file's column that contains the y values.
        :param y_col_number: Number of the file's column that contains the x values.
        :return: x and y values (tuple (?)).
        '''

        self.data.sort_values(by=x_col_name, axis='index', inplace=True, ascending=True, na_position='last')
        self.data = self.data.reset_index(drop=True)
        # --- TO DO (1): Dependiendo de si trabajamos con nombre o numero de fila, determinar si usamos formato x o x2
        # x = self.data.loc[:, x_col_name]
        x = self.data.loc[:, self.data.columns[x_col_number]]
        # y = self.data.loc[:, y_col_name]
        y = self.data.loc[:, self.data.columns[y_col_number]]
        # --- (HASTA ACA (1))
        return (x, y)