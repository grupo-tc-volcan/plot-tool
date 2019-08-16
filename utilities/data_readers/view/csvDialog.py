from PyQt5.QtWidgets import QApplication

from utilities.data_readers.designer.csvDialog_ui import Ui_Dialog
from utilities.data_readers.dataReader import DataReader
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues

class CsvDialog(Ui_Dialog):
    '''Csv Dialog'''

    def __init__(self,drr,*args,**kwargs):
        super(CsvDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.dr = drr

        self.comboBox_3.addItems([magnitude.value for magnitude in GraphMagnitude])
        self.comboBox_4.addItems([magnitude.value for magnitude in GraphMagnitude])
        self.comboBox.addItems(self.dr.get_file_data_names())
        self.comboBox_2.addItems(self.dr.get_file_data_names())

        self.plainTextEdit.textChanged.connect(self.onChanges)

    def onChanges(self):
        pass

