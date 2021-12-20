import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.btn.clicked.connect(self.paint)
        self.paint = False

    def paint(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setPen(QColor(255, 255, 0))
        for i in range(20):
            radius = randrange(5, 150)
            pos = randrange(radius, self.width() - radius), randrange(radius, self.height() - radius)
            qp.drawArc(*pos, radius, radius, 0, 5760)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())