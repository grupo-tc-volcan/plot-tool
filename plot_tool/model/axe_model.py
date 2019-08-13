# python native modules
from enum import Enum

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude


class Scale(Enum):
    Linear = "Linear"
    Semilog = "Semilog"
    Log = "Log"


class GraphAxeModel(QObject):
    """ GraphAxe Model """

    # GraphAxeModel's Signal
    hasChanged = pyqtSignal()

    def __init__(self,
                 xMagnitude: GraphMagnitude,
                 yMagnitude: GraphMagnitude,
                 parent=None,
                 *args, **kwargs):
        super(GraphAxeModel, self).__init__(*args, **kwargs)

        # Data model references
        self.parent = parent

        # Property members
        self._xLabel = "X Label"
        self._yLabel = "Y Label"
        self._xScale = Scale.Linear

        self._xMinimum = None
        self._xMaximum = None

        self._yMinimum = None
        self._yMaximum = None

        self._yMagnitude = yMagnitude
        self._xMagnitude = xMagnitude

    def notifyChange(self):
        self.hasChanged.emit()

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
