# python native modules

# third-party modules
from matplotlib.backend_bases import FigureCanvasBase

# plot-tool modules


class View(object):
    """ View base class, it will be used to define base
    signal and slots used to communicate throughout the application.
    """

    # View signals
    def __init__(self, canvas=None):
        self.canvas = canvas

    def setFigureCanvas(self, canvas: FigureCanvasBase):
        self.canvas = canvas
