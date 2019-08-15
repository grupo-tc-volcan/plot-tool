# python native modules

# third-party modules

# plot-tool modules
from plot_tool.model.plotter_model import GraphPlotterModel

from PyQt5.QtWidgets import QListView


class Session(object):
    """ The Session class contains information about the user,
    the project or the plotter which is currently being used
    when running the application.
    """

    def __init__(self):
        self.plotter_models = []

    def addPlotterModel(self, plotter_model: GraphPlotterModel):
        self.plotter_models.append(plotter_model)
