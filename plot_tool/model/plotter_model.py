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
from plot_tool.model.axe_model import GraphAxesModel


# noinspection PyPropertyAccess
class GraphPlotterModel(QObject):
    """ GraphPlotter Model """

    # GraphPlotterModel's signals
    graphModelChanged = pyqtSignal()
    axeModelChanged = pyqtSignal()
    propertyChanged = pyqtSignal()

    def __init__(self, graphPlotter: GraphPlotter, *args, **kwargs):
        super(GraphPlotterModel, self).__init__(*args, **kwargs)

        # Data model reference
        self.plotter = graphPlotter

        # A GraphPlotterModel has the following models as components
        self.graphModels = [GraphFunctionModel(graph, self) for graph in self.plotter.graphs]
        self.axeModels = []

        # Property Members
        self._name = kwargs["name"] if "name" in kwargs.keys() else "Name"
        self._xLabel = kwargs["xLabel"] if "xLabel" in kwargs.keys() else "X Label"
        self._xScale = kwargs["xScale"] if "xScale" in kwargs.keys() else Scale.Linear
        self._xMinimum = kwargs["xMinimum"] if "xMinimum" in kwargs.keys() else 0.0
        self._xMaximum = kwargs["xMaximum"] if "xMaximum" in kwargs.keys() else 10.0

    def addGraph(self, graph: GraphFunction) -> bool:
        """
        Adds a new graph to the Plotter Model and creates a model
        of it. It returns False if failed.

        :param graph: GraphFunction being added to the Plotter.
        :return: Returns whether it could or not add the graph.
        """
        if self.plotter.add_graph(graph):
            # GraphFunction model change
            self.graph_models.append(GraphFunctionModel(graph, self))
            self.graphModelChanged.emit()

            # Updating axe models
            self.updateAxeModels()
            self.updateAxeProperties()

            return True
        else:
            return False

    def removeGraph(self, graph: GraphFunction) -> bool:
        """
        Removes the given graph from the plotter. Returns False if it
        failed.

        :param graph:  GraphFunction being removed from the Plotter.
        :return: Returns whether it could or not remove the graph.
        """
        if self.plotter.remove_graph(graph):
            # GraphFunction model change
            self.graph_models.remove(GraphFunctionModel(graph, self))
            self.graphModelChanged.emit()

            # Updating axe models
            self.updateAxeModels()
            self.updateAxeProperties()

            return True
        else:
            return False

    def updateAxeProperties(self):
        """ Updates the current value of axes properties. """
        for axeModel in self.axeModels:
            axeModel.xScale = self.xScale
            axeModel.xLabel = self.xLabel
            axeModel.xMinimum = self.xMinimum
            axeModel.xMaximum = self.xMaximum

    def updateAxeModels(self):
        """ Updates the current status of axes models. """

        # Looking for new Axe Models
        for y_magnitude in self.plotter.y_magnitudes:
            for axeModel in self.axeModels:
                if axeModel.yMagnitude == y_magnitude:
                    break
            else:
                self.axeModels.append(
                    GraphAxesModel(
                        self.plotter.x_magnitude,
                        y_magnitude,
                        self
                    )
                )

        # Deleting not used Axe Models
        removeModels = []
        for axeModel in self.axeModels:
            if axeModel.yMagnitude not in self.plotter.y_magnitudes:
                removeModels.append(axeModel)
        for removeModel in removeModels:
            self.axeModels.remove(removeModel)

        # Event triggering
        self.axeModelChanged.emit()

    def notifyPropertyChange(self):
        """ Notifying that a property has changed and propagating
        the change throughout the internal axe models. """
        self.updateAxeProperties()
        self.propertyChanged.emit()

    # GraphPlotterModel's properties
    @pyqtProperty(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.notifyPropertyChange()

    @pyqtProperty(str)
    def xLabel(self):
        return self._xLabel

    @xLabel.setter
    def xLabel(self, value: str):
        self._xLabel = value
        self.notifyPropertyChange()

    @pyqtProperty(Scale)
    def xScale(self):
        return self._xScale

    @xScale.setter
    def xScale(self, value: Scale):
        self._xScale = value
        self.notifyPropertyChange()

    @pyqtProperty(float)
    def xMinimum(self):
        return self._xMinimum

    @xMinimum.setter
    def xMinimum(self, value: float):
        self._xMinimum = value
        self.notifyPropertyChange()

    @pyqtProperty(float)
    def xMaximum(self):
        return self._xMaximum

    @xMaximum.setter
    def xMaximum(self, value: float):
        self._xMaximum = value
        self.notifyPropertyChange()
