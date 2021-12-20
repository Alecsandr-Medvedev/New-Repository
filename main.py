import sys
from random import randrange
from untitled import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
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
        for i in range(20):
            qp.setPen(QColor(randrange(255), randrange(255), randrange(255)))
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