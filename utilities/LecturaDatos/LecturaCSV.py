import pandas as pd
import matplotlib.pyplot as plt
import csv
#import datetime

DEBUG = True
#NOMBRE_CSV = "/Users/malemuller/Desktop/TC/TP1/EJ3/csvTest.csv"
NOMBRE_CSV = "csvTest.csv" #HACER: USAR LA DIRECCION COMO VARIABLE, recibirla!!!


def main():
    info = pd.read_csv(NOMBRE_CSV, names=['freq', 'amp', 'phase'],
                       header=0, delimiter=";", encoding="utf-8",
                       decimal=",")  # SI SE USA DECIMAL CON PUNTO, CAMBIAR delimiter!
    # info = pd.read_csv(NOMBRE_CSV, delimiter = ";",encoding = "utf-8", decimal= ",")
    if DEBUG:
        print(info)
    info.sort_values(by='freq', axis='index', inplace=True, ascending=True, na_position='last')
    info = info.reset_index(drop=True)
    if DEBUG:
        print(type(info['freq']))
        print(info)
        for i in range(len(info)):
            print("frecuencia: " + str(info['freq'][i]))
        print(info)


main()