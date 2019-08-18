from LTSpice_feature.reader.ltpice_reader import LTSpiceReader
from LTSpice_feature.reader.ltspice_bode_reader import LTSpiceBodeReader
from LTSpice_feature.reader.ltspice_time_graph_reader import LTSpiceTimeGraphReader

class LTSpiceReaderInterface:
    reader = None # used as a class to read the desired LTSpice file
    isBode = False
    data = dict()

    def __init__(self, filepath, isMc):
        self.reader = LTSpiceReader(filepath)
        if self.reader.isBode():
            self.reader = LTSpiceBodeReader(filepath, isMc)
        else:
            self.reader = LTSpiceTimeGraphReader(filepath, isMc)
       self.data = self.reader.get_data()

    def get_y_axis_labels(self):
        labels = []
        for y_var in range(0, self.reader.get_y_axis_var_count()):
           labels.append( self.data["y_axis_" + string(yvar)])

        return labels

    def get_x_axis_values(self):
        return self.data["x_axis"]

    def get_y_axis_values(self, *list_of_vars, number_of_steps = self.reader.get_mc_steps()):
        vars_list = list(range(list_of_vars))
        inverted_data = {v: k for k, v in self.data.items()} #inverting data list to have access with variable names
        values = []
        for variable in vars_list:
            for step in range(number_of_steps):
            self.data["y_

        #esra parte esta picante, basicamente me devuelve I(C!)_Phase, I(C1)_Module y lo tengo que traducir a mi
        # convenvion de abs_y_axis_0_step1 pha_y_axis_0_step1 (esto si es bode, si es en el tiempo es facil porque los
            # datos se corresponcen con una variable) si soluciono esto sale al toque el resto. estoy muy quemado
            #no puedo seguir asi