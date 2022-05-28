# Weather UI
# * Only UI, contains no logic
# * Uses Qt

import sys
from main import *
from PySide6 import QtCore, QtWidgets, QtGui

class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.currentWeather= QtWidgets.QLabel("Weather: " + getWeather())
        self.futureWeather = QtWidgets.QLabel("Tomorrow: " + futureWeather())
        self.location = QtWidgets.QLabel(data['city'] + ', ' + data['country'])

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.currentWeather)
        self.layout.addWidget(self.futureWeather)
        self.layout.addWidget(self.location)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainView()
    widget.resize(200, 100)
    widget.show()

    sys.exit(app.exec())