from PySide6.QtWidgets import (QWidget, QSplitter, QFrame, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import (Qt, Slot)  # PySide6.QtCore.Qt.Orientation for QSplitter


class InteriorTabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.create_interior()
        self.create_left_frame()
        self.create_right_frame()
        self.create_bottom_frame()

    def create_interior(self):
        splitterV = QSplitter(Qt.Orientation.Vertical)
        splitterH = QSplitter(Qt.Orientation.Horizontal)

        self.left_frame = QFrame()
        self.left_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.right_frame = QFrame()
        self.right_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.bottom_frame = QFrame()
        self.bottom_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)

        splitterH.addWidget(self.left_frame)
        splitterH.addWidget(self.right_frame)
        splitterV.addWidget(splitterH)
        splitterV.addWidget(self.bottom_frame)

        splitterV.setSizes([300, 30])
        splitterH.setSizes([150, 500])

        layout = QGridLayout()
        layout.addWidget(splitterV)

        self.setLayout(layout)

    def create_left_frame(self):
        bttn_config = QPushButton("Config")
        bttn_config.clicked.connect(self.left_frame_bttn_config_signal)
        bttn_save = QPushButton("Save")
        bttn_save.clicked.connect(self.left_frame_bttn_save_signal)
        bttn_add = QPushButton("Add")
        bttn_add.clicked.connect(self.left_frame_bttn_add_signal)
        bttn_run = QPushButton("Run")
        bttn_run.clicked.connect(self.left_frame_bttn_run_signal)

        layout_bttn_v1 = QVBoxLayout()
        layout_bttn_v1.addStretch(1)
        layout_bttn_v1.addWidget(bttn_config)
        layout_bttn_v1.addWidget(bttn_save)

        layout_bttn_v2 = QVBoxLayout()
        layout_bttn_v2.addStretch(1)
        layout_bttn_v2.addWidget(bttn_add)
        layout_bttn_v2.addWidget(bttn_run)

        self.info_left_frame = QFrame()
        self.info_left_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        #scroll_area = self.info_left_frame.QScrollArea()
        ##############################################


        layout = QGridLayout()
        layout.rowStretch(1)
        layout.columnStretch(1)

        layout.addWidget(self.info_left_frame, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(layout_bttn_v1, 20, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addLayout(layout_bttn_v2, 20, 12, Qt.AlignmentFlag.AlignRight)

        self.left_frame.setLayout(layout)

    def left_frame_bttn_config_signal(self):
        print("left_frame_bttn_config_signal")

    def left_frame_bttn_save_signal(self):
        print("left_frame_bttn_save_signal")

    def left_frame_bttn_add_signal(self):
        print("left_frame_bttn_add_signal")

    def left_frame_bttn_run_signal(self):
        print("left_frame_bttn_run_signal")

    def create_right_frame(self):
        pass

    def create_bottom_frame(self):
        pass

