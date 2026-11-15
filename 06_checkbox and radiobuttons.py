import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QRadioButton,
    QCheckBox,
    QPushButton,
    QButtonGroup,
)


# checkbox/radiobutton.*signal*.connect(*slot*)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radio Buttons & Checkboxes")
        self.setGeometry(500, 200, 450, 500)

        self.initUI()

    def initUI(self):

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # RADIO BUTTONS
        layout.addWidget(QLabel("Choose your favourite language:"))

        self.radio1 = QRadioButton("Python")
        self.radio2 = QRadioButton("Java")
        self.radio3 = QRadioButton("C++")

        # Group radio buttons to make them mutually exclusive
        self.radio_group = QButtonGroup(self)

        self.radio_group.addButton(self.radio1)
        self.radio_group.addButton(self.radio2)
        self.radio_group.addButton(self.radio3)

        # Connect radio button signal
        self.radio_group.buttonToggled.connect(self.radio_button_changed)

        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        # CHECKBOXES (Select multiple)

        layout.addWidget(QLabel("Choose technologies you know:"))

        self.check1 = QCheckBox("Machine Learning")
        self.check2 = QCheckBox("Deep Learning")
        self.check3 = QCheckBox("NLP")
        self.check4 = QCheckBox("PyQt6")

        # Connect checkbox signals
        self.check1.toggled.connect(self.checkbox_changed)
        self.check2.toggled.connect(self.checkbox_changed)
        self.check3.toggled.connect(self.checkbox_changed)
        self.check4.toggled.connect(self.checkbox_changed)

        layout.addWidget(self.check1)
        layout.addWidget(self.check2)
        layout.addWidget(self.check3)
        layout.addWidget(self.check4)

        # SUBMIT AND RESET BUTTONS
        self.submit_btn = QPushButton("Submit")
        self.reset_btn = QPushButton("Reset")

        self.submit_btn.clicked.connect(self.submit)
        self.reset_btn.clicked.connect(self.reset)

        layout.addWidget(self.submit_btn)
        layout.addWidget(self.reset_btn)

        # Output label
        self.result_label = QLabel("Your selections will appear here.")
        self.result_label.setWordWrap(True)

        layout.addWidget(self.result_label)

    # RADIO BUTTON SLOT
    def radio_button_changed(self, button, checked):

        # buttonToggled emits for both checked and unchecked
        if checked:
            print(f"Selected language: {button.text()}")

    # CHECKBOX SLOT

    def checkbox_changed(self, checked):

        # self.sender() returns the checkbox that emitted the signal
        checkbox = self.sender()

        if checked:
            print(f"{checkbox.text()} selected")
        else:
            print(f"{checkbox.text()} deselected")

    # SUBMIT SLOT

    def submit(self):

        # Get selected radio button
        selected_language = self.radio_group.checkedButton()

        language = selected_language.text() if selected_language else "None"

        # Get all checked checkboxes
        technologies = []

        for checkbox in [self.check1, self.check2, self.check3, self.check4]:
            if checkbox.isChecked():
                technologies.append(checkbox.text())

        result = (
            f"Language: {language}\n"
            f"Technologies: {', '.join(technologies) if technologies else 'None'}"
        )

        self.result_label.setText(result)

    # RESET SLOT

    def reset(self):

        # Clear radio button selection
        self.radio_group.setExclusive(False)

        for button in self.radio_group.buttons():
            button.setChecked(False)

        self.radio_group.setExclusive(True)

        # Uncheck all checkboxes
        for checkbox in [self.check1, self.check2, self.check3, self.check4]:
            checkbox.setChecked(False)

        self.result_label.setText("Your selections will appear here.")


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
