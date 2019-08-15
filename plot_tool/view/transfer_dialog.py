# python native modules
from io import BytesIO

# third-party modules
from PyQt5.QtSvg import QSvgWidget

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout

import matplotlib.pyplot as plot

# plot-tool modules
from plot_tool.designer.transfer_dialog.transfer_dialog_ui import Ui_Dialog
from plot_tool.view.base.graph_dialog_view import GraphFunctionDialog

# Settings needed for the functions to work!
plot.rc("mathtext", fontset="cm")


class TransferDialog(GraphFunctionDialog, Ui_Dialog):
    """ Transfer Dialog """

    def __init__(self, *args, **kwargs):
        super(TransferDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Creating the preview widget
        self.previewSvg = QSvgWidget()
        self.previewLayout.addWidget(self.previewSvg)

        # Connecting the signals...
        self.gain.textChanged.connect(self.updateWithRoots)
        self.zeros.textChanged.connect(self.updateWithRoots)
        self.poles.textChanged.connect(self.updateWithRoots)

        self.numerator.textChanged.connect(self.updateWithCoefficients)
        self.denominator.textChanged.connect(self.updateWithCoefficients)

        self.type.currentTextChanged.connect(self.onType)
        self.importButton.clicked.connect(self.onImport)

        self.frequencyModule.toggled.connect(self.onFrequencyModule)
        self.frequencyPhase.toggled.connect(self.onFrequencyPhase)
        self.bodeModule.toggled.connect(self.onBodeModule)
        self.bodePhase.toggled.connect(self.onBodePhase)

    def updateWithRoots(self):
        zeros = self.canParseStringValue(self.zeros.text())
        if zeros is not None:
            poles = self.canParseStringValue(self.poles.text())
            if poles is not None:
                gain = self.canParseGainValue(self.gain.text())
                if gain is not None:
                    if len(zeros) and len(poles):
                        latex = latex_rational_from_roots(zeros, poles, gain)
                        self.previewSvg.load(svg_from_latex(latex))

    def updateWithCoefficients(self):
        num = self.canParseStringValue(self.numerator.text())
        if num is not None:
            den = self.canParseStringValue(self.denominator.text())
            if den is not None:
                if len(num) and len(den):
                    latex = latex_rational_from_coefficients(num, den)
                    self.previewSvg.load(svg_from_latex(latex))

    def onType(self):
        pass

    def onFrequencyModule(self):
        pass

    def onFrequencyPhase(self):
        pass

    def onBodeModule(self):
        pass

    def onBodePhase(self):
        pass

    def onImport(self):
        pass

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
    return ".".join(["(s {} {})".format("-" if root > 0 else "+", abs(root)) for root in roots])


def latex_rational_from_roots(zeros: list, poles: list, gain: float) -> str:
    """ Returns a string value representing a polynomial function
    described by the given zeros, poles and gain using LaTeX. """
    return r'\frac{}{} '.format(
        "{" + "{} \cdot ".format(gain) + latex_polynomial_from_roots(zeros) + "}",
        "{" + latex_polynomial_from_roots(poles) + "}"
    )


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
