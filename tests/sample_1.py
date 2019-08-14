import sys

from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *

from io import BytesIO

import matplotlib.pyplot as plt

plt.rc("mathtext", fontset="cm")


def text2svg(formula, fontsize=12, dpi=300):
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, r'${}$'.format(formula), fontsize=fontsize)

    output = BytesIO()
    fig.savefig(output, dpi=dpi, transparent=True, format="svg",
                bbox_inches="tight", pad_inches=0.0, frameon=False)

    plt.close(fig)

    output.seek(0)
    return output.read()


if __name__ == "__main__":
    FORMULA = r'\sqrt{\frac{a}{b}}'

    app = QApplication(sys.argv)
    svg = QSvgWidget()
    svg.load(text2svg(FORMULA))
    svg.show()
    sys.exit(app.exec_())
