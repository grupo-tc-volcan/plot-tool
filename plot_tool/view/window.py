# python native modules

# third-party modules
from PyQt5.QtWidgets import QMainWindow

# plot-tool modules
from plot_tool.designer.window.window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    """ Application Window """

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
