'''
TO DO:
    (1) Definir si usamos numero o nombre de columna para acceder a la misma.
    (2) VERIFICAR QUE LA COLUMNA EXISTA, YA SEA NUMERO O NOMBRE.
    (4) Averiguar paths.
    (5) Agregar la parte de ltspice.
    (6) Ver si input data se guarda en algún lado o no.
    (7) Agregar caso .txt.
    (8) Meter todo esto en una clase DataReader o similar y que guarde data solo la primera vez que lo abre para buscar las cols.

'''
import pandas as pd
import matplotlib.pyplot as plt
import csv
#from pandas import ExcelWriter
#from pandas import ExcelFile
import os

DEBUG = False

class DataReader:
    def __init__(self,_file_path):
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
        # else:
        #    print("Incorrect file extension")
        '''
        #--- TO DO (2)
        VERIFICAR QUE LA COLUMNA EXISTA, YA SEA NUMERO O NOMBRE
        if (x_col_number >= len(data.columns)) or (y_col_number >= len(data.columns)):
            print(ERROR)
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


def main(): #FOR TEST
    #file_path = "xlsTest.xlsx"
    #file_path = "txtTest2.txt"
    file_path = "csvTest.csv"
    #x_col_name = "Freq."
    x_col_name = "Freq"
    x_col_number = 0
    y_col_name = "Amplitude"
    #y_col_name = "I(L1)"
    y_col_number = 1

    #data_columns = get_file_data_names(file_path)
    #input_data = import_file_data(file_path, x_col_name, x_col_number, y_col_name, y_col_number)


    myFile = DataReader(file_path)
    data_columns = myFile.get_file_data_names()
    input_data = myFile.import_file_data(x_col_name, x_col_number, y_col_name, y_col_number)

    if DEBUG:
        print("data received:")
        print(input_data[0])
        print(input_data)
        print("data type:")
        print(type(input_data))

main()