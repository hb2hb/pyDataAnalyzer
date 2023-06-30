import sys
##import PySide6
from PySide6.QtWidgets import (QApplication)
from MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication()
    mw = MainWindow()
    mw.show()

    sys.exit(app.exec())

