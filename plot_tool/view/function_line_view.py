# python native modules

# third-party modules
from matplotlib.lines import Line2D

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.model.function_model import GraphFunctionModel


# noinspection PyPropertyAccess
class GraphFunctionLineView(Line2D):
    """ GraphFunction Line View """

    def __init__(self, model: GraphFunctionModel, parent=None, *args, **kwargs):
        super(GraphFunctionLineView, self).__init__(
            model.graph.values.x,
            model.graph.values.y,
            visible=model.isVisible,
            label=model.name,
            color=self.convertColor(model.color),
            *args,
            **kwargs
        )

        # Reference Members
        self.parent = parent
        self.model = model

        # Connecting slots and signals
        self.model.hasChanged.connect(self.onHasChanged)

    @staticmethod
    def convertColor(color: QColor):
        return [
            color.red() / 255,
            color.green() / 255,
            color.blue() / 255
        ]

    def onHasChanged(self):
        self.set_visible(self.model.isVisible)
        self.set_color(self.convertColor(self.model.color))
        self.set_label(self.model.name)
