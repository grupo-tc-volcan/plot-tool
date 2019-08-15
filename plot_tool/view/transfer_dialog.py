# python native modules
from io import BytesIO

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSvg import QSvgWidget

import matplotlib.pyplot as plot

# plot-tool modules

# Settings needed for the functions to work!
plot.rc("mathtext", fontset="cm")


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


if __name__ == "__main__":
    app = QApplication([])
    svg = QSvgWidget()
    svg.load(svg_from_latex(latex_rational_from_coefficients([1, 2, 3], [2, 3, 4])))
    svg.show()
    app.exec()
