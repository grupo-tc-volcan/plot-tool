# python native modules

# third-party modules
from PyQt5.QtWidgets import QDialog

# plot-tool modules
from plot_tool.data.function import GraphFunction


class GraphFunctionDialog(QDialog):
    """ Defines the base class as an interface to a dialog which will
    return a GraphFunction object as a positive result.
    """

    def __init__(self, *args, **kwargs):
        super(GraphFunctionDialog, self).__init__(*args, **kwargs)

    def getGraphFunction(self) -> GraphFunction:
        """ Returns the resulting value of GraphFunction.
        If was rejected, should return None.
        """
        raise NotImplemented
