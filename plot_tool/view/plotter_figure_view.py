# python native modules

# third-party modules
from matplotlib.figure import Figure
from matplotlib.backend_bases import FigureCanvasBase

from PyQt5.QtGui import QColor

# plot-tool modules
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.model.function_model import GraphFunctionModel
from plot_tool.model.axe_model import GraphAxesModel

from plot_tool.view.function_line_view import GraphFunctionLineView
from plot_tool.view.axe_view import GraphAxesView

from plot_tool.view.base.view import View


# noinspection PyPropertyAccess
class GraphPlotterFigureView(Figure, View):
    """ GraphPlotter figure view """

    def __init__(self, model: GraphPlotterModel, *args, **kwargs):
        Figure.__init__(
            self,
            figsize=(1.5, 1),
            facecolor=self.convertColor(model.faceColor),
            edgecolor=self.convertColor(model.edgeColor),
            *args, **kwargs)
        View.__init__(self)

        # Data model references
        self.model = model

        # GraphPlotter view components
        self.graphViews = []
        self.axesViews = []
        self.legendView = None

        # Updating initial views
        for graphModel in self.model.graphModels:
            self.onGraphModelAdded(graphModel)
        for axesModel in self.model.axesModels:
            self.onAxesModelAdded(axesModel)

        # Signal and slot connection
        self.model.graphModelAdded.connect(self.onGraphModelAdded)
        self.model.graphModelRemoved.connect(self.onGraphModelRemoved)
        self.model.axesModelAdded.connect(self.onAxesModelAdded)
        self.model.axesModelRemoved.connect(self.onAxesModelRemoved)
        self.model.propertyChanged.connect(self.onPropertyChanged)

    def onPropertyChanged(self):
        """ When properties have changed, updating view... """
        self.set_facecolor(self.convertColor(self.model.faceColor))
        self.set_edgecolor(self.convertColor(self.model.edgeColor))
        self.suptitle(self.model.name if self.model.titleVisible else "")
        self.updateLegendView()

    def onGraphModelAdded(self, model: GraphFunctionModel):
        """ When the GraphFunctionModel is created """
        self.graphViews.append(GraphFunctionLineView(model, self.canvas))

        # Need to know when its color is updated!
        model.hasChanged.connect(self.updateLegendView)

        # Update axe and line attachment
        self.updateAttachments()

    def onGraphModelRemoved(self, model: GraphFunctionModel):
        """ When the GraphFunctionModel is removed """
        for graphView in self.graphViews:
            if graphView.model == model:
                self.graphViews.remove(graphView)
                graphView.remove()
                self.updateLegendView()
                break

    def onAxesModelAdded(self, model: GraphAxesModel):
        """ When the GraphAxesModel is created """
        # Sharing x axis after the first one is created
        if len(self.axesViews):
            axesView = GraphAxesView(model,
                                     self,
                                     self.canvas,
                                     [0.1, 0.1, 0.8, 0.8])

            # Magic code to hide all the axes spines
            axesView.spines["left"].set_position(("axes", 1.1))
            axesView.patch.set_visible(False)
        else:
            axesView = GraphAxesView(model,
                                     self,
                                     self.canvas,
                                     [0.1, 0.1, 0.8, 0.8])

        # Appending and adding to the figure!
        self.axesViews.append(axesView)
        self.add_axes(axesView)

        # Update axe and line attachment
        self.updateAttachments()

    def onAxesModelRemoved(self, model: GraphAxesModel):
        """ When the GraphAxesModel is removed """
        for axesView in self.axesViews:
            if axesView.model == model:

                if self.axesViews.index(axesView) == 0:
                    self.axesViews[-1].spines["left"].set_position(("data", 0))

                self.axesViews.remove(axesView)
                axesView.remove()
                self.updateLegendView()
                break

    def updateAttachments(self):
        """ Attaches every GraphFunction view to its corresponding AxesView """
        for axesView in self.axesViews:
            for graphView in self.graphViews:
                if graphView.model.graph.y_magnitude == axesView.model.yMagnitude:
                    if graphView not in axesView.get_lines():

                        # When a new line is attached, we also need to update
                        # the legend() label
                        axesView.add_line(graphView)
                        self.updateLegendView()

    def updateLegendView(self):
        """ Updating the legend view """
        if self.legendView is not None:
            self.legendView.remove()
        self.legendView = self.legend(handles=[graphView for graphView in self.graphViews if graphView.model.hasLabel],
                                      facecolor=self.convertColor(self.model.legendFaceColor),
                                      edgecolor=self.convertColor(self.model.legendEdgeColor))
        self.canvas.draw_idle()

    @staticmethod
    def convertColor(value: QColor):
        return (
            value.red() / 255,
            value.green() / 255,
            value.blue() / 255,
            value.alpha() / 255
        )
