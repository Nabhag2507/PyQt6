import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton, QVBoxLayout
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVBoxLayout Example")
        self.setFixedSize(400, 300)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create widgets
        title = QLabel("Login Form")
        username = QLineEdit()
        password = QLineEdit()
        login_btn = QPushButton("Login")

        username.setPlaceholderText("Enter username")
        password.setPlaceholderText("Enter password")
        password.setEchoMode(QLineEdit.EchoMode.Password)

        # Create vertical layout
        layout = QVBoxLayout()

        # Add widgets vertically
        layout.addWidget(title)
        layout.addWidget(username)
        layout.addWidget(password)
        layout.addWidget(login_btn)

        # Apply layout
        central_widget.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()