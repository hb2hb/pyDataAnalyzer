from PySide6.QtWidgets import (QWidget, QTabWidget, QSplitter, QFrame, QGridLayout, QHBoxLayout)
from InteriorTabWidget import InteriorTabWidget
###

class MainTabWidget(QTabWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.tabs={}

    def create_tabs(self, tab_name: str):
        if tab_name in self.tabs:
            return None

        self.tabs[tab_name] = InteriorTabWidget()
        self.addTab(self.tabs[tab_name], tab_name)

        return self.tabs[tab_name]

    def get_tabs(self):
        return self.tabs

    def get_tab(self, tab_name: str):
        return self.tabs[tab_name]

