# python native modules

# third-party modules
from matplotlib.axes import Axes

from matplotlib.scale import LinearScale
from matplotlib.scale import LogScale

# plot-tool modules
from plot_tool.model.axe_model import GraphAxesModel
from plot_tool.model.axe_model import Scale


# noinspection PyPropertyAccess,PyTypeChecker
class GraphAxesView(Axes):
    """ GraphAxesModel View """

    def __init__(self, model: GraphAxesModel, parent, rect, *args, **kwargs):
        super(GraphAxesView, self).__init__(
            parent,
            rect,
            xscale=self.convertScale(model.xScale),
            yscale=self.convertScale(model.yScale),
            xlabel=model.xLabel,
            ylabel=model.yLabel,
            xlim=(model.xMinimum, model.xMaximum),
            ylim=(model.yMinimum, model.yMaximum),
            *args, **kwargs)

        # Data model reference
        self.model = model
        self.parent = parent

        # Signal and slot connections
        self.model.hasChanged.connect(self.onHasChanged)

    def onHasChanged(self):
        # Scale update
        self.set_xscale(self.convertScale(self.model.xScale))
        self.set_xscale(self.convertScale(self.model.yScale))

        # Axis Limits
        self.set_xlim(self.model.xMinimum, self.model.xMaximum)
        self.set_ylim(self.model.yMinimum, self.model.yMaximum)

        # Labels
        self.set_xlabel(self.model.xLabel)
        self.set_ylabel(self.model.yLabel)

    @staticmethod
    def convertScale(modelValue: Scale):
        if modelValue == Scale.Linear:
            return LinearScale.name
        elif modelValue == Scale.Log:
            return LogScale.name
