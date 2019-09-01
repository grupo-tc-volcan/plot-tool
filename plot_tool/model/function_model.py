# python native modules
from enum import Enum
from random import randint

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.data.function import GraphFunction


class Styles(Enum):
    """ Supported line styles """
    Solid = "Solid"
    Dashed = "Dashed"


class Markers(Enum):
    """ Supported line markers """
    Default = "Default"
    Point = "Point"


class GraphFunctionModel(QObject):
    """ GraphFunction Model """

    # GraphFunctionModel's signals
    hasChanged = pyqtSignal()

    def __init__(self, graph_function: GraphFunction, parent=None, *args, **kwargs):
        super(GraphFunctionModel, self).__init__()

        # Data model reference
        self.graph = graph_function
        self.parent = parent

        # Property members
        self._isVisible = True
        self._hasLabel = True

        self._marker = Markers.Default.value
        self._style = Styles.Solid.value

        self._name = self.graph.name
        self._color = QColor(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

    def __eq__(self, other):
        return self.graph == other.graph

    def notifyChange(self):
        """ A change on the model's properties has been done
        and an event is triggered.
        """
        self.hasChanged.emit()

    # GraphFunctionModel's properties
    @pyqtProperty(bool)
    def hasLabel(self):
        return self._hasLabel

    @hasLabel.setter
    def hasLabel(self, value: bool):
        self._hasLabel = value
        self.notifyChange()

    @pyqtProperty(str)
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value: str):
        self._marker = value
        self.notifyChange()

    @pyqtProperty(str)
    def style(self):
        return self._style

    @style.setter
    def style(self, value: str):
        self._style = value
        self.notifyChange()

    @pyqtProperty(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.graph.name = value
        self.notifyChange()

    @pyqtProperty(bool)
    def isVisible(self):
        return self._isVisible

    @isVisible.setter
    def isVisible(self, value: bool):
        self._isVisible = value
        self.notifyChange()

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, value: QColor):
        self._color = value
        self.notifyChange()
