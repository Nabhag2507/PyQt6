import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(500, 150, 500, 600)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet("font-size: 25px;" "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        layout.addWidget(
            self.line_edit  # , alignment=Qt.AlignmentFlag.AlignLeft, stretch=200
        )

        self.button = QPushButton("Submit")
        self.button.setStyleSheet("font-size: 25px;" "font-family: Arial;")

        layout.addWidget(self.button)

        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
