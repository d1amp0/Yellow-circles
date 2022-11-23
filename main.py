import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        uic.loadUi('UI.ui', self)
        self.first = False
        self.btnDraw.clicked.connect(self.redo)

    def redo(self):
        self.first = True
        self.repaint()

    def paintEvent(self, event):
        if self.first:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            w = randint(0, 250)
            qp.drawEllipse(randint(0, 500 - w // 2), randint(0, 500 - w // 2), w, w)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())