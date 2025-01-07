if len(data) == 1:
        #     self.bar_set = QBarSet("Values")
        #     self.bar_set.append([10,])  # Example data

        # # Create a QBarSeries and add the QBarSet
        #     self.bar_series = QBarSeries()
        #     self.bar_series.append(self.bar_set)

        # # Create a QChart and add the QBarSeries
        #     self.chart = QChart()
        #     self.chart.addSeries(self.bar_series)
        #     self.chart.setTitle("Simple Bar Chart")
        #     self.chart.setAnimationOptions(QChart.SeriesAnimations)

        # # Customize axes
        #     self.categories = ["Value"]  # Example categories
        #     self.axisX = QBarCategoryAxis()
        #     self.axisX.append(self.categories)
        #     self.chart.addAxis(self.axisX, Qt.AlignBottom)
        #     self.bar_series.attachAxis(self.axisX)

        #     self.axisY = QValueAxis()
        #     self.axisY.setRange(0, 60)  # Set Y-axis range
        #     self.chart.addAxis(self.axisY, Qt.AlignLeft)
        #     self.bar_series.attachAxis(self.axisY)
        #     self.chart_view = QChartView(self.chart)
        #     self.ui.verticalLayout_14.addWidget(self.chart_view)
        #     self.chart_view.setRenderHint(QPainter.Antialiasing)
        #     return