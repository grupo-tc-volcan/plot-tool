# python native modules

# third-party modules

# plot-tool modules
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.values import GraphValues


class GraphFunction(object):
    """ Describes a function with values and which magnitudes refer
    each of the axis. The function's name defines what it represents.
    """

    def __init__(self,
                 name: str,
                 values: GraphValues,
                 x_magnitude: GraphMagnitude,
                 y_magnitude: GraphMagnitude):
        self.name = name
        self.values = values
        self.x_magnitude = x_magnitude
        self.y_magnitude = y_magnitude

    def __eq__(self, other) -> bool:
        return self.name == other.name
