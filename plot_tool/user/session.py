# python native modules

# third-party modules

# plot-tool modules
from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.data.plotter import GraphPlotter

from PyQt5.QtWidgets import QListView


class Session(object):
    """ The Session class contains information about the user,
    the project or the plotter which is currently being used
    when running the application.
    """

    def __init__(self):
        self.plotter_models = []

    def getPlotterModel(self, plotter_data: GraphPlotter):
        for plotter_model in self.plotter_models:
            if plotter_model.plotter == plotter_data:
                return plotter_model

    def addPlotterModel(self, plotter_model: GraphPlotterModel):
        self.plotter_models.append(plotter_model)
