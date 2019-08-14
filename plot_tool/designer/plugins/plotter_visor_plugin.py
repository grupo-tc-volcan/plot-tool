# python native modules

# third-party modules
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

# sae project modules
from plot_tool.view.plotter_visor_view import GraphPlotterVisorView


class GraphPlotterVisorViewPlugin(QPyDesignerCustomWidgetPlugin):
    """ Plugin Class to create a custom draggable object
    so as it can be used in the QtCreator framework when
    designing the main window. """

    def __init__(self, parent=None):
        super(GraphPlotterVisorViewPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return GraphPlotterVisorView(parent)

    def name(self):
        return "GraphPlotterVisorView"

    def group(self):
        return "PlotTool Widgets"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def domXml(self):
        return '<widget class="GraphPlotterVisorView" name="visorView">\n' \
               ' <property name="toolTip">\n' \
               '  <string>Click and drag here</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis">\n' \
               '  <string>Visor View. ' \
               ' </string>\n' \
               ' </property>\n' \
               '</widget>\n'

    def includeFile(self):
        return "plotter_visor_view"
