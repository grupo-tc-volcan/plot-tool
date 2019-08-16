# python native modules
from copy import copy

# third-party modules

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction


class GraphPlotter(object):
    """ This is a container of GraphFunction objects which represents
    the same space where they are being drawn.
    """

    def __init__(self,
                 x_magnitude: GraphMagnitude,
                 name: str):
        self.name = name
        self.x_magnitude = x_magnitude
        self.y_magnitudes = []
        self.graphs = []

    def add_graph(self, graph: GraphFunction) -> bool:
        """
        Adds a graph to the GraphPlotter. Adding a new graph can fail
        when there is already another GraphFunction with the same name
        or when the GraphFunction does not have the same x magnitude.

        :param graph: GraphFunction being added to the plotter.
        :return: Boolean value true or false.
        """
        if graph.x_magnitude == self.x_magnitude:
            if graph not in self.graphs:
                if graph.y_magnitude not in self.y_magnitudes and len(self.y_magnitudes) >= 2:
                    return False

                self.graphs.append(graph)
                self.update_magnitude()
                return True
        return False

    def remove_graph(self, graph: GraphFunction) -> bool:
        """
        Removes the given GraphFunction from the plotter. Returning
        whether it could or not remove it, also if it is False, then
        it may also mean that the given GraphFunction was not found.

        :param graph: GraphFunction being removed from the plotter.
        :return:  Boolean value true or false.
        """
        if graph in self.graphs:
            self.graphs.remove(graph)
            self.update_magnitude()
            return True
        else:
            return False

    def update_magnitude(self):
        """
        Updates the GraphPlotter y magnitudes according to the
        GraphFunctions that have been added to it.
        """
        self.y_magnitudes = []
        for graph in self.graphs:
            if graph.y_magnitude not in self.y_magnitudes:
                self.y_magnitudes.append(copy(graph.y_magnitude))
