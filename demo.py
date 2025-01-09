from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel, QMessageBox

class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Example")
        self.setGeometry(100, 100, 600, 400)

        # Create buttons to open the file dialogs
        self.button1 = QPushButton("Recent Date File")
        self.button1.clicked.connect(lambda: self.open_file_dialog(1))

        self.button2 = QPushButton("Previos Date File")
        self.button2.clicked.connect(lambda: self.open_file_dialog(2))

        # Labels to display selected file paths
        self.label1 = QLabel("Selected File 1: None")
        self.label2 = QLabel("Selected File 2: None")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.label1)
        layout.addWidget(self.button2)
        layout.addWidget(self.label2)

        # Set the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file_dialog(self, button_id):
        while True:
            # Open the file dialog
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly  # Open in read-only mode
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "All Files (*);;Text Files (*.txt)", options=options)

            # If a file was selected, show a confirmation message box
            if file_path:
                reply = QMessageBox.question(self, 'Confirmation', f"Are you sure you want to select this file?\n{file_path}", 
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if button_id == 1:
                        self.label1.setText(f"Selected File 1: {file_path}")
                    elif button_id == 2:
                        self.label2.setText(f"Selected File 2: {file_path}")
                    break  # Exit the loop if the user confirms the selection

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FileDialogExample()
    window.show()
    sys.exit(app.exec_())
