# python native modules
from enum import Enum

# third-party modules

# plot-tool modules


def get_magnitude_from_string(value: str):
    """ Return the GraphMagnitude Enum corresponding
    to the String value given.
    """
    for magnitude in GraphMagnitude:
        if magnitude.value == value:
            return magnitude
    return None


class GraphMagnitude(Enum):
    """ Every graph's values will have a magnitude, this way the plotting tool
    can tell which graphs can be grouped together, because they share an x axis.
    """
    Voltage = "Voltage (V)"
    Current = "Current (A)"
    Time = "Time (s)"
    Frequency = "Frequency (Hz)"
    Decibel = "Decibel (Db)"
    AngularFrequency = "Angular Frequency (rad/s)"
