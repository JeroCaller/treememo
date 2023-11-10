"""
2023-11-10 재시작.
"""

import sys

from PySide6.QtWidgets import (QApplication, QMainWindow)

from uifiles.main_ui import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._additionalUiSet()

        self.show()

    def _additionalUiSet(self):
        # splitter 내의 두 위젯 간 너비 비율 설정.
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 3)

        self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(['파일명', '확장자'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()