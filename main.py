# python native modules
import sys

# third-party modules
from PyQt5.QtWidgets import QApplication

# plot-tool modules
from plot_tool.view.window import Window


def main(*args, **kwargs):
    """ Main function of the PlotTool application.
    """
    # Creates an instance of QApplication passing the system arguments
    app = QApplication(sys.argv)

    # New MainWindow displayed
    window = Window()
    window.show()

    # Event loop!
    sys.exit(app.exec())


if __name__ == "__main__":
    # Executing the main function
    main()
