from LTSpice_feature.reader.ltspice_time_graph_reader import *

lts = LTSpiceTimeGraphReader('2time.txt', True)

data = lts.get_data()

print(data['y_axis_0_step1'])
print(data['x_axis'])
print(data['x_axis_label'])
