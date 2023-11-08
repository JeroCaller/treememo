# 시작일 : 2023-04-10
# === 남은 과제 ===
# * 패키지 계층을 텍스트로 출력해주는 기능 테스트
# * QTextEdit.textChanged 시그널 발생 이유가 사용자가 텍스트를 조작해서인지
# 아니면 그저 파일로부터 읽어온 내용을 보여줄 때 발생한 것인지 판별하는 기능 구현하기
# * (가능하다면) MainWindow 클래스 내 모든 메서드들은 오로지 signal에 연결될 slot만을 남기고
# 그 외에 기능, 알고리즘 구현 메서드는 다른 클래스에서 따로 구현하기.

import sys
import os
import iconResources_rc as iconResources_rc
from PySide6 import QtWidgets
from PySide6 import QtGui
from treeviewMemoUi import Ui_MainWindow
from ver1.handledirectory import HandleDir, FileIO
from ver1.functions import EmbodyFunc

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ORIGINAL_TITLE = "트리메모"
        self.setWindowTitle(self.ORIGINAL_TITLE)
        self.setWindowIcon(QtGui.QIcon(":/icon/icons/two_tree.jpg"))

        self.handle_dir_obj = HandleDir()
        self.handle_file_io_obj = FileIO()
        self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(["이름", "확장명"])
        self.root_tree = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)

        # 트리 아이템들의 위치를 알기 쉽게 하기 위함.
        self.tree_index : dict[str, int] = {}  # item_text : index

        self.algorighms = EmbodyFunc(self)

        self.ui.textEdit.setAcceptRichText(True)
        self.switchReadMode()  # 맨 처음 실행 시에는 읽기 모드로.

        # QTextEdit.textChanged() 시그널이 발생된 이유가
        # 사용자가 텍스트를 조작해서가 아니라 파일로부터 
        # 내용을 읽어왔기 때문일 경우 True
        self.text_changed_because_read_from_file = True

        # QSplitter 안에 놓인 위젯들의 크기 비율 설정.
        # 첫 번째 인자는 위젯의 인덱스, 두 번째 인자는 원하는 비율
        self.ui.splitter.setStretchFactor(0, 1)
        self.ui.splitter.setStretchFactor(1, 3)

        # 해당 메서드를 통해 메인 윈도우가 확대되거나 축소될 때 위젯들도 같이 확대 또는 축소되도록 설정.
        self.setCentralWidget(self.ui.splitter)

        # 메뉴, 툴바 버튼 signal-slot 설정
        self.ui.actionAddRootFolder.triggered.connect(self.createNewDir)
        self.ui.actionOpenFolder.triggered.connect(self.openDir)
        self.ui.actionSave.triggered.connect(self.saveAllContentsInDir)
        self.ui.actionAddNewDoc.triggered.connect(self.createNewDocument)
        self.ui.actionReadMode.triggered.connect(self.switchReadMode)
        self.ui.actionEditMode.triggered.connect(self.switchEditMode)
        self.ui.actionAddImage.triggered.connect(self.addImage)
        self.ui.actionTooBarOnOff.triggered.connect(self.switchToolBar)
        self.ui.actionRefreshTree.triggered.connect(self.refreshTreeWidget)

        # 그 외 signal-slot 설정
        self.ui.textEdit.textChanged.connect(self.NotSavedState)
        self.ui.treeWidget.itemDoubleClicked.connect(self.treeItemDoubleClicked)

    def createNewDir(self):
        dir_dialog = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "새 폴더를 추가할 경로 선택"
        )
        if dir_dialog == "":
            return
        self.handle_dir_obj.setDir(dir_dialog)

        while True:
            root_dir_name, ok = QtWidgets.QInputDialog.getText(
                self, "루트 폴더 이름 입력", "루트 폴더 이름을 입력하세요.", text="root"
            )
            if not ok:
                self.handle_dir_obj.setDir("")
                break  # 사용자가 취소를 누름. 루트 폴더 생성 취소
            elif root_dir_name == "":
                # 사용자가 이름을 아무것도 입력하지 않을 경우 다시 입력하도록 함
                QtWidgets.QMessageBox.critical(
                        self, "정보", "이름을 입력해야 합니다."
                        )
                continue
            else:
                self.handle_dir_obj.addSubDir(root_dir_name)
                message = "이미 같은 이름의 폴더가 있습니다. 다른 이름을 입력하세요."
                is_ok = self.handle_dir_obj.tryMakeDir(message=message)
                if is_ok:
                    break
                else:
                    self.handle_dir_obj.setDir(dir_dialog)
        self.removeAllTreeWidgets()
        self.showTree()

    def openDir(self):
        dir_dialog = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "가져올 폴더 선택"
        )
        if dir_dialog == "":
            return
        self.removeAllTreeWidgets()
        self.handle_dir_obj.setDir(dir_dialog)
        self.showTree()
        self.printAllTreeWidgetItems()

    def saveAllContentsInDir(self):
        self.SavedState()
        pass

    def createNewDocument(self):
        pass

    def switchReadMode(self):
        self.ui.textEdit.setReadOnly(True)
        self.ui.actionReadMode.setEnabled(False)
        self.ui.actionEditMode.setEnabled(True)

    def switchEditMode(self):
        self.ui.textEdit.setReadOnly(False)
        self.ui.actionEditMode.setEnabled(False)
        self.ui.actionReadMode.setEnabled(True)

    def addImage(self):
        pass

    def switchToolBar(self):
        pass

    def showTree(self):
        """루트 폴더 내 모든 폴더 및 파일들을 트리뷰 형태로 보여줌"""
        if self.handle_dir_obj.getDir() == '':
            return
        root_path = self.handle_dir_obj.getDir()
        root_name = root_path.split('\\')[-1]
        self.root_tree.setText(0, root_name)

        def setTree(root_path: str, parent_tree: QtWidgets.QTreeWidgetItem):
            base = os.path.basename(root_path)
            file_and_ext = base.rsplit('.', 1)
            if len(file_and_ext) == 2:
                item = QtWidgets.QTreeWidgetItem(parent_tree, [file_and_ext[0], file_and_ext[1]])
            else:
                item = QtWidgets.QTreeWidgetItem(parent_tree, [file_and_ext[0]])
            if os.path.isdir(root_path):
                for file_or_dir in os.listdir(root_path):
                    full_path = os.path.join(root_path, file_or_dir)
                    setTree(full_path, item)

        setTree(root_path, self.root_tree)

        self.ui.treeWidget.addTopLevelItem(self.root_tree)
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.show()
        self.ui.treeWidget.expandAll()

    def removeAllTreeWidgets(self):
        if self.root_tree.childCount() == 0:
            return
        self.root_tree.takeChildren()

    def printAllTreeWidgetItems(self):
        """모든 자식 아이템 출력.
        테스트용."""
        if self.root_tree.childCount() == 0:
            print("자식 트리 위젯 아이템 없음")
            return
        for i in range(self.root_tree.childCount()):
            child = self.root_tree.child(i)
            print(child.text(0), child.text(1))

    def treeItemDoubleClicked(self, tree_item_obj):
        """사용자가 트리 위젯에서 아이템 하나를 더블클릭했을 때
        해당 파일 내용을 텍스트 위젯에 띄움."""
        selected_file_path = tree_item_obj.text(0) + "." + tree_item_obj.text(1)
        full_path = self.handle_dir_obj.getPathOfSelectedFile(tree_item_obj, selected_file_path)
        if os.path.isdir(full_path):
            return
        self.handle_file_io_obj.setDir(full_path)
        data = self.handle_file_io_obj.readFromFile()
        self.text_changed_because_read_from_file = True
        self.ui.textEdit.setText(data)

    def refreshTreeWidget(self):
        """트리 위젯 새로고침"""
        self.removeAllTreeWidgets()
        self.showTree()

    def NotSavedState(self):
        if self.text_changed_because_read_from_file:
            self.text_changed_because_read_from_file = False
            return
        self.setWindowTitle(self.ORIGINAL_TITLE + "*")

    def SavedState(self):
        self.setWindowTitle(self.ORIGINAL_TITLE)

    def assignTreeIndex(self):
        """특정 트리 아이템 위젯의 수월한 인덱싱을 위해 
        각 인덱스에 텍스트를 붙임"""
        pass
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()