# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QWidget

# plot-tool modules
from plot_tool.designer.function_properties.function_properties_ui import Ui_Form

from plot_tool.model.function_model import Styles
from plot_tool.model.function_model import Markers


class GraphFunctionPropertiesView(QWidget, Ui_Form):
    """ GraphFunction Properties View """

    def __init__(self, parent=None, model=None, *args, **kwargs):
        super(GraphFunctionPropertiesView, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        # Object reference
        self.models = None
        self.dialog = QColorDialog()

        # Setting up data
        self.markerList.addItems([marker.value for marker in Markers])
        self.styleList.addItems([style.value for style in Styles])

        # Setting the slots
        self.name.textChanged.connect(self.onNameChanged)
        self.markerList.currentIndexChanged.connect(self.onMarkerChanged)
        self.styleList.currentIndexChanged.connect(self.onStyleChanged)
        self.color.clicked.connect(self.onColorChanged)
        self.visible.toggled.connect(self.onVisibleChanged)
        self.legend.toggled.connect(self.onLegendChanged)

    def onNameChanged(self):
        if self.models is not None and len(self.models) == 1:
            self.models[0].name = self.name.text()

    def onMarkerChanged(self):
        if self.models is not None:
            for model in self.models:
                model.marker = self.markerList.currentText()

    def onStyleChanged(self):
        if self.models is not None:
            for model in self.models:
                model.style = self.styleList.currentText()

    def onColorChanged(self):
        if self.models is not None:
            color = self.dialog.getColor()

            # Setting into the model the new color
            for model in self.models:
                model.color = color

            # Updating new color
            self.color.setStyleSheet(
                "background: rgb({}, {}, {}, {});".format(
                    color.red() / 255,
                    color.green() / 255,
                    color.blue() / 255,
                    color.alpha() / 255
                )
            )

    def onVisibleChanged(self):
        if self.models is not None:
            for model in self.models:
                model.isVisible = self.visible.isChecked()

    def onLegendChanged(self):
        if self.models is not None:
            for model in self.models:
                model.hasLabel = self.legend.isChecked()

    def setModel(self, models):
        # Enabling and setting up the model
        self.setEnabled(True)
        self.models = models if type(models) is list else [models]

        # Updating the data
        if len(self.models) == 1:
            self.name.setText(self.models[0].name)
            self.name.setEnabled(True)
            self.markerList.setCurrentText(self.models[0].marker)
            self.styleList.setCurrentText(self.models[0].style)
            self.color.setStyleSheet(
                "background: rgb({}, {}, {}, {});".format(
                    self.models[0].color.red(),
                    self.models[0].color.green(),
                    self.models[0].color.blue(),
                    self.models[0].color.alpha()
                )
            )

            self.visible.setChecked(self.models[0].isVisible)
            self.legend.setChecked(self.models[0].hasLabel)
        else:
            self.name.setText("Many selected")
            self.name.setEnabled(False)

            self.markerList.setCurrentText(self.models[0].marker)
            self.styleList.setCurrentText(self.models[0].style)
            self.color.setStyleSheet(
                "background: rgb({}, {}, {}, {});".format(
                    self.models[0].color.red(),
                    self.models[0].color.green(),
                    self.models[0].color.blue(),
                    self.models[0].color.alpha()
                )
            )

            self.visible.setChecked(self.models[0].isVisible)
            self.legend.setChecked(self.models[0].hasLabel)


if __name__ == "__main__":
    app = QApplication([])
    widget = GraphFunctionPropertiesView()
    widget.show()
    app.exec()
