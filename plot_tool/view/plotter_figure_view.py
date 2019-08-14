# python native modules

# third-party modules
from matplotlib.figure import Figure

# plot-tool modules
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.model.function_model import GraphFunctionModel
from plot_tool.model.axe_model import GraphAxesModel

from plot_tool.view.function_line_view import GraphFunctionLineView
from plot_tool.view.axe_view import GraphAxesView


class GraphPlotterFigureView(Figure):
    """ GraphPlotter figure view """

    def __init__(self, model: GraphPlotterModel, *args, **kwargs):
        super(GraphPlotterFigureView, self).__init__(
            figsize=(1, 1),
            *args, **kwargs)

        # Data model references
        self.model = model
        self.parent = None

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

    def setParent(self, parent):
        """ Setting up the parent """
        self.parent = parent

    def onGraphModelAdded(self, model: GraphFunctionModel):
        """ When the GraphFunctionModel is created """
        self.graphViews.append(GraphFunctionLineView(model, self))

        # Update axe and line attachment
        self.updateAttachments()

    def onGraphModelRemoved(self, model: GraphFunctionModel):
        """ When the GraphFunctionModel is removed """
        graphView = GraphFunctionLineView(model, self)
        self.graphViews.remove(graphView)
        graphView.remove()

    def onAxesModelAdded(self, model: GraphAxesModel):
        """ When the GraphAxesModel is created """
        # Sharing x axis after the first one is created
        if len(self.axesViews):
            axesView = GraphAxesView(model,
                                     self,
                                     [0.1, 0.1, 0.8, 0.8],
                                     sharex=self.axesViews[0])

            # Magic code to hide all the axes spines
            axesView.spines["left"].set_position(("axes", 1.1))
            axesView.set_frame_on(True)
            axesView.patch.set_visible(False)
            for spine in axesView.spines.values():
                spine.set_visible(False)
            axesView.spines["left"].set_visible(True)

            # Resizing the figure to keep adding new axis
            self.set_figwidth(self.get_figwidth() * 1.1)
        else:
            axesView = GraphAxesView(model,
                                     self,
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
                self.axesViews.remove(axesView)
                axesView.remove()

    def updateAttachments(self):
        """ Attaches every GraphFunction view to its corresponding AxesView """
        for axesView in self.axesViews:
            for graphView in self.graphViews:
                if graphView.model.graph.y_magnitude == axesView.model.yMagnitude:
                    if graphView not in axesView.get_lines():

                        # When a new line is attached, we also need to update
                        # the legend() label
                        axesView.add_line(graphView)
                        if self.legendView is not None:
                            self.legendView.remove()
                        self.legendView = self.legend(handles=self.graphViews)
