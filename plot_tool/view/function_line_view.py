# python native modules

# third-party modules
from matplotlib.lines import Line2D
from matplotlib.backend_bases import FigureCanvasBase

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.model.function_model import GraphFunctionModel
from plot_tool.model.function_model import Markers

from plot_tool.view.base.view import View


# noinspection PyPropertyAccess
class GraphFunctionLineView(Line2D, View):
    """ GraphFunction Line View """

    def __init__(self, model: GraphFunctionModel, canvas: FigureCanvasBase, *args, **kwargs):
        Line2D.__init__(
            self,
            model.graph.values.x,
            model.graph.values.y,
            visible=model.isVisible,
            label=model.name,
            color=self.convertColor(model.color),
            *args,
            **kwargs
        )
        View.__init__(self, canvas)

        # Reference Members
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

        # New functionality, changing the trace
        self.set_marker(self.convertMarker(self.model.marker))
        self.set_linestyle(self.model.style.lower())

        self.canvas.draw_idle()

    @staticmethod
    def convertMarker(marker: Markers):
        if marker == Markers.Point.value:
            return "."
        else:
            return None
