# python native modules
from enum import Enum

# third-party modules

# plot-tool modules


class GraphMagnitude(Enum):
    """ Every graph's values will have a magnitude, this way the plotting tool
    can tell which graphs can be grouped together, because they share an x axis.
    """
    Voltage = "V"
    Current = "A"
    Time = "s"
    Frequency = "Hz"
    Decibel = "Db"
    AngularFrequency = "rad/s"
