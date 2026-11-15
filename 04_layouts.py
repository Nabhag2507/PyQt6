import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setGeometry(100, 100, 500, 500)
        self.initUI()

    # common practice
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # when working with layout managers, we will add that layout manager to the central widget
        # the central widget is then added to the main window

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()
        vbox = QGridLayout()

        # row 0 column 0
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 1, 0)
        vbox.addWidget(label3, 2, 1)
        vbox.addWidget(label4, 3, 0)
        vbox.addWidget(label5, 3, 3)

        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
