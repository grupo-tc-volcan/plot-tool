from LTSpice_feature.designer.file_select_dialog.FileSelectWindow_ui import Ui_Dialog

# Luqui's stuff
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues


class ShittyLTSpiceReader(Ui_Dialog):
    def __init__(self):
        self.plainTextEdit.setPlaceholderText("")