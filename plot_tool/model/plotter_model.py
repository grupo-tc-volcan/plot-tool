# python native modules

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QMessageBox

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
    graphModelAdded = pyqtSignal(GraphFunctionModel)
    graphModelRemoved = pyqtSignal(GraphFunctionModel)
    axesModelAdded = pyqtSignal(GraphAxesModel)
    axesModelRemoved = pyqtSignal(GraphAxesModel)
    propertyChanged = pyqtSignal()
    hasChanged = pyqtSignal()

    def __init__(self, graphPlotter: GraphPlotter, *args, **kwargs):
        super(GraphPlotterModel, self).__init__()

        # Data model reference
        self.plotter = graphPlotter

        # A GraphPlotterModel has the following models as components
        self.graphModels = []
        self.axesModels = []

        self.addGraphModels()
        self.addAxesModels()

        # Property Members
        self._name = kwargs["name"] if "name" in kwargs.keys() else "Name"
        self._xLabel = kwargs["xLabel"] if "xLabel" in kwargs.keys() else self.plotter.x_magnitude.value
        self._xScale = kwargs["xScale"] if "xScale" in kwargs.keys() else Scale.Linear
        self._xMinimum = kwargs["xMinimum"] if "xMinimum" in kwargs.keys() else 0.0
        self._xMaximum = kwargs["xMaximum"] if "xMaximum" in kwargs.keys() else 10.0

        self._faceColor = kwargs["faceColor"] if "faceColor" in kwargs.keys() else QColor(255, 255, 255, 255)
        self._edgeColor = kwargs["edgeColor"] if "edgeColor" in kwargs.keys() else QColor(0, 0, 0, 255)
        self._legendFaceColor = kwargs["legendFaceColor"] if "legendFaceColor" in kwargs.keys() else QColor(255, 255, 255, 255)
        self._legendEdgeColor = kwargs["legendEdgeColor"] if "legendEdgeColor" in kwargs.keys() else QColor(0, 0, 0, 255)

    def addGraph(self, graph: GraphFunction) -> bool:
        """
        Adds a new graph to the Plotter Model and creates a model
        of it. It returns False if failed.

        :param graph: GraphFunction being added to the Plotter.
        :return: Returns whether it could or not add the graph.
        """
        if self.plotter.add_graph(graph):
            # General adding methods
            self.addGraphModels()
            self.addAxesModels()

            # Some algorithms to improve visualization
            self.adjustSizeOfXAxis()
            self.adjustSizeOfYAxis()

            return True
        else:
            return False

    def addGraphModels(self):
        """ Updates the graph models needed according to the data source """
        for graph in self.plotter.graphs:
            model = GraphFunctionModel(graph, self)
            if model not in self.graphModels:
                self.graphModels.append(model)
                self.graphModelAdded.emit(model)
                self.hasChanged.emit()

    def addAxesModels(self):
        """ Updates the current status of axes models. """
        for y_magnitude in self.plotter.y_magnitudes:
            model = GraphAxesModel(
                self.plotter.x_magnitude,
                y_magnitude,
                self
            )
            if model not in self.axesModels:
                self.axesModels.append(model)

                model.xScale = self.xScale
                model.xLabel = self.xLabel
                model.xMinimum = self.xMinimum
                model.xMaximum = self.xMaximum

                self.axesModelAdded.emit(model)
                self.hasChanged.emit()

    def removeGraph(self, graph: GraphFunction) -> bool:
        """
        Removes the given graph from the plotter. Returns False if it
        failed.

        :param graph:  GraphFunction being removed from the Plotter.
        :return: Returns whether it could or not remove the graph.
        """
        if self.plotter.remove_graph(graph):
            self.removeGraphModel(GraphFunctionModel(graph, self))
            self.removeAxesModels()
            return True
        else:
            return False

    def removeGraphModel(self, model: GraphFunctionModel):
        """ Removes the given GraphFunctionModel """
        self.graphModels.remove(model)
        self.graphModelRemoved.emit(model)
        self.hasChanged.emit()

    def removeAxesModels(self):
        """ Removes all axes that are not being used. """
        removeModels = [axesModel for axesModel in self.axesModels if axesModel.yMagnitude not in self.plotter.y_magnitudes]
        for removeModel in removeModels:
            self.axesModels.remove(removeModel)
            self.axesModelRemoved.emit(removeModel)
            self.hasChanged.emit()

    def updateAxesProperties(self):
        """ Updates the current value of axes properties. """
        for axesModel in self.axesModels:
            axesModel.xScale = self.xScale
            axesModel.xLabel = self.xLabel
            axesModel.xMinimum = self.xMinimum
            axesModel.xMaximum = self.xMaximum

    def notifyPropertyChange(self):
        """ Notifying that a property has changed and propagating
        the change throughout the internal axe models. """
        self.updateAxesProperties()
        self.propertyChanged.emit()
        self.hasChanged.emit()

    # Algorithms used to improve the user experience
    # when handling several GraphFunctions inside the Plotter
    def adjustSizeOfXAxis(self):
        """ Gets the x minimum and maximum values needed to produce a stretch
        view of the graph. """
        xMinimum = xMaximum = None
        for graphModel in self.graphModels:
            for x in graphModel.graph.values.x:
                if xMinimum is None and xMaximum is None:
                    xMinimum = xMaximum = x
                    continue

                if x < xMinimum:
                    xMinimum = x
                elif x > xMaximum:
                    xMaximum = x

        self.xMinimum = xMinimum
        self.xMaximum = xMaximum

    def adjustSizeOfYAxis(self):
        """ It's more complicated, for each possible y magnitude we should find the
        minimum and maximum value needed to represent the graph, then the corresponding
        axe should have that settings. """
        for axesModel in self.axesModels:

            # Each axes model has its corresponding values
            yMinimum = yMaximum = None

            for graphModel in self.graphModels:
                if graphModel.graph.y_magnitude == axesModel.yMagnitude:
                    for y in graphModel.graph.values.y:
                        if yMaximum is None and yMinimum is None:
                            yMaximum = yMinimum = y
                            continue

                        if y > yMaximum:
                            yMaximum = y
                        elif y < yMinimum:
                            yMinimum = y

            # If values needed were found... updates them
            if yMinimum is not None and yMaximum is not None:
                axesModel.yMinimum = yMinimum
                axesModel.yMaximum = yMaximum

    # GraphPlotterModel's properties
    @pyqtProperty(QColor)
    def faceColor(self):
        return self._faceColor

    @faceColor.setter
    def faceColor(self, value: QColor):
        self._faceColor = value
        self.notifyPropertyChange()

    @pyqtProperty(QColor)
    def edgeColor(self):
        return self._edgeColor

    @edgeColor.setter
    def edgeColor(self, value: QColor):
        self._edgeColor = value
        self.notifyPropertyChange()

    @pyqtProperty(QColor)
    def legendFaceColor(self):
        return self._legendFaceColor

    @legendFaceColor.setter
    def legendFaceColor(self, value: QColor):
        self._legendFaceColor = value
        self.notifyPropertyChange()

    @pyqtProperty(QColor)
    def legendEdgeColor(self):
        return self._legendEdgeColor

    @legendEdgeColor.setter
    def legendEdgeColor(self, value: QColor):
        self._legendEdgeColor = value
        self.notifyPropertyChange()

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
