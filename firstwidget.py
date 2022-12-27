import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin, self).__init__(parent)

        self.setWindowTitle("第一个窗口程序")
        self.resize(500,500)
        self.status = self.statusBar()
        self.status.showMessage('只存在十秒',10000)
if __name__== '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('C:\zxcc\工作\南京智隐\QT学习\Icon_.png'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec())
