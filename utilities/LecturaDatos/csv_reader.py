import pandas as pd
import matplotlib.pyplot as plt
import csv
#import datetime

DEBUG = True

CSV_NAME = "csvTest.csv" #TO DO: RECEIVE DIRECTORY, instead of name as a constant!!


def main():
    info = pd.read_csv(CSV_NAME, names=['freq', 'amp', 'phase'],
                       header=0, delimiter=";", encoding="utf-8",
                       decimal=",")
    # info = pd.read_csv(CSV_NAME, delimiter = ";",encoding = "utf-8", decimal= ",")
    if DEBUG:
        print(info)
    info.sort_values(by='freq', axis='index', inplace=True, ascending=True, na_position='last')
    info = info.reset_index(drop=True)
    if DEBUG:
        print(type(info['freq']))
        print(info)
        for i in range(len(info)):
            print("frequency: " + str(info['freq'][i]))
        print(info)


main()