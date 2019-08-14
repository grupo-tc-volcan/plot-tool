# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication

from numpy import sin
from numpy import square
from numpy import heaviside
from numpy import pi
from numpy import radians
from numpy import arange

# plot-tool modules
from plot_tool.designer.graph_dialog.graph_dialog_ui import Ui_Dialog

from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog

from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.function import GraphFunction
from plot_tool.data.values import GraphValues


class SignalDialog(GraphFunctionDialog, Ui_Dialog):
    """ Signal Form Dialog """

    def __init__(self, *args, **kwargs):
        super(SignalDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.xMagnitudeInput.addItems([magnitude.value for magnitude in GraphMagnitude])
        self.yMagnitudeInput.addItems([magnitude.value for magnitude in GraphMagnitude])
        self.buttonBox.setEnabled(False)

        self.nameInput.textChanged.connect(self.onChanges)
        self.xMagnitudeInput.currentIndexChanged.connect(self.onChanges)
        self.yMagnitudeInput.currentIndexChanged.connect(self.onChanges)
        self.waveformsInput.currentIndexChanged.connect(self.onChanges)

        self.sinAmplitude.valueChanged.connect(self.onChanges)
        self.sinFrequency.valueChanged.connect(self.onChanges)
        self.sinPhase.valueChanged.connect(self.onChanges)

        self.stepAmplitude.valueChanged.connect(self.onChanges)

        self.triangleAmplitude.valueChanged.connect(self.onChanges)
        self.triangleFrequency.valueChanged.connect(self.onChanges)
        self.triangleSymmetry.valueChanged.connect(self.onChanges)

        self.squareAmplitude.valueChanged.connect(self.onChanges)
        self.squareFrequency.valueChanged.connect(self.onChanges)
        self.squareDuty.valueChanged.connect(self.onChanges)

    def onChanges(self):
        if len(self.nameInput.text()):
            if self.xMagnitudeInput.currentText() != self.yMagnitudeInput.currentText():

                if self.waveformsInput.currentText() == "Sinusoidal":
                    if self.sinAmplitude.value() != 0.0 and self.sinFrequency.value() != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Step":
                    if self.stepAmplitude.value() != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Square":
                    if self.squareAmplitude.value() != 0.0 \
                            and self.squareFrequency.value() != 0.0 and self.squareDuty != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
                elif self.waveformsInput.currentText() == "Triangle":
                    if self.triangleAmplitude.value() != 0.0 \
                            and self.triangleFrequency.value() != 0.0 and self.triangleSymmetry != 0.0:
                        self.buttonBox.setEnabled(True)
                        return
        self.buttonBox.setEnabled(False)

    def getGraphFunction(self) -> GraphFunction:
        if self.waveformsInput.currentText() == "Sinusoidal":
            amplitude = float(self.sinAmplitude.value())
            frequency = float(self.sinFrequency.value())
            phase = float(self.sinPhase.value())

            times = arange(0, 1 / frequency, 1 / frequency / 100)
            values = [amplitude * sin(time * 2 * pi * frequency + radians(phase)) for time in times]

            return GraphFunction(
                self.nameInput.text(),
                GraphValues(list(times), values),
                self.xMagnitudeInput.currentText(),
                self.yMagnitudeInput.currentText()
            )


if __name__ == "__main__":
    app = QApplication([])
    dialog = SignalDialog()
    dialog.show()
    app.exec()
