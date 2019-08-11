# python native modules

# third-party modules
from PyQt5.QtCore import QObject

# plot-tool modules
from plot_tool.data.plotter import GraphPlotter
from plot_tool.data.function import GraphFunction

from plot_tool.model.function_model import GraphFunctionModel


class GraphPlotterModel(QObject):
    """ GraphPlotter Model """

    def __init__(self, graph_plotter: GraphPlotter, *args, **kwargs):
        super(GraphPlotterModel, self).__init__(*args, **kwargs)

        # Data model reference
        self.plotter = graph_plotter

        # In the same way a GraphPlotter contains GraphFunctions, the
        # GraphPlotterModel contains the GraphFunctionModels of each data source
        self.graph_models = [GraphFunctionModel(graph) for graph in self.plotter.graphs]

    def add_graph(self, graph: GraphFunction) -> bool:
        """
        Adds a new graph to the Plotter Model and creates a model
        of it. It returns False if failed.

        :param graph: GraphFunction being added to the Plotter.
        :return: Returns whether it could or not add the graph.
        """
        if self.plotter.add_graph(graph):
            self.graph_models.append(GraphFunctionModel(graph))
            return True
        else:
            return False

    def remove_graph(self, graph: GraphFunction) -> bool:
        """
        Removes the given graph from the plotter. Returns False if it
        failed.

        :param graph:  GraphFunction being removed from the Plotter.
        :return: Returns whether it could or not remove the graph.
        """
        if self.plotter.remove_graph(graph):
            self.graph_models.remove(GraphFunctionModel(graph))
            return True
        else:
            return False
