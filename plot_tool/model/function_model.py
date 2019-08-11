# python native modules

# third-party modules
from PyQt5.QtCore import QObject

# plot-tool modules
from plot_tool.data.function import GraphFunction


class GraphFunctionModel(QObject):
    """ GraphFunction Model
    """

    def __init__(self, graph_function: GraphFunction, *args, **kwargs):
        super(GraphFunctionModel, self).__init__(*args, **kwargs)

        # Data model reference
        self.graph = graph_function

    def __eq__(self, other):
        return self.graph == other.graph
