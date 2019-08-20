"LTSpice_reader modules"
from utilities.ltspice.ltpice_reader import LTSpiceReader


class LTSpiceTimeGraphReader(LTSpiceReader):
    """
    Reads data from Spice generated .txt simulation file
    stores it in a dictionary retrievable using get_data method
    receives a filepath and a bool that indicates whether the simulation was made using Montecarlo or not
    """
    is_mc = False

    def __init__(self, filename, is_mc):
        LTSpiceReader.__init__(self, filename)
        self.is_mc = is_mc

    def __get_values(self):
        """
        saves all the data from the file in self.data
        """
        super(LTSpiceTimeGraphReader, self)._read_y_axis_vars()

        if self.is_mc:

            self.__read_mc_file(1, len(self. opened_file))

        else:

            self.__read_non_mc_file(1, len(self. opened_file))

    def __read_mc_file(self, start, end):
        """
        Reads a LTSpice Monte-Carlo .txt simulation file dividing it into mini non-MC chunks.
        Then sends them to the MC reading method
        """
        pnt = 0
        temp_steps = ''
        while self. opened_file[start][pnt] != '/':  # looking for '/' which indicates where's the number of
            # steps in the first line
            pnt += 1
        pnt += 1
        while self. opened_file[start][pnt] != ')':  # saves it
            temp_steps += self. opened_file[start][pnt]
            pnt += 1
        self.total_steps = str(temp_steps)
        mc_step_start = start + 1  # the relevant simulation info starts after the MC step counting line

        for line in range(2, end):
            if self. opened_file[line][0] == 'S' or line == (len(self. opened_file) - 1):   # 'S' (as in 'Step...')
                                                                                # indicates the end of a step in the sim
                mc_step_end = line
                self.__read_non_mc_file(mc_step_start, mc_step_end)
                mc_step_start = mc_step_end + 1
                self.mc_step_counter += 1

    def __read_non_mc_file(self, start, end):
        """
        Reads a LTSpice  .txt simulation file dividing it into mini non-MC chunks.
        Then sends them to the MC reading method

        :param start: starting line of data
        :param end: last line of data

        """

        if self.mc_step_counter == 1:  # only save x_axis if it's the first step, Spice always uses same values
            self.data['x_axis'] = []

        for i in range(start, end):  # This is O(scary), but seems quick enough in practice.
            pnt = 0
            c1 = ''

            while self. opened_file[i][pnt] != '\t':   # saving the x_axis value for this row
                c1 += self. opened_file[i][pnt]
                pnt += 1
            c1 = float(c1)

            if self.mc_step_counter == 1:
                self.data['x_axis'].append(c1)

            for j in range(0, self.y_axis_var_count):    # saving y_axis values for every variable in this row
                c2 = ''

                if i == start:
                    self.data['y_axis_' + str(j) + '_step' + str(self.mc_step_counter)] = []

                while self.__not_num(self. opened_file[i][pnt]):
                    pnt += 1

                while self. opened_file[i][pnt] != '\t' and self. opened_file[i][pnt] != '\n':
                    c2 += self. opened_file[i][pnt]
                    pnt += 1

                c2 = float(c2)

                self.data['y_axis_' + str(j) + '_step' + str(self.mc_step_counter)].append(c2)

    def __not_num(self, content):

        is_num = super(LTSpiceTimeGraphReader, self)._not_num(content)
        return is_num

    def get_data(self):
        """
        :return: a dictionary with all the data acquired from the spice file
        """

        self.__get_values()
        return self.data

"""
We took a lot of the code used here from
https://github.com/newtonis/EjemplosElectrotecnia/blob/master/ejemplo6_leer_spice/read_spice.py
but modified it in order to read different kinds of files. Anyway thanks to newtonis(Ariel Nowik)
for letting us use his code  :)
WE KNOW IT'S NOT MADE IN A PYTHON FRIENDLY WAY (A LOT OF WHILE LOOPS)  :(
TODO:  REWRITE THIS IN A MORE "READABLE/ NOT SO C++" WAY
"""