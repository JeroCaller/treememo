# 시작일 : 2023-04-10

# 모듈 간 임포트 관계를 파악해보는 작업도 필요할 것 같다.

import sys
import iconResources_rc
from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
from treeviewMemoUi import Ui_MainWindow
import embodyfunc as ef
import contextmenu as cm
import handledirectory as handir 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ORIGINAL_TITLE = "트리메모"
        self.setWindowTitle(self.ORIGINAL_TITLE)
        self.setWindowIcon(QtGui.QIcon(":/icon/icons/two_tree.jpg"))

        self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(["이름", "확장명"])
        self.root_tree_item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)

        # 외부 모듈에서 정의된 클래스의 인스턴스들을 변수에 할당
        self.hd = handir.HandleRootDir()
        self.getset = ef.GetSet()
        self.getset.setRootTreeWidget(self.ui.treeWidget)
        self.getset.setRootTreeItem(self.root_tree_item)
        self.uifunc = ef.EmbodyFunc(self, self.getset, self.hd)
        self.context_menu = cm.ContextMenuForTreeWidget(
            self,
            self.getset,
            self.hd
        )

        self.ui.textEdit.setAcceptRichText(True)

        # QSplitter 안에 놓인 위젯들의 크기 비율 설정.
        # 첫 번째 인자는 위젯의 인덱스, 두 번째 인자는 원하는 비율
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 3)

        # 해당 메서드를 통해 메인 윈도우가 확대되거나 축소될 때 위젯들도 같이 확대 또는 축소되도록 설정.
        self.setCentralWidget(self.ui.splitter)

        # 메뉴, 툴바 버튼 signal-slot 설정
        self.ui.actionAddRootFolder.triggered.connect(self.createNewRootDir)
        self.ui.actionOpenFolder.triggered.connect(self.openRootDir)
        self.ui.actionSave.triggered.connect(self.saveAllContentsInDir)
        self.ui.actionAddNewDoc.triggered.connect(self.createNewDocument)
        self.ui.actionReadMode.triggered.connect(self.switchReadMode)
        self.ui.actionEditMode.triggered.connect(self.switchEditMode)
        self.ui.actionAddImage.triggered.connect(self.addImage)
        self.ui.actionTooBarOnOff.triggered.connect(self.switchToolBar)
        self.ui.actionRefreshTree.triggered.connect(self.refreshTreeWidget)

        # 그 외 signal-slot 설정
        self.ui.textEdit.textChanged.connect(self.markNotSavedState)
        self.ui.treeWidget.itemDoubleClicked.connect(self.treeItemDoubleClicked)

    def createNewRootDir(self):
        self.ui.textEdit.setText('') # QTextEdit에 기존 텍스트가 있으면 지운다.
        is_true = self.uifunc.createNewRootDir()
        if not is_true: return
        self.refreshTreeWidget()
        
    def openRootDir(self):
        self.ui.textEdit.setText('')
        is_true = self.uifunc.openRootDir()
        if not is_true: return
        self.refreshTreeWidget()

    def saveAllContentsInDir(self):
        pass

    def createNewDocument(self):
        pass

    def switchReadMode(self):
        self.ui.textEdit.setReadOnly(True)
        self.ui.actionReadMode.setEnabled(False)
        self.ui.actionEditMode.setEnabled(True)

    def switchEditMode(self):
        # 루트 폴더를 가져오지 않은 상태에서는 쓰기 모드를 제한한다.
        if self.funcs.getRootDir() == '': return
        self.ui.textEdit.setReadOnly(False)
        self.ui.actionEditMode.setEnabled(False)
        self.ui.actionReadMode.setEnabled(True)

    def addImage(self):
        pass

    def switchToolBar(self):
        is_checked = self.ui.actionTooBarOnOff.isChecked()
        if is_checked: self.ui.toolBar.show()
        else: self.ui.toolBar.hide()

    def refreshTreeWidget(self):
        self.uifunc.removeAllTreeWidgets()
        self.uifunc.showTree()

    def markNotSavedState(self):
        """텍스트 내용 변경되고 사용자가 따로 저장 버튼을 누르지 않았다면,
        해당 텍스트 파일명 맨 뒤에 별표(*)를 덧붙여 해당 파일이 저장되지 않았음
        을 표시해준다."""
        pass

    def treeItemDoubleClicked(
            self,
            current_tree_item: QtWidgets.QTreeWidgetItem
        ):
        """사용자가 특정 텍스트 파일 선택 시 해당 파일 내 텍스트를
        QTextEdit 위젯에 보여준다."""
        self.getset.setCurrentTreeItem(current_tree_item)
        content = self.uifunc.getTextFromCurrentTreeItem()
        if content is None: return
        self.ui.textEdit.setText(content)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()