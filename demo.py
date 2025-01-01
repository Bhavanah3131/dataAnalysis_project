from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create a QTableWidget
        table = QTableWidget(4, 3)  # 4 rows, 3 columns
        table.setHorizontalHeaderLabels(["ID", "Name", "Age"])
        
        # Populate the table
        data = [
            (1, "Alice", 25),
            (2, "Bob", 30),
            (3, "Charlie", 35),
            (4, "Diana", 28)
        ]
        for row, (id_, name, age) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(str(id_)))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(str(age)))
        
        # Apply stylesheet for borderless table with transparent background
        table.setStyleSheet("""
            @font-face {
                font-family: "CustomFont";
                src: url("https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Me5Q.ttf");
            }

            QTableWidget {
                background: transparent;  /* Transparent background */
                border: none;  /* No border */
                gridline-color: #444444;  /* Gridline color */
                color: white;  /* Text color */
                font-family: "CustomFont";  /* Custom font */
                font-size: 14px;  /* Font size */
            }

            QHeaderView {
                background-color: #333333;
                border: none;  /* No border */
                color: white;
                font-family: "CustomFont";  /* Custom font */
                font-size: 16px;
            }

            QHeaderView::section {
                background-color: #333333;
                border: none;  /* No border */
                padding: 5px;
                color: white;
            }

            QHeaderView::section:first {
                border-top-left-radius: 15px;  /* Rounded top-left corner */
            }

            QHeaderView::section:last {
                border-top-right-radius: 15px;  /* Rounded top-right corner */
            }

            QTableCornerButton::section {
                background-color: #333333;
                border-top-left-radius: 15px;
            }

            QTableWidget::item {
                color: white;
                font-family: "CustomFont";
                font-size: 14px;
                padding: 5px;
            }

            QTableWidget::item:selected {
                background-color: #3a3a3a;  /* Selected item background */
                color: white;
            }
        """)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
