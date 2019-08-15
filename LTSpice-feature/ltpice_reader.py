



import numpy as np
import matplotlib.pyplot as plt


class LTSpiceReader:
    data = dict()
    filename = ''
    mc_step_counter = 1
    total_steps = 0
    y_axis_var_count = 0

    def __init__(self, filename):

        self.filename = filename

    def _read_y_axis_vars(self, opened_file):
        pointer = 0
        y_axis_name_counter = 0
        y_axis_name_temp = ''
        self.data["y_axis_0"] = ''
        while opened_file[0][pointer] != '\t':  # i don't need to know x axis name i already know its frequency
            pointer += 1
        pointer += 1

        while opened_file[0][pointer] != '\r' and opened_file[0][pointer] != '\n':  # get the y-axis name and
            # store it in the dictionary

            if opened_file[0][pointer] == '\t':

                self.data["y_axis_" + str(y_axis_name_counter)] = y_axis_name_temp
                y_axis_name_temp = ''
                pointer += 1
                y_axis_name_counter += 1
                self.data["y_axis_" + str(y_axis_name_counter)] = ''

            else:

                y_axis_name_temp += opened_file[0][pointer]
                pointer += 1

        self.data["y_axis_" + str(y_axis_name_counter)] = y_axis_name_temp
        y_axis_name_counter += 1
        self.y_axis_var_count = y_axis_name_counter

    @staticmethod
    def _not_num(content):
        if content == "0":
            return 0
        if content == "1":
            return 0
        if content == "2":
            return 0
        if content == "3":
            return 0
        if content == "4":
            return 0
        if content == "5":
            return 0
        if content == "6":
            return 0
        if content == "7":
            return 0
        if content == "8":
            return 0
        if content == "9":
            return 0
        if content == "-":
            return 0
        return 1


class LTSpiceBodeReader(LTSpiceReader):
    """
    kind of self-explanatory
    """
    is_mc = False

    def __init__(self, filename, is_mc):
        LTSpiceReader.__init__(self, filename)
        self.is_mc = is_mc

    def __get_values(self):
        """
        saves all the data from the file in self.data
        """
        file = open(self.filename, 'r')
        opened_file = file.readlines()
        super(LTSpiceBodeReader, self)._read_y_axis_vars(opened_file)

        if self.is_mc:

            self.__read_mc_file(opened_file, 1, len(opened_file))

        else:

            self.__read_non_mc_file(opened_file, 1, len(opened_file))

    def get_data(self):
        """
        :return: a dictionary with all the data acquired from the spice file
        """

        self. __get_values()
        return self. data

    def __read_mc_file(self, opened_file, start, end):
        """
        Reads a LTSpice Monte-Carlo .txt simulation file dividing it into mini non-MC chunks.
        Then sends them to the MC reading method
        """
        pnt = 0
        temp_steps = ''
        while opened_file[start][pnt] != "/":   # looking for '/' which indicates where's the number of
                                                # steps in the first line
            pnt += 1
        pnt += 1
        while opened_file[start][pnt] != ")":   # saves it
            temp_steps += opened_file[start][pnt]
            pnt += 1
        self.total_steps = str(temp_steps)
        mc_step_start = start + 1               # the relevant simulation info starts after the MC step counting line

        for line in range(2, end):
            if opened_file[line][0] == 'S' or line == (len(opened_file) - 1):     # 'S' (as in "Step...")
                                                                            # indicates the end of a step in the sim
                mc_step_end = line
                self.__read_non_mc_file(opened_file, mc_step_start, mc_step_end)
                mc_step_start = mc_step_end + 1
                self.mc_step_counter += 1

    def __read_non_mc_file(self, opened_file, start, end):
        """
        Reads a LTSpice  .txt simulation file dividing it into mini non-MC chunks.
        Then sends them to the MC reading method
        :param opened_file: recieved after executing file.readlines
        :param start: starting line of bode data
        :param end: last line of data

        """

        if self.mc_step_counter == 1:  # only save freq if it's the first step, Spice always uses same values
            self. data["f"] = []

        for i in range(start, end):
            pnt = 0
            c1 = ""

            while opened_file[i][pnt] != '\t':
                c1 += opened_file[i][pnt]
                pnt += 1
            c1 = float(c1)

            if self.mc_step_counter == 1:
                self.data["f"].append(c1)

            for j in range(0, self.y_axis_var_count):
                c2 = ""
                c3 = ""

                if i == start:
                    self.data["abs" + '_' + "y_axis_" + str(j) + '_step' + str(self. mc_step_counter)] = []
                    self.data["pha" + '_' + "y_axis_" + str(j) + '_step' + str(self. mc_step_counter)] = []

                while self. __not_num(opened_file[i][pnt]):
                    pnt += 1

                while opened_file[i][pnt] != 'd':
                    c2 += opened_file[i][pnt]
                    pnt += 1
                pnt += 1

                while self. __not_num(opened_file[i][pnt]):
                    pnt += 1

                while opened_file[i][pnt] != '°':
                    c3 += opened_file[i][pnt]
                    pnt += 1

                c2 = float(c2)
                c3 = float(c3)

                self. data["abs" + '_' + "y_axis_" + str(j) + '_step' + str(self. mc_step_counter)].append(c2)
                self. data["pha" + '_' + "y_axis_" + str(j) + '_step' + str(self. mc_step_counter)].append(c3)

    def __not_num(self, content):

        is_num = super(LTSpiceBodeReader, self)._not_num(content)
        return is_num



# class LTSpiceFunctionReader:
# aca empieza lo de ari nowik

"""
def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1

def read_bode_file_spice(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    data = dict()

    data["f"] = []
    data["abs"] = []
    data["pha"] = []
    #print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != 'd':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '°':
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["f"].append(c1)
        data["abs"].append(c2)
        data["pha"].append(c3)

    return data
    """
# data = read_file_spice("input/EJ_1_simulaciones.txt")
# print(data["abs"])
