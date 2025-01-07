from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPen, QColor, QPainter
from PyQt5.QtCore import Qt

class DonutChartExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a Pie Series
        series = QPieSeries()
        series.append("A", 40)
        series.append("B", 30)
        series.append("C", 20)
        series.append("D", 10)

        # Customize slices
        for slice_ in series.slices():
            slice_.setLabelVisible(True)  # Display labels
            slice_.setExploded(True) if slice_.label() == "A" else slice_.setExploded(False)  # Highlight slice A
            slice_.setBrush(QColor(100, 100, 255, 200))  # Semi-transparent blue
            slice_.setPen(QPen(Qt.NoPen))  # No border for slices

        # Create a chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Donut Chart Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Adjust the pie hole size (to make it a donut chart)
        series.setHoleSize(0.5)

        # Make the chart background transparent
        chart.setBackgroundBrush(Qt.transparent)
        chart.setBackgroundPen(QPen(Qt.NoPen))
        chart.setPlotAreaBackgroundBrush(Qt.transparent)
        chart.setPlotAreaBackgroundVisible(False)

        # Create a ChartView
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set up the main window
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)
        layout.addWidget(chart_view)

        self.setCentralWidget(container)
        self.setWindowTitle("Donut Chart Example")

if __name__ == "__main__":
    app = QApplication([])
    window = DonutChartExample()
    window.resize(800, 600)
    window.show()
    app.exec_()
