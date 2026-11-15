import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Images Demo")
        self.setGeometry(500, 100, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("obito.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry(
            # center of the screen
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height(),
        )


def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
