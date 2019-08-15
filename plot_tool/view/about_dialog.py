# python native modules

# third-party modules
from plot_tool.designer.about_dialog.about_dialog import Ui_Dialog

from PyQt5.QtWidgets import QDialog

# plot-tool modules


class AboutDialog(QDialog, Ui_Dialog):
    """ About Dialog """

    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
