from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QDialog,
                               QVBoxLayout, QToolBar, QStatusBar )
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import (QAction, QKeySequence, QScreen )
from MainTabWidget import MainTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data analyzer")
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setGeometry(0, 0, 3*screen_size.width()//4, 3*screen_size.height()//4)

        #geometry = self.screen().availableGeometry()
        #self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)
        #self.showMaximized()
        #self.centralwidget = QWidget(self)
        #self.setCentralWidget(self.centralwidget)

        self.menu=self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.tools_menu = self.menu.addMenu("Tools")
        self.help_menu = self.menu.addMenu("Help")

        self.main_tab_widget = MainTabWidget()
        tab_name="undefined"

        self.main_tab_widget.create_tabs(tab_name)
        #self.main_tab_widget.create_tabs("Project-2")
        #self.main_tab_widget.create_tabs("BIO-Project")

        self.setCentralWidget(self.main_tab_widget)

        self.status_bar.showMessage("Ready to enjoy of data analytics...")


