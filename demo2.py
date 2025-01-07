from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel, QMessageBox
from main import MainWindow
from windows.selectfile_ui import *
class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        self.ui.pushButton.clicked.connect(lambda: self.open_file_dialog(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.open_file_dialog(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.process_data())

    def open_file_dialog(self, button_id):
        while True:
            # Open the file dialog
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly  # Open in read-only mode
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "All Files (*);;Text Files (*.txt)", options=options)

            # If a file was selected, show a confirmation message box
            if file_path:
                reply = QMessageBox.question(self, 'Confirmation', f"Are you sure you want to select this file?\n{file_path}", 
                                             QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    if button_id == 1:
                        self.ui.label.setText(f"{file_path}")
                    elif button_id == 2:
                        self.ui.label_2.setText(f"{file_path}")
                    break  # Exit the loop if the user confirms the selection
                else:
                    QMessageBox.information(self, 'No File Selected', 'No files were selected.')
                    break  # Exit the loop if the user declines the selection
    def process_data(self):
        print(self.ui.label.text())
        self.hide()
        window = MainWindow()
        window.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FileDialogExample()
    window.show()
    sys.exit(app.exec_())
