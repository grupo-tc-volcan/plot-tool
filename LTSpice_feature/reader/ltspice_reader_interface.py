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
            self.isBode = True
        else:
            self.reader = LTSpiceTimeGraphReader(filepath, isMc)
            self.isBode = False
        self.data = self.reader.get_data()

    def get_y_axis_labels(self):
        labels = []
        for y_var in range(0, self.reader.get_y_axis_var_count()):
            labels.append(self.data['y_axis_' + str(y_var)])
        return labels

    def get_x_axis_values(self):
        return self.data['x_axis']

    def is_bode(self):
        return self.isBode

    def get_y_axis_values(self, *selected_vars, number_of_steps = 0):

        if number_of_steps == 0:
            number_of_steps = self.reader.get_mc_steps()
        vars_list = list(range(*selected_vars))
        inverted_data = {v: k for k, v in self.data.items()} # inverting data list to have access with variable names
        values = []
        if not self.isBode:     # if not working with a bode plot variable name corresponds to its place in data
            for variable in vars_list:
                for step in range(1, number_of_steps):
                    values.append(self.data[inverted_data[vars_list[variable]] + '_step' + string(step)])
            return values
        else:               # for a bode it's a little more complicated because of phase and module values
            print("not finished yet")

        # esra parte esta picante, basicamente me devuelve I(C1)_Phase, I(C1)_Module y lo tengo que traducir a mi
        # convenvion de abs_y_axis_0_step1 pha_y_axis_0_step1 (esto si es bode, si es en el tiempo es facil porque los
            # datos se corresponcen con una variable) si soluciono esto sale al toque el resto. estoy muy quemado
            # no puedo seguir asi

