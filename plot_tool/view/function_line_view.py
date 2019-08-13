# python native modules

# third-party modules
from matplotlib.lines import Line2D

# plot-tool modules
from plot_tool.model.function_model import GraphFunctionModel


# noinspection PyPropertyAccess
class GraphFunctionLineView(Line2D):
    """ GraphFunction Line View """

    def __init__(self, model: GraphFunctionModel, parent=None, *args, **kwargs):
        super(GraphFunctionLineView, self).__init__(
            model.graph.values.x,
            model.graph.values.y,
            *args,
            **kwargs
        )

        # Reference Members
        self.parent = parent
        self.model = model

        # Connecting slots and signals
        self.model.hasChanged.connect(self.onHasChanged)

    def onHasChanged(self):
        self.set_visible(self.model.isVisible)
        self.set_color(
            [
                self.model.color.red() / 255,
                self.model.color.green() / 255,
                self.model.color.blue() / 255
            ]
        )
        self.set_label(self.model.name)
