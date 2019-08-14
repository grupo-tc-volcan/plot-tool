# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget

# plot-tool modules
from plot_tool.designer.plotter_visor.plotter_visor_ui import Ui_GraphPlotterVisor

from plot_tool.data.magnitudes import GraphMagnitude

from plot_tool.model.plotter_model import GraphPlotterModel
from plot_tool.model.axe_model import Scale

from plot_tool.view.function_visor_view import GraphFunctionVisorView


class GraphPlotterVisorView(QWidget, Ui_GraphPlotterVisor):
    """ GraphPlotter model's visor view """

    def __init__(self, parent=None, model=None):
        super(GraphPlotterVisorView, self).__init__(parent)

        self.setupUi(self)
        self.colorDialog = QColorDialog()
        self.model = None
        if model is not None:
            self.setModel(model)

        self.axes.currentIndexChanged.connect(self.updateAxesData)

        self.faceColorButton.clicked.connect(self.onFaceColorButton)
        self.edgeColorButton.clicked.connect(self.onEdgeColorButton)
        self.legendFaceColorButton.clicked.connect(self.onLegendFaceColorButton)
        self.legendEdgeColorButton.clicked.connect(self.onLegendEdgeColorButton)

        self.name.textChanged.connect(self.onNameChanged)
        self.xLabel.textChanged.connect(self.onLabelXChanged)
        self.xScale.currentTextChanged.connect(self.onScaleXChanged)
        self.xMinimum.valueChanged.connect(self.onMinimumXChanged)
        self.xMaximum.valueChanged.connect(self.onMaximumXChanged)

        self.yLabel.textChanged.connect(self.onLabelYChanged)
        self.yScale.currentTextChanged.connect(self.onScaleYChanged)
        self.yMinimum.valueChanged.connect(self.onMinimumYChanged)
        self.yMaximum.valueChanged.connect(self.onMaximumYChanged)

        self.xMinimumDial.valueChanged.connect(self.onMinimumXDialChanged)
        self.xMaximumDial.valueChanged.connect(self.onMaximumXDialChanged)
        self.yMinimumDial.valueChanged.connect(self.onMinimumYDialChanged)
        self.yMaximumDial.valueChanged.connect(self.onMaximumYDialChanged)

    def onMinimumXDialChanged(self):
        self.xMinimum.setValue(float(self.xMinimumDial.value()))

    def onMaximumXDialChanged(self):
        self.xMaximum.setValue(float(self.xMaximumDial.value()))

    def onMinimumYDialChanged(self):
        self.yMinimum.setValue(float(self.yMinimumDial.value()))

    def onMaximumYDialChanged(self):
        self.yMaximum.setValue(float(self.yMaximumDial.value()))

    def verifyXValue(self, value: float):
        if self.xScale.currentText() == Scale.Log.value:
            if value < 0:
                QMessageBox.warning(
                    self,
                    "Error message",
                    "Logarithmic scale cannot have negative values!"
                )
                return False

        return True

    def verifyYValue(self, value: float):
        if self.yScale.currentText() == Scale.Log.value:
            if value < 0:
                QMessageBox.warning(
                    self,
                    "Error message",
                    "Logarithmic scale cannot have negative values!"
                )
                return False

        return True

    def onLabelYChanged(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                selectedAxes.yLabel = self.yLabel.text()

    def onScaleYChanged(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                selectedAxes.yScale = self.convertScale(self.yScale.currentText())

    def onMinimumYChanged(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                if self.verifyYValue(self.yMinimum.value()):
                    selectedAxes.yMinimum = self.yMinimum.value()
                    self.yMinimumDial.setValue(selectedAxes.yMinimum)
                else:
                    self.yMinimum.setValue(selectedAxes.yMinimum)

    def onMaximumYChanged(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                if self.verifyYValue(self.yMaximum.value()):
                    selectedAxes.yMaximum = self.yMaximum.value()
                    self.yMaximumDial.setValue(selectedAxes.yMaximum)
                else:
                    self.yMaximum.setValue(selectedAxes.yMaximum)

    def onMaximumXChanged(self):
        if self.model is not None:
            if self.verifyXValue(float(self.xMaximum.value())):
                self.model.xMaximum = float(self.xMaximum.value())
                self.xMaximumDial.setValue(self.model.xMaximum)
            else:
                self.xMaximum.setValue(self.model.xMaximum)

    def onMinimumXChanged(self):
        if self.model is not None:
            if self.verifyXValue(float(self.xMinimum.value())):
                self.model.xMinimum = float(self.xMinimum.value())
                self.xMinimumDial.setValue(self.model.xMinimum)
            else:
                self.xMinimum.setValue(self.model.xMinimum)

    def onScaleXChanged(self):
        if self.model is not None:
            self.model.xScale = self.convertScale(self.xScale.currentText())

    def onLabelXChanged(self):
        if self.model is not None:
            self.model.xLabel = self.xLabel.text()

    def onNameChanged(self):
        if self.model is not None:
            if len(self.name.text()):
                self.model.name = self.name.text()
            else:
                QMessageBox.warning(
                    self,
                    "Error message",
                    "Please remember not to use empty names!"
                )
                self.name.setText(self.model.name)

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
            if self.name.text() != self.model.name:
                self.name.setText(self.model.name)
            if self.xLabel.text() != self.model.xLabel:
                self.xLabel.setText(self.model.xLabel)
            if self.xMinimum.value() != self.model.xMinimum:
                self.xMinimum.setValue(self.model.xMinimum)
            if self.xMaximum.value() != self.model.xMaximum:
                self.xMaximum.setValue(self.model.xMaximum)

            self.xMagnitude.setText(self.model.plotter.x_magnitude.value)

            if self.xScale.currentText() != self.model.xScale.value:
                self.xScale.clear()
                self.xScale.addItems([s.value for s in Scale])
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

            self.listWidget.clear()
            items = [GraphFunctionVisorView(None, graphModel) for graphModel in self.model.graphModels]
            for item in items:
                widgetItemWrapper = QListWidgetItem(self.listWidget)
                widgetItemWrapper.setSizeHint(item.sizeHint())
                self.listWidget.addItem(widgetItemWrapper)
                self.listWidget.setItemWidget(widgetItemWrapper, item)

            self.updateAxesData()

    def updateAxesData(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]

                if self.yLabel.text() != selectedAxes.yLabel:
                    self.yLabel.setText(selectedAxes.yLabel)

                if self.yMinimum.value() != selectedAxes.yMinimum:
                    self.yMinimum.setValue(selectedAxes.yMinimum)
                if self.yMaximum.value() != selectedAxes.yMaximum:
                    self.yMaximum.setValue(selectedAxes.yMaximum)

                self.yMagnitude.setText(selectedAxes.yMagnitude.value)

                if self.yScale.currentText() != selectedAxes.yScale.value:
                    self.yScale.clear()
                    self.yScale.addItems([s.value for s in Scale])
                    self.yScale.setCurrentText(selectedAxes.yScale.value)

    @staticmethod
    def convertScale(value: str):
        for s in Scale:
            if s.value == value:
                return s
        return None


if __name__ == "__main__":
    app = QApplication([])
    widget = GraphPlotterVisorView()
    widget.show()
    app.exec()
