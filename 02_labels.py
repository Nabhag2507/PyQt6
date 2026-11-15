import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt  # used for alignment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 50))
        label.setGeometry(0, 0, 500, 100)

        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        # label.setAlignment(Qt.AlignmentFlag.AlignTop)
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # Qt.AlignmentFlag.AlignCenter
        # Qt.AlignmentFlag.AlignLeft
        # Qt.AlignmentFlag.AlignRight
        # Qt.AlignmentFlag.AlignTop
        # Qt.AlignmentFlag.AlignBottom
        # Qt.AlignmentFlag.AlignHCenter
        # Qt.AlignmentFlag.AlignVCenter

        label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
