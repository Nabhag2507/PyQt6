import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
# widgets begins with Q

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First GUI")
        # self.setGeometry(x, y, width, height)
        self.setGeometry(500, 100, 600, 600)
        self.setWindowIcon(QIcon("obito.png"))


def main():
    # We use sys.argv to allow our PyQt application to receive command-line arguments when the program starts.
    # QApplication([])     =>    Starts the application without command-line arguments

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

    # The default behaviour of main window is to hide it


if __name__ == "__main__":
    main()