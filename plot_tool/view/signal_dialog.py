# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication

from numpy import sin
from numpy import pi
from numpy import radians
from numpy import arange
from numpy import heaviside

from scipy.signal import square

# plot-tool modules
from plot_tool.designer.graph_dialog.graph_dialog_ui import Ui_Dialog

from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog

from plot_tool.data.magnitudes import get_magnitude_from_string
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
        self.sinDc.valueChanged.connect(self.onChanges)

        self.stepAmplitude.valueChanged.connect(self.onChanges)

        self.triangleAmplitude.valueChanged.connect(self.onChanges)
        self.triangleFrequency.valueChanged.connect(self.onChanges)
        self.triangleSymmetry.valueChanged.connect(self.onChanges)
        self.triangleDc.valueChanged.connect(self.onChanges)

        self.squareAmplitude.valueChanged.connect(self.onChanges)
        self.squareFrequency.valueChanged.connect(self.onChanges)
        self.squareDuty.valueChanged.connect(self.onChanges)
        self.squareDc.valueChanged.connect(self.onChanges)

        self.fromInput.valueChanged.connect(self.onChanges)
        self.toInput.valueChanged.connect(self.onChanges)

    def onChanges(self):
        """ Whenever a change is done in the SignalDialog, we have to check if everything needed has been set up
        and enable the Ok button. """
        if len(self.nameInput.text()):
            if self.fromInput.value() < self.toInput.value():
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

    def getGraphFunction(self) -> list:
        """ When the SignalDialog has ended with an accepted() signal from the user,
        the result will be received through this method. """
        graphFunctions = []

        times = arange(self.fromInput.value(),
                       self.toInput.value(),
                       (self.toInput.value() - self.fromInput.value()) / 1000)

        if self.waveformsInput.currentText() == "Sinusoidal":
            amplitude = float(self.sinAmplitude.value())
            frequency = float(self.sinFrequency.value())
            phase = float(self.sinPhase.value())
            dc = float(self.sinDc.value())

            values = [amplitude * sin(time * 2 * pi * frequency + radians(phase)) + dc for time in times]

            graphFunctions.append(
                GraphFunction(
                    self.nameInput.text(),
                    GraphValues(list(times), values),
                    get_magnitude_from_string(self.xMagnitudeInput.currentText()),
                    get_magnitude_from_string(self.yMagnitudeInput.currentText())
                )
            )
        elif self.waveformsInput.currentText() == "Step":
            amplitude = float(self.stepAmplitude.value())
            values = [amplitude * heaviside(time, amplitude) for time in times]

            graphFunctions.append(
                GraphFunction(
                    self.nameInput.text(),
                    GraphValues(list(times), list(values)),
                    get_magnitude_from_string(self.xMagnitudeInput.currentText()),
                    get_magnitude_from_string(self.yMagnitudeInput.currentText())
                )
            )
        elif self.waveformsInput.currentText() == "Square":
            amplitude = float(self.squareAmplitude.value())
            frequency = float(self.squareFrequency.value())
            duty = float(self.squareDuty.value())
            dc = float(self.squareDc.value())

            values = amplitude * square(2 * pi * frequency * times, duty/100) + dc

            graphFunctions.append(
                GraphFunction(
                    self.nameInput.text(),
                    GraphValues(list(times), list(values)),
                    get_magnitude_from_string(self.xMagnitudeInput.currentText()),
                    get_magnitude_from_string(self.yMagnitudeInput.currentText())
                )
            )
        elif self.waveformsInput.currentText() == "Triangle":
            amplitude = float(self.triangleAmplitude.value())
            frequency = float(self.triangleFrequency.value())
            symmetry = float(self.triangleSymmetry.value())
            dc = float(self.triangleDc.value())

            def triangle(time: float) -> float:
                t = time % (1 / frequency)

                if t < symmetry / (frequency * 100):
                    return (100 * t * frequency * amplitude) / symmetry
                else:
                    return ((amplitude * 100) / (symmetry - 100)) * (frequency * t - 1)

            values = [triangle(t) + dc for t in times]

            graphFunctions.append(
                GraphFunction(
                    self.nameInput.text(),
                    GraphValues(list(times), list(values)),
                    get_magnitude_from_string(self.xMagnitudeInput.currentText()),
                    get_magnitude_from_string(self.yMagnitudeInput.currentText())
                )
            )

        return graphFunctions


if __name__ == "__main__":
    app = QApplication([])
    dialog = SignalDialog()
    dialog.show()
    app.exec()
