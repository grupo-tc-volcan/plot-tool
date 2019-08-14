# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QWidget

# plot-tool modules
from plot_tool.designer.plotter_visor.plotter_visor_ui import Ui_GraphPlotterVisor

from plot_tool.data.magnitudes import GraphMagnitude

from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.model.axe_model import Scale


class GraphPlotterVisorView(QWidget, Ui_GraphPlotterVisor):
    """ GraphPlotter model's visor view """

    def __init__(self, parent=None, *args, **kwargs):
        super(GraphPlotterVisorView, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.colorDialog = QColorDialog()
        self.model = None

        self.axes.currentIndexChanged.connect(self.updateAxesData)

        self.faceColorButton.clicked.connect(self.onFaceColorButton)
        self.edgeColorButton.clicked.connect(self.onEdgeColorButton)
        self.legendFaceColorButton.clicked.connect(self.onLegendFaceColorButton)
        self.legendEdgeColorButton.clicked.connect(self.onLegendEdgeColorButton)

    def onFaceColorButton(self):
        if self.model is not None:
            self.model.faceColor = self.colorDialog.getColor()

    def onEdgeColorButton(self):
        if self.model is not None:
            self.model.edgeColor = self.colorDialog.getColor()

    def onLegendFaceColorButton(self):
        if self.model is not None:
            self.model.legendFaceColor = self.colorDialog.getColor()

    def onLegendEdgeColorButton(self):
        if self.model is not None:
            self.model.legendEdgeColor = self.colorDialog.getColor()

    def setModel(self, model: GraphPlotterModel):
        # Setting the reference
        self.model = model

        # Signal connections
        self.model.hasChanged.connect(self.updateViewData)
        self.updateViewData()

    def updateViewData(self):
        if self.model is not None:
            self.name.setText(self.model.name)
            self.xLabel.setText(self.model.xLabel)
            self.xMinimum.setValue(self.model.xMinimum)
            self.xMaximum.setValue(self.model.xMaximum)
            self.xMagnitude.setText(self.model.plotter.x_magnitude.value)

            self.xScale.clear()
            self.xScale.addItems([scale.value for scale in Scale])
            self.xScale.setCurrentText(self.model.xScale.value)

            self.axes.clear()
            self.axes.addItems(["Axes {}".format(index) for index in range(len(self.model.axesModels))])

            self.faceColorView.setStyleSheet(
                "background-color: rgb({}, {}, {}, {});".format(
                    self.model.faceColor.red(),
                    self.model.faceColor.green(),
                    self.model.faceColor.blue(),
                    self.model.faceColor.alpha()
                )
            )

            self.edgeColorView.setStyleSheet(
                "background-color: rgb({}, {}, {}, {});".format(
                    self.model.edgeColor.red(),
                    self.model.edgeColor.green(),
                    self.model.edgeColor.blue(),
                    self.model.edgeColor.alpha()
                )
            )

            self.legendFaceColorView.setStyleSheet(
                "background-color: rgb({}, {}, {}, {});".format(
                    self.model.legendFaceColor.red(),
                    self.model.legendFaceColor.green(),
                    self.model.legendFaceColor.blue(),
                    self.model.legendFaceColor.alpha()
                )
            )

            self.legendEdgeColorView.setStyleSheet(
                "background-color: rgb({}, {}, {}, {});".format(
                    self.model.legendEdgeColor.red(),
                    self.model.legendEdgeColor.green(),
                    self.model.legendEdgeColor.blue(),
                    self.model.legendEdgeColor.alpha()
                )
            )

            self.updateAxesData()

    def updateAxesData(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]

                self.yLabel.setText(selectedAxes.yLabel)
                self.yMinimum.setValue(selectedAxes.yMinimum)
                self.yMaximum.setValue(selectedAxes.yMaximum)
                self.yMagnitude.setText(selectedAxes.yMagnitude.value)

                self.yScale.clear()
                self.yScale.addItems([scale.value for scale in Scale])
                self.yScale.setCurrentText(selectedAxes.yScale.value)


if __name__ == "__main__":
    app = QApplication([])
    widget = GraphPlotterVisorView()
    widget.show()
    app.exec()
