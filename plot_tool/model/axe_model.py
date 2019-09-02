# python native modules
from enum import Enum

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude


"""
Enum classes are used only as declaring statements. Any variable in the program shall
be set using the string value of the enum. So every time we set a scale value,
shall be using :
    variable = Scale.Linear.value

And comparing:
    if variable == Scale.Linear.value
"""


class Scale(Enum):
    Linear = "Linear"
    Log = "Log"


class Grid(Enum):
    Major = "Major"
    Minor = "Minor"
    Both = "Both"


# noinspection PyPropertyAccess
class GraphAxesModel(QObject):
    """ GraphAxes Model
    This model class is used to represent a GraphPlotterModel component
    used to describe where different graphs are being drawn.
    """

    # GraphAxeModel's Signal
    hasChanged = pyqtSignal()

    def __init__(self,
                 xMagnitude: GraphMagnitude,
                 yMagnitude: GraphMagnitude,
                 parent=None,
                 *args, **kwargs):
        super(GraphAxesModel, self).__init__()

        # Data model references
        self.parent = parent

        # Property members
        self._xMagnitude = xMagnitude
        self._xScale = kwargs["xScale"] if "xScale" in kwargs.keys() else Scale.Linear.value
        self._xLabel = kwargs["xLabel"] if "xLabel" in kwargs.keys() else xMagnitude.value
        self._xMinimum = kwargs["xMinimum"] if "xMinimum" in kwargs.keys() else 0.0
        self._xMaximum = kwargs["xMaximum"] if "xMaximum" in kwargs.keys() else 10.0

        self._yMagnitude = yMagnitude
        self._yScale = kwargs["yScale"] if "yScale" in kwargs.keys() else Scale.Linear.value
        self._yLabel = kwargs["yLabel"] if "yLabel" in kwargs.keys() else yMagnitude.value
        self._yMinimum = kwargs["yMinimum"] if "yMinimum" in kwargs.keys() else 0.0
        self._yMaximum = kwargs["yMaximum"] if "yMaximum" in kwargs.keys() else 10.0

        self._faceColor = kwargs["faceColor"] if "faceColor" in kwargs.keys() else QColor(255, 255, 255)

        self._gridEnable = False
        self._gridOption = Grid.Major.value

    def __eq__(self, other):
        return self.yMagnitude == other.yMagnitude

    def notifyChange(self):
        self.hasChanged.emit()

    @pyqtProperty(bool)
    def gridEnable(self):
        return self._gridEnable

    @gridEnable.setter
    def gridEnable(self, value: bool):
        self._gridEnable = value
        self.notifyChange()

    @pyqtProperty(Grid)
    def gridOption(self):
        return self._gridOption

    @gridOption.setter
    def gridOption(self, value: Grid):
        self._gridOption = value
        self.notifyChange()

    @pyqtProperty(QColor)
    def faceColor(self):
        return self._faceColor

    @faceColor.setter
    def faceColor(self, value: QColor):
        self._faceColor = value
        self.notifyChange()

    @pyqtProperty(GraphMagnitude)
    def yMagnitude(self):
        return self._yMagnitude

    @yMagnitude.setter
    def yMagnitude(self, value: GraphMagnitude):
        self._yMagnitude = value
        self.notifyChange()

    @pyqtProperty(GraphMagnitude)
    def xMagnitude(self):
        return self._xMagnitude

    @xMagnitude.setter
    def xMagnitude(self, value: GraphMagnitude):
        self._xMagnitude = value
        self.notifyChange()

    @pyqtProperty(str)
    def xLabel(self):
        return self._xLabel

    @xLabel.setter
    def xLabel(self, value: str):
        self._xLabel = value
        self.notifyChange()

    @pyqtProperty(str)
    def yLabel(self):
        return self._yLabel

    @yLabel.setter
    def yLabel(self, value: str):
        self._yLabel = value
        self.notifyChange()

    @pyqtProperty(Scale)
    def yScale(self):
        return self._yScale

    @yScale.setter
    def yScale(self, value: Scale):
        if value == "":
            pass
        self._yScale = value
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

    @pyqtProperty(float)
    def yMinimum(self):
        return self._yMinimum

    @yMinimum.setter
    def yMinimum(self, value: float):
        self._yMinimum = value
        self.notifyChange()

    @pyqtProperty(float)
    def yMaximum(self):
        return self._yMaximum

    @yMaximum.setter
    def yMaximum(self, value: float):
        self._yMaximum = value
        self.notifyChange()
