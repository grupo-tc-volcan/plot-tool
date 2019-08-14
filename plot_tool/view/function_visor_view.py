# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QWidget

# plot-tool modules
from plot_tool.designer.function_visor.function_visor_ui import Ui_FunctionVisor

from plot_tool.model.function_model import GraphFunctionModel


class GraphFunctionVisorView(QWidget, Ui_FunctionVisor):
    """ GraphFunction Visor View """

    def __init__(self, parent=None, model=None, *args, **kwargs):
        super(GraphFunctionVisorView, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        # Object references
        self.model = None
        self.dialog = QColorDialog()
        if model is not None:
            self.setModel(model)

        # Signal connection
        self.changeColorButton.clicked.connect(self.onChangeColorButton)
        self.isVisibleBox.toggled.connect(self.onVisibleToggled)
        self.deleteButton.clicked.connect(self.onDeleteButton)

    def onDeleteButton(self):
        if self.model is not None:
            self.model.parent.removeGraph(self.model.graph)

    def onVisibleToggled(self):
        if self.model is not None:
            self.model.isVisible = self.isVisibleBox.isChecked()

    def onChangeColorButton(self):
        if self.model is not None:
            self.model.color = self.dialog.getColor()

    def setModel(self, model: GraphFunctionModel):
        # Reference
        self.model = model
        self.updateViewData()

        # Signal connections
        self.model.hasChanged.connect(self.updateViewData)

    def updateViewData(self):
        if self.model is not None:
            self.name.setText(self.model.name)
            self.isVisibleBox.setChecked(self.model.isVisible)
            self.color.setStyleSheet(
                "background-color: rgb({}, {}, {}, {});".format(
                    self.model.color.red(),
                    self.model.color.green(),
                    self.model.color.blue(),
                    self.model.color.alpha()
                )
            )


if __name__ == "__main__":
    app = QApplication([])
    app.exec()
