"""
Sample 0: Creates a QTApplication, builds the MainWindow and runs it.
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication

# plot-tool modules
from plot_tool.view.window import Window


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
