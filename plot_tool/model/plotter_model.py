# python native modules

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

# plot-tool modules
from plot_tool.data.plotter import GraphPlotter
from plot_tool.data.function import GraphFunction

from plot_tool.model.axe_model import Scale

from plot_tool.model.function_model import GraphFunctionModel


class GraphPlotterModel(QObject):
    """ GraphPlotter Model """

    # GraphPlotterModel's signals
    hasChanged = pyqtSignal()

    def __init__(self, graphPlotter: GraphPlotter, *args, **kwargs):
        super(GraphPlotterModel, self).__init__(*args, **kwargs)

        # Data model reference
        self.plotter = graphPlotter

        # In the same way a GraphPlotter contains GraphFunctions, the
        # GraphPlotterModel contains the GraphFunctionModels of each data source
        self.graphModels = [GraphFunctionModel(graph, self) for graph in self.plotter.graphs]

        # Property Members
        self._name = None
        self._xLabel = None
        self._xScale = None
        self._xMinimum = None
        self._xMaximum = None

    def add_graph(self, graph: GraphFunction) -> bool:
        """
        Adds a new graph to the Plotter Model and creates a model
        of it. It returns False if failed.

        :param graph: GraphFunction being added to the Plotter.
        :return: Returns whether it could or not add the graph.
        """
        if self.plotter.add_graph(graph):
            self.graph_models.append(GraphFunctionModel(graph, self))
            self.notifyChange()
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
            self.graph_models.remove(GraphFunctionModel(graph, self))
            self.notifyChange()
            return True
        else:
            return False

    def notifyChange(self):
        self.hasChanged.emit()

    @pyqtProperty(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.notifyChange()

    @pyqtProperty(str)
    def xLabel(self):
        return self._xLabel

    @xLabel.setter
    def xLabel(self, value: str):
        self._xLabel = value
        self.notifyChange()

    @pyqtProperty(Scale)
    def xScale(self):
        return self._xScale

    @xScale.setter
    def xScale(self, value: Scale):
        self._xScale = value
        self.notifyChange()

    @pyqtProperty(float)
    def xMinimum(self):
        return self._xMinimum

    @xMinimum.setter
    def xMinimum(self, value: float):
        self._xMinimum = value
        self.notifyChange()

    @pyqtProperty(float)
    def xMaximum(self):
        return self._xMaximum

    @xMaximum.setter
    def xMaximum(self, value: float):
        self._xMaximum = value
        self.notifyChange()
