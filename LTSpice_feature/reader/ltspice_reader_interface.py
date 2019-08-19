from LTSpice_feature.reader.ltpice_reader import LTSpiceReader
from LTSpice_feature.reader.ltspice_bode_reader import LTSpiceBodeReader
from LTSpice_feature.reader.ltspice_time_graph_reader import LTSpiceTimeGraphReader
from plot_tool.data.function import GraphFunction
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues
from plot_tool.data.magnitudes import get_magnitude_from_string


class LTSpiceReaderInterface:
    reader = None  # used as a class to read the desired LTSpice file
    isBode = False
    data = dict()
    labels = dict()
    graphFunctionList = list()

    def __init__(self, filepath, isMc):
        self.reader = LTSpiceReader(filepath)
        if self.reader.isBode():
            self.reader = LTSpiceBodeReader(filepath, isMc)
            self.isBode = True
        else:
            self.reader = LTSpiceTimeGraphReader(filepath, isMc)
            self.isBode = False
        self.data = self.reader.get_data()
        for y_var in range(0, self.reader.get_y_axis_var_count()):
            self.labels[self.data['y_axis_' + str(y_var)]] = ''
            self.labels[self.data['y_axis_' + str(y_var)]] = 'y_axis_' + str(y_var)

    def get_y_axis_labels(self):
        labels = []
        for y_var in range(0, self.reader.get_y_axis_var_count()):
            labels.append(self.data['y_axis_' + str(y_var)])
        return labels

    def get_x_axis_values(self):
        return list(self.data['x_axis'])

    def is_bode(self):
        return self.isBode

    def get_y_axis_values(self, name, step):
        return self.reader.data[self.from_nice_to_data_name(name, step)]

    def add_function_to_list(self, name: str):
        name = name.replace(' ','',1)
        splitted = name.split(',')
        for step in range(1, int(self.reader.get_mc_steps())):

            self.graphFunctionList.append(GraphFunction(splitted[0] + '_' + str(step),
                                                        GraphValues(self.get_x_axis_values(),
                                                                    self.get_y_axis_values(name, step)),
                                                        GraphMagnitude.Frequency.value if self.isBode else
                                                        GraphMagnitude.Time.value,
                                                        get_magnitude_from_string(splitted[1])))

    def remove_function_from_list(self, name: str):
        name = name.replace(' ', '', 1)
        splitted = name.split(',')
        for step in range(1, self.reader.get_mc_steps()):
            self.graphFunctionList.remove(GraphFunction(splitted[0] + '_' + str(step),
                                                        GraphValues(self.get_x_axis_values(), self.get_y_axis_labels()),
                                                        GraphMagnitude.Frequency.value if self.isBode else
                                                        GraphMagnitude.Time.value,
                                                        get_magnitude_from_string(splitted[1])))

    def from_nice_to_data_name(self, niceName: str, step):

        niceString = str(niceName)
        splitted = niceString.split(',')
        yAxisLabelPos = self.labels[splitted[0]]   # this should return something like y_axis_0
        if not self.reader.isBode():
            return yAxisLabelPos + '_step' + str(step)
        else:
            if splitted[1] == GraphMagnitude.Decibel.value:
                return 'abs_' + yAxisLabelPos + '_step' + str(step)
            if splitted[1] == GraphMagnitude.Phase.value:
                return 'pha_' + yAxisLabelPos + '_step' + str(step)

    def get_graph_functions(self) -> list:
        return self.graphFunctionList

