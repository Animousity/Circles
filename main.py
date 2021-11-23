import sys
import random

from UI import WindowSample
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Circles(QWidget, WindowSample):
    def __init__(self):
        super().__init__()
        self.circle = QLabel(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.createCircles)

    def createCircles(self):
        x = random.choice(range(850))
        y = random.choice(range(650))
        side = random.choice(range(650))
        self.circle.setGeometry(x, y, side, side)
        self.circle.setStyleSheet(f'border-radius: {side // 2}; background-color: rgb({random.choice(range(256))}, {random.choice(range(256))}, {random.choice(range(256))});')
        self.circle.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
