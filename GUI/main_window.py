from PySide2.QtWidgets import QMainWindow

from core.utils import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        load_ui("GUI/design/MainWindow.ui", self)
