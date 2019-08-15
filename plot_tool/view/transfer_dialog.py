# python native modules
from io import BytesIO

# third-party modules
from PyQt5.QtSvg import QSvgWidget

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout

import matplotlib.pyplot as plot

from scipy.signal import lti

from numpy import angle
from numpy import pi

# plot-tool modules
from plot_tool.designer.transfer_dialog.transfer_dialog_ui import Ui_Dialog
from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog
from plot_tool.view.signal_dialog import SignalDialog

from plot_tool.data.values import GraphValues
from plot_tool.data.magnitudes import GraphMagnitude
from plot_tool.data.magnitudes import get_magnitude_from_string
from plot_tool.data.function import GraphFunction

# Settings needed for the functions to work!
plot.rc("mathtext", fontset="cm")


class TransferDialog(GraphFunctionDialog, Ui_Dialog):
    """ Transfer Dialog """

    def __init__(self, *args, **kwargs):
        super(TransferDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Data
        self.transferFunction = None
        self.signalFunction = None

        # Creating the preview widget
        self.previewSvg = QSvgWidget()
        self.previewLayout.addWidget(self.previewSvg)

        # Setting up components...
        self.yMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])
        self.xMagnitude.addItems([magnitude.value for magnitude in GraphMagnitude])

        # Connecting the signals...
        self.gain.textChanged.connect(self.updateWithRoots)
        self.zeros.textChanged.connect(self.updateWithRoots)
        self.poles.textChanged.connect(self.updateWithRoots)

        self.numerator.textChanged.connect(self.updateWithCoefficients)
        self.denominator.textChanged.connect(self.updateWithCoefficients)

        self.importButton.clicked.connect(self.onImport)

        self.type.currentTextChanged.connect(self.verifySetupComplete)
        self.frequencyModule.toggled.connect(self.verifySetupComplete)
        self.frequencyPhase.toggled.connect(self.verifySetupComplete)
        self.bodeModule.toggled.connect(self.verifySetupComplete)
        self.bodePhase.toggled.connect(self.verifySetupComplete)
        self.name.textChanged.connect(self.verifySetupComplete)
        self.xMagnitude.currentTextChanged.connect(self.verifySetupComplete)
        self.yMagnitude.currentTextChanged.connect(self.verifySetupComplete)

    def getGraphFunction(self) -> list:
        graphFunctions = []

        if self.type.currentText() == "Frequency Response":
            frequency, magnitudes = self.transferFunction.freqresp()

            if self.xMagnitude.currentText() == GraphMagnitude.Frequency.value:
                frequency = frequency / (2 * pi)

            if self.frequencyModule.isChecked():
                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(frequency, [abs(magnitude) for magnitude in magnitudes]),
                        get_magnitude_from_string(self.xMagnitude.currentText()),
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )
            if self.frequencyPhase.isChecked():
                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(frequency, [angle(magnitude) for magnitude in magnitudes]),
                        get_magnitude_from_string(self.xMagnitude.currentText()),
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

        elif self.type.currentText() == "Bode":
            frequency, magnitudes, phases = self.transferFunction.bode()

            if self.xMagnitude.currentText() == GraphMagnitude.Frequency.value:
                frequency = frequency / (2 * pi)

            if self.bodeModule.isChecked():
                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(frequency, [magnitude for magnitude in magnitudes]),
                        get_magnitude_from_string(self.xMagnitude.currentText()),
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

            if self.bodePhase.isChecked():
                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(frequency, [phase for phase in phases]),
                        get_magnitude_from_string(self.xMagnitude.currentText()),
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

        elif self.type.currentText() == "Temporal Response":
            if self.signalFunction is not None:
                t, y, x = self.transferFunction.output(self.signalFunction.values.y,
                                                       self.signalFunction.values.x)

                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(t, y),
                        self.signalFunction.x_magnitude,
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

            if self.impulsive.isChecked():
                t, y = self.transferFunction.impulsive()

                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(t, y),
                        GraphMagnitude.Time,
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

            if self.step.isChecked():
                t, y = self.transferFunction.step()

                graphFunctions.append(
                    GraphFunction(
                        self.name.text(),
                        GraphValues(t, y),
                        GraphMagnitude.Time,
                        get_magnitude_from_string(self.yMagnitude.currentText())
                    )
                )

        return graphFunctions

    def verifySetupComplete(self):
        if self.transferFunction is not None:
            if len(self.name.text()):
                if self.type.currentText() == "Frequency Response":
                    if self.frequencyModule.isChecked() or self.frequencyPhase.isChecked():
                        if self.xMagnitude.currentText() == GraphMagnitude.AngularFrequency.value \
                                or self.xMagnitude.currentText() == GraphMagnitude.Frequency.value:
                            self.buttonBox.setEnabled(True)
                            return
                        else:
                            self.status.setText("ERROR")
                            self.status.setStyleSheet("color: red;")
                            self.info.setText("Frequency Response requires a frequency x magnitude!")
                elif self.type.currentText() == "Bode":
                    if self.bodeModule.isChecked() or self.bodePhase.isChecked():
                        if self.xMagnitude.currentText() == GraphMagnitude.AngularFrequency.value \
                                or self.xMagnitude.currentText() == GraphMagnitude.Frequency.value:
                            self.buttonBox.setEnabled(True)
                            return
                        else:
                            self.status.setText("ERROR")
                            self.status.setStyleSheet("color: red;")
                            self.info.setText("Frequency Response requires a frequency x magnitude!")
                elif self.type.currentText() == "Temporal Response":
                    if self.signalFunction is not None or self.impulsive.isChecked() or self.step.isChecked():
                        self.buttonBox.setEnabled(True)
                        return
        self.buttonBox.setEnabled(False)

    def updateWithRoots(self):
        zeros = self.canParseStringValue(self.zeros.text())
        if zeros is not None:
            poles = self.canParseStringValue(self.poles.text())
            if poles is not None:
                gain = self.canParseGainValue(self.gain.text())
                if gain is not None:
                    latex = latex_rational_from_roots(zeros, poles, gain)
                    self.previewSvg.load(svg_from_latex(latex))

                    self.transferFunction = lti(zeros, poles, gain)

    def updateWithCoefficients(self):
        num = self.canParseStringValue(self.numerator.text())
        if num is not None:
            den = self.canParseStringValue(self.denominator.text())
            if den is not None:
                if len(num) and len(den):
                    latex = latex_rational_from_coefficients(num, den)
                    self.previewSvg.load(svg_from_latex(latex))

                    self.transferFunction = lti(num, den)

    def onImport(self):
        dialog = SignalDialog()
        if dialog.exec():
            self.signalFunction = dialog.getGraphFunction()[0]
            self.verifySetupComplete()

    def canParseGainValue(self, value: str):
        """ Returns whether the string value containing the gain is valid or not.
        If it is OK, then the float value is returned, if not, None is returned.
        """
        try:
            self.status.setText("OK")
            self.status.setStyleSheet("color: green;")
            self.info.setText("")
            return float(value)
        except:
            if len(value):
                self.status.setText("ERROR")
                self.status.setStyleSheet("color: red;")
                self.info.setText("Please... the Gain must be a number!")
            return None

    def canParseStringValue(self, value: str):
        """ Returns whether the string value received from the user interface is well formatted,
        if not then notifies the user!
        Success returns the list of values and failure returns None.
        """
        try:
            if len(value):
                split_list = value.split(",")
                parsed_list = [float(split_value) for split_value in split_list]
            else:
                parsed_list = []

            self.status.setText("OK")
            self.status.setStyleSheet("color: green;")
            self.info.setText("")

            return parsed_list
        except Exception:
            self.status.setText("ERROR")
            self.status.setStyleSheet("color: red;")
            self.info.setText("Error detected in the input fields, remember to separate each value with a comma. \n"
                              "Do not use spaces between values.")
        return None


def latex_polynomial_from_roots(roots: list) -> str:
    """ Returns a string value representing a polynomial function
    described by the given roots using LaTeX. """
    return ".".join(
        ["(s{})".format(
            "" if root == 0 else " {} {}".format("-" if root > 0 else "+", abs(root)))
            for root in roots
        ]
    )


def latex_rational_from_roots(zeros: list, poles: list, gain: float) -> str:
    """ Returns a string value representing a polynomial function
    described by the given zeros, poles and gain using LaTeX. """

    if len(zeros) and len(poles):
        return r'\frac{}{} '.format(
            "{" + "{} \cdot ".format(gain) + latex_polynomial_from_roots(zeros) + "}",
            "{" + latex_polynomial_from_roots(poles) + "}"
        )
    elif len(zeros):
        return r'{} \cdot '.format(gain) + latex_polynomial_from_roots(zeros)
    elif len(poles):
        return r'\frac{}{} '.format(
            "{" + "{}".format(gain) + "}",
            "{" + latex_polynomial_from_roots(poles) + "}"
        )
    else:
        return "{}".format(gain)


def latex_polynomial_from_coefficients(coefs: list) -> str:
    """ Returns a string value representing a polynomial function
    described by the given coefficients using LaTeX. """
    return " + ".join(
        [r'{} {}'.format(c, " \cdot s^{" + str(len(coefs)-i-1) + "}" if c != coefs[-1] else "")
         for i, c in enumerate(coefs)
         ]
    )


def latex_rational_from_coefficients(num: list, den: list) -> str:
    """ Returns a string value representing the rational function
    described by the given coefficients, using the LaTeX language
    to describe that function. """
    return r'\frac{}{} '.format(
        "{" + latex_polynomial_from_coefficients(num) + "}",
        "{" + latex_polynomial_from_coefficients(den) + "}"
    )


def svg_from_latex(latex: str, font_size=12, dpi=300):
    """ Returns data needed to create a SVG image with
    the content of a string formatted with LaTex language. """

    # We create a figure where we print the LaTeX
    figure = plot.figure(figsize=(1, 1))
    figure.text(0, 0, r'${}$'.format(latex), fontsize=font_size)

    # We create the output, where the SVG data is saved
    output = BytesIO()
    figure.savefig(
        output,
        dpi=dpi,
        transparent=True,
        format="svg",
        bbox_inches="tight",
        pad_inches=0.0,
        frameon=False
    )

    # Closes the plot and saves data
    plot.close(figure)
    output.seek(0)
    return output.read()


def main():
    app = QApplication([])
    dialog = TransferDialog()
    dialog.exec()
    app.exec()
