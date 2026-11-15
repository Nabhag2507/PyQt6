import sys
from tokenize import Triple
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hello", self)

        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 15px;")

        # with buttons we need signal that's connected to a slot
        # that signal isn't event the slot is an action that is going to take when click the button
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)

        self.label.setText("Good byee!")


def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
