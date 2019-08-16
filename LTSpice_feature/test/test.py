from ltpice_reader import *

lts = LTSpiceBodeReader('21.txt', True)

data = lts.get_data()

print(data['abs_y_axis_0_step1'])
print(data['f'])
