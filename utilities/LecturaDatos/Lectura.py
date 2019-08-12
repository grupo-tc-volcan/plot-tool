import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime

NOMBRE_CSV = "csvTest.csv" #RECIBIRLO CON LA DIRECCION!!!

class Info:
    def __init__(self,freq_):
        self.freq = freq_
        # self.freq = None
        self.amp = None
        self.phase = None
        self.eventos = []

    def nuevoDato(self,dato): #dato es una linea entera del csv
        self.eventos.append(dato)
    def procesarInfo(self):
        self.amp = self.eventos[0]['Amplitude']
        self.phase = self.eventos[0]['Phase']
    #     print("Procesando info.\n")
    # def validarDatos(self):
    #     print("Validando datos.\n")
    # def graficar(self):
    #     print("Graficando datos.\n")

def main():
    archivo = pd.read_csv(NOMBRE_CSV, delimiter = ";",encoding = "ISO-8859-1", decimal= ",") #SI SE USA DECIMAL CON PUNTO, CAMBIAR!
    archivo = archivo.sort_values(by = 'Freq')
    data = archivo.to_dict("index")
    puntos = dict()

    for dato in data.keys():
        freq = data[dato]['Freq']
        if freq in puntos:
            puntos[freq].nuevoDato(data[dato])
        else:
            puntos[freq] = Info(freq)
            puntos[freq].nuevoDato(data[dato])
        for info in puntos.keys(): #EN VEZ DE ESTO, QUE GRAFIQUE
            puntos[info].procesarInfo()

    #for info in puntos.keys():
            #   trackRow = puntos[info][freq]
            #       puntos[info][amp]
    #       puntos[info][phase]


    for punto in puntos:
        freqs[punto] = puntos[punto].freq
        amps[punto] = puntos[punto].amp
        phases[punto] = puntos[punto].phase

    #print "Value : %s" % puntos.keys()
    # freqs = []
    # amps = []
    # phases = []
    # # for punto in puntos:
    # #     freqs[punto] = puntos[punto].freq
    # #     amps[punto] = puntos[punto].amp
    # #     phases[punto] = puntos[punto].phase
    #
    # plt.figure(1)
    # plt.subplot(211)
    # plt.semilogx(freqs, amps)  # Bode magnitude plot
    # # plt.figure(2)
    # plt.subplot(212)
    # plt.plot(freqs, phases)  # Bode phase plot
    # plt.show()
    #
    # fig, axs = plt.subplots(2)
    # fig.suptitle('Vertically stacked subplots')
    # axs[0].plot(freqs, amps)
    # axs[1].plot(preqs, phases)

    csvHeaders = ['Freq', 'Amp', 'Phase']
    with open('Resultados.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(csvHeaders)
        for info in puntos.keys():
            trackRow = [puntos[info].freq,
                        puntos[info].amp,
                        puntos[info].phase]
            writer.writerow(trackRow)
    csvFile.close()


main()




#camiones: puntos
#camion: info
#Camion: Info
#Dominio: Freq
#dominio: freq