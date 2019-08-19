class LTSpiceReader:
    """
    Base class for bode reader and time based reader
    """

    def __init__(self, filename):
        self.data = dict()
        self.opened_file = ''
        self.mc_step_counter = 1
        self.total_steps = 1
        self.y_axis_var_count = 0
        file = open(filename, 'r')
        self. opened_file = file.readlines()

    def _read_y_axis_vars(self):
        pointer = 0
        y_axis_name_counter = 0
        axis_name_temp = ''
        self.data['y_axis_0'] = ''
        self.data['x_axis_label'] = ''
        while self.opened_file[0][pointer] != '\t':  # save x-axis name(always the first column)
            axis_name_temp += self.opened_file[0][pointer]
            pointer += 1
        self.data['x_axis_label'] = axis_name_temp
        axis_name_temp = ''
        pointer += 1

        while self.opened_file[0][pointer] != '\r' and self.opened_file[0][pointer] != '\n':  # get the y-axis name and
            # store it in the dictionary

            if self.opened_file[0][pointer] == '\t':

                self.data['y_axis_' + str(y_axis_name_counter)] = axis_name_temp
                axis_name_temp = ''
                pointer += 1
                y_axis_name_counter += 1
                self.data['y_axis_' + str(y_axis_name_counter)] = ''

            else:

                axis_name_temp += self.opened_file[0][pointer]
                pointer += 1

        self.data['y_axis_' + str(y_axis_name_counter)] = axis_name_temp
        y_axis_name_counter += 1
        self.y_axis_var_count = y_axis_name_counter

    def get_data(self):
        """
        :return: a dictionary with all the data acquired from the spice file
        """

        self._read_y_axis_vars()
        return self.data

    @staticmethod
    def _not_num(content):
        if content == '0':
            return 0
        if content == '1':
            return 0
        if content == '2':
            return 0
        if content == '3':
            return 0
        if content == '4':
            return 0
        if content == '5':
            return 0
        if content == '6':
            return 0
        if content == '7':
            return 0
        if content == '8':
            return 0
        if content == '9':
            return 0
        if content == '-':
            return 0
        return 1

    def isBode(self):
        self._read_y_axis_vars()
        if self.data['x_axis_label'] == 'time':  # si la variable del eje x es tiempo entonces no es un bode
            return False
        else:                              # por ahora solamente se pueden obtener graficos en f(t) y f(frec)
            return True

    def get_y_axis_var_count(self):
        return self.y_axis_var_count

    def get_mc_steps(self):
        return self.total_steps


"""
We took a lot of the code used here from
https://github.com/newtonis/EjemplosElectrotecnia/blob/master/ejemplo6_leer_spice/read_spice.py
but modified it in order to read different kinds of files. Anyway thanks to newtonis(Ariel Nowik)
for letting us use his code  :)
WE KNOW IT'S NOT MADE IN A PYTHON FRIENDLY WAY (A LOT OF WHILE LOOPS)  :(
TODO:  REWRITE THIS IN A MORE "READABLE/ NOT SO C++" WAY
"""






