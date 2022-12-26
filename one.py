import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 600)
    w.move(300, 600)
    w.setWindowTitle("first one ")
    w.show()
    sys.exit(app.exec_())
    