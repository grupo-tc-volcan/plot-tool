# python native modules

# third-party modules
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.scale import LinearScale
from matplotlib.scale import LogScale

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.model.axe_model import GraphAxesModel
from plot_tool.model.axe_model import Scale

from plot_tool.view.base.view import View


# noinspection PyPropertyAccess,PyTypeChecker
class GraphAxesView(Axes, View):
    """ GraphAxesModel View """

    def __init__(self, model: GraphAxesModel, figure: Figure, canvas: FigureCanvasBase, rect, *args, **kwargs):
        Axes.__init__(
            self,
            figure,
            rect,
            xscale=self.convertScale(model.xScale),
            yscale=self.convertScale(model.yScale),
            xlabel=model.xLabel,
            ylabel=model.yLabel,
            xlim=(model.xMinimum, model.xMaximum),
            ylim=(model.yMinimum, model.yMaximum),
            facecolor=self.convertColor(model.faceColor),
            *args, **kwargs)
        View.__init__(self, canvas)

        # Data model reference
        self.model = model

        # Signal and slot connections
        self.model.hasChanged.connect(self.onHasChanged)

    def onHasChanged(self):
        # Scale update
        self.set_xscale(self.convertScale(self.model.xScale))
        self.set_yscale(self.convertScale(self.model.yScale))

        # Axis Limits
        self.set_xlim(self.model.xMinimum, self.model.xMaximum)
        self.set_ylim(self.model.yMinimum, self.model.yMaximum)

        # Labels
        self.set_xlabel(self.model.xLabel)
        self.set_ylabel(self.model.yLabel)

        # We first clear all existing grids, then...
        self.grid(b=False, which="major", axis="both")
        self.grid(b=False, which="minor", axis="both")
        self.grid(b=False, which="both", axis="both")

        if self.model.gridOption.lower() == "minor" or self.model.gridOption.lower() == "both":
            self.minorticks_on()

        if self.model.gridEnable:
            if self.model.gridOption.lower() == "minor" or self.model.gridOption.lower() == "both":
                self.grid(
                    b=True,
                    linestyle=":",
                    which="minor",
                    axis='both')
            if self.model.gridOption.lower() == "major" or self.model.gridOption.lower() == "both":
                self.grid(
                    b=True,
                    linestyle="-",
                    which="major",
                    axis='both')

        # Coloring...
        self.set_facecolor(self.convertColor(self.model.faceColor))

        self.canvas.draw_idle()

    @staticmethod
    def convertScale(modelValue: Scale):
        if modelValue == Scale.Linear:
            return LinearScale.name
        elif modelValue == Scale.Log:
            return LogScale.name

    @staticmethod
    def convertColor(value: QColor):
        return (
            value.red() / 255,
            value.green() / 255,
            value.blue() / 255,
            value.alpha() / 255
        )
