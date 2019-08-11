# python native modules

# third-party modules

# plot-tool modules


class Session(object):
    """ The Session class contains information about the user,
    the project or the plotter which is currently being used
    when running the application.
    """

    def __init__(self):
        self.current_plotter = None
        self.plotters = []
