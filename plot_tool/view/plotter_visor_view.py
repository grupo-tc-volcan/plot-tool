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
from plot_tool.model.axe_model import Grid

from plot_tool.view.function_visor_view import GraphFunctionVisorView


# noinspection PyPropertyAccess
class GraphPlotterVisorView(QWidget, Ui_GraphPlotterVisor):
    """ GraphPlotter model's visor view """

    def __init__(self, parent=None, model=None):
        super(GraphPlotterVisorView, self).__init__(parent)

        # Initial settings
        self.setupUi(self)
        self.setEnabled(False)

        # References
        self.colorDialog = QColorDialog()
        self.model = None

        if model is not None:
            self.setModel(model)

        self.gridOption.addItems([grid.value for grid in Grid])

        self.axes.currentIndexChanged.connect(self.updateAxesData)

        self.axesFaceColorButton.clicked.connect(self.onAxesFaceColorButton)
        self.faceColorButton.clicked.connect(self.onFaceColorButton)
        self.edgeColorButton.clicked.connect(self.onEdgeColorButton)
        self.legendFaceColorButton.clicked.connect(self.onLegendFaceColorButton)
        self.legendEdgeColorButton.clicked.connect(self.onLegendEdgeColorButton)

        self.adjustButton.clicked.connect(self.onAdjustButton)
        self.name.textChanged.connect(self.onNameChanged)

        self.xLabel.textChanged.connect(self.onLabelXChanged)
        self.xScale.currentTextChanged.connect(self.onScaleXChanged)
        self.xMinimum.valueChanged.connect(self.onXIntervalChanged)
        self.xMaximum.valueChanged.connect(self.onXIntervalChanged)

        self.yLabel.textChanged.connect(self.onLabelYChanged)
        self.yScale.currentTextChanged.connect(self.onScaleYChanged)
        self.yMinimum.valueChanged.connect(self.onYIntervalChanged)
        self.yMaximum.valueChanged.connect(self.onYIntervalChanged)

        self.visible.toggled.connect(self.onIsVisibleButton)

        self.gridOption.currentTextChanged.connect(self.onGridOption)
        self.gridVisible.toggled.connect(self.onGridVisible)

    def onGridOption(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]

                selectedAxes.gridOption = self.gridOption.currentText()

    def onGridVisible(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]

                selectedAxes.gridEnable = self.gridVisible.isChecked()

    def onIsVisibleButton(self):
        if self.model is not None:
            self.model.titleVisible = self.visible.isChecked()

    def onAdjustButton(self):
        if self.model is not None:
            self.model.adjustSizeOfXAxis()
            self.model.adjustSizeOfYAxis()

            self.loadViewData()

    def verifyXInterval(self) -> bool:
        xMinimum = self.xMinimum.value()
        xMaximum = self.xMaximum.value()
        xScale = self.xScale.currentText()

        # Check if values are in the correct order...
        if xMinimum >= xMaximum:
            return False

        # Check if there are no negative values when using Logarithmic Scale...
        if xScale == Scale.Log.value and xMinimum <= 0:
            return False

        return True

    def verifyYInterval(self) -> bool:
        if len(self.model.axesModels):
            yMinimum = self.yMinimum.value()
            yMaximum = self.yMaximum.value()
            yScale = self.yScale.currentText()

            # Check if values are in the correct order...
            if yMinimum >= yMaximum:
                return False

            # Check if there are no negative values when using Logarithmic Scale...
            if yScale == Scale.Log.value and yMinimum <= 0:
                return False

            return True

    def onXIntervalChanged(self):
        if self.model is not None:
            if self.verifyXInterval():
                self.model.xMinimum = self.xMinimum.value()
                self.model.xMaximum = self.xMaximum.value()

    def onYIntervalChanged(self):
        if self.model is not None:
            if self.verifyYInterval():
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                selectedAxes.yMinimum = self.yMinimum.value()
                selectedAxes.yMaximum = self.yMaximum.value()

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

                if selectedAxes.yScale == Scale.Log:
                    if self.yMaximum.value() <= 0:
                        self.yMaximum.setValue(1)
                    if self.yMinimum.value() <= 0:
                        self.yMinimum.setValue(1)

    def onLabelXChanged(self):
        if self.model is not None:
            self.model.xLabel = self.xLabel.text()

    def onScaleXChanged(self):
        if self.model is not None:
            self.model.xScale = self.convertScale(self.xScale.currentText())

            if self.model.xScale == Scale.Log:
                if self.xMaximum.value() <= 0:
                    self.xMaximum.setValue(1)
                if self.xMinimum.value() <= 0:
                    self.xMinimum.setValue(1)

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

    def onAxesFaceColorButton(self):
        if self.model is not None:
            if len(self.model.axesModels):
                selectedAxes = self.model.axesModels[self.axes.currentIndex()]
                selectedAxes.faceColor = self.colorDialog.getColor()

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

        # Enabling the widget
        self.setEnabled(True)

        self.loadViewData()

    def loadViewData(self):
        if self.model is not None:
            if self.name.text() != self.model.name:
                self.name.setText(self.model.name)
            if self.xLabel.text() != self.model.xLabel:
                self.xLabel.setText(self.model.xLabel)
            if self.xMinimum.value() != self.model.xMinimum:
                self.xMinimum.setValue(self.model.xMinimum)
            if self.xMaximum.value() != self.model.xMaximum:
                self.xMaximum.setValue(self.model.xMaximum)

    def removeModel(self):
        self.model = None
        self.name.clear()

        self.xMaximum.clear()
        self.xMinimum.clear()
        self.yMaximum.clear()
        self.yMinimum.clear()
        self.xMagnitude.clear()
        self.yMagnitude.clear()
        self.listWidget.clear()

        self.setEnabled(False)

    def updateViewData(self):
        if self.model is not None:

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

                self.axesFaceColor.setStyleSheet(
                    "background-color: rgb({}, {}, {});".format(
                        selectedAxes.faceColor.red(),
                        selectedAxes.faceColor.green(),
                        selectedAxes.faceColor.blue()
                    )
                )

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
