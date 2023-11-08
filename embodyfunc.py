import os
from PySide6 import QtWidgets
from ver2.handledirectory import HandleDir, FileIO

def setTree(root_path: str, parent_tree: QtWidgets.QTreeWidgetItem):
    """루트 디렉토리 경로로부터 모든 하위 디렉토리 및 파일들을
    트리 위젯에 보이도록 설정한다."""
    base = os.path.basename(root_path)
    file_and_ext = base.rsplit('.', 1)
    if len(file_and_ext) == 2:
        item = QtWidgets.QTreeWidgetItem(
            parent_tree, [file_and_ext[0], file_and_ext[1]])
    else:
        item = QtWidgets.QTreeWidgetItem(parent_tree, [file_and_ext[0]])
    if os.path.isdir(root_path):
        for file_or_dir in os.listdir(root_path):
            full_path = os.path.join(root_path, file_or_dir)
            setTree(full_path, item)


class GetSetWidgets():
    """Pyside 몇몇 위젯들을 설정하거나 리턴하는 getset기이다."""
    def __init__(self):
        self.root_tree_item: QtWidgets.QTreeWidgetItem
        self.qtreewidget: QtWidgets.QTreeWidget
        self.tree_item: QtWidgets.QTreeWidgetItem

    def setRootTree(self, new_root_tree: QtWidgets.QTreeWidgetItem):
        self.root_tree_item = new_root_tree

    def getRootTree(self) -> QtWidgets.QTreeWidgetItem:
        return self.root_tree_item
    
    def setTreeWidget(self, new_tree_widget: QtWidgets.QTreeWidget):
        self.qtreewidget = new_tree_widget

    def getTreeWidget(self) -> QtWidgets.QTreeWidget:
        return self.qtreewidget
    
    def setTreeItem(self, new_tree_item: QtWidgets.QTreeWidgetItem):
        self.tree_item = new_tree_item

    def getTreeItem(self) -> QtWidgets.QTreeWidgetItem:
        return self.tree_item


class EmBodyFunc():
    """ui 부문을 제외한 데이터 처리, 기능 구현 등의 작업을 위한 클래스"""
    def __init__(
            self,
            main_win : QtWidgets.QMainWindow = None,
            getset_obj : GetSetWidgets = None
        ):
        self.main_win = main_win
        self.getset = getset_obj
        self.hd = HandleDir(main_win=main_win)
        self.fio = FileIO()

    def getRootDir(self) -> str:
        """현재 루트 폴더 경로명 반환."""
        return self.hd.getDir()

    def createNewRootDir(self):
        root_dir = self.hd.askAndGetDir("새 폴더를 추가할 경로 선택")

        # 사용자가 QFileDialog에서 취소를 누른 경우.
        # 그냥 QFileDialog 창을 닫고 아무런 행동을 하지 않는다.
        if root_dir == '': return
        else: self.hd.setDir(root_dir)

        while True:
            root_dir_name, ok = QtWidgets.QInputDialog.getText(
                self.main_win, 
                "루트 폴더 이름 입력", 
                "루트 폴더 이름을 입력하세요.", 
                text="root"
            )
            if not ok:
                # 사용자가 취소를 누름. 루트 폴더 생성 취소
                self.hd.setDir("")
                break
            elif root_dir_name == "":
                # 사용자가 이름을 아무것도 입력하지 않을 경우 다시 입력하도록 함
                QtWidgets.QMessageBox.critical(
                        self.main_win, "정보", "이름을 입력해야 합니다."
                        )
                continue
            else:
                self.hd.addSubDir(root_dir_name)
                message = "이미 같은 이름의 폴더가 있습니다. 다른 이름을 입력하세요."
                is_ok = self.hd.tryMakeDir(message=message)
                if is_ok: break
                else: 
                    self.hd.setDir(root_dir)
                    os.chdir(self.hd.getDir())

    def getOpenRootDir(self):
        """사용자가 열 폴더 선택 시 해당 루트 폴더 경로를 설정"""
        root_dir = self.hd.askAndGetDir("가져올 폴더 선택")

        # 사용자가 QFileDialog에서 취소를 누른 경우.
        # 그냥 QFileDialog 창을 닫고 아무런 행동을 하지 않는다.
        if root_dir == '': return
        self.hd.setDir(root_dir)
        os.chdir(self.hd.getDir())
                
    def removeAllTreeWidgets(self):
        """트리 위젯에 있는 모든 트리 위젯 아이템 삭제.
        사용자 눈에는 빈 트리 위젯만 보이도록 한다."""
        root_tree = self.getset.getRootTree()
        if root_tree.childCount() == 0:
            return
        root_tree.takeChildren()
        self.getset.setRootTree(root_tree)

    def showTree(self):
        """사용자가 선택한 루트 폴더 내 모든 폴더 및 파일들을
        계층에 따라 트리 형식으로 보여준다."""
        if self.hd.getDir() == "": return
        root_path = self.hd.getDir()
        root_tree = self.getset.getRootTree()
        root_tree.setText(0, root_path)
        setTree(root_path, root_tree)
        tree_widget = self.getset.getTreeWidget()
        tree_widget.addTopLevelItem(root_tree)
        tree_widget.resizeColumnToContents(0)
        tree_widget.show()
        tree_widget.expandAll()  # 트리 내 모든 하위 폴더 및 파일들을 펼쳐 보여줌.

    def refreshTreeWidget(self):
        """트리 위젯 새로 고침"""
        self.removeAllTreeWidgets()
        self.showTree()

    def getTextFromSelectedTreeItem(self) -> str:
        """사용자가 특정 텍스트 파일 선택 시 이를 
        QTextEdit 위젯에 띄울 수 있도록 해당 파일 텍스트 반환."""
        tree_item = self.getset.getTreeItem()
        if self.hd.isDir(tree_item.text(0)): return ''
        selected_file_path = tree_item.text(0) + "." + tree_item.text(1)
        full_path = self.hd.getPathOfSelectedFile(
            tree_item,
            selected_file_path
        )
        self.fio.setPath(full_path)
        try:
            data = self.fio.readFromFile()
            return data
        except FileNotFoundError: pass  # 에러 무시
    

class EmbodyFuncInContextTree(EmBodyFunc):
    """트리 위젯의 컨텍스트 메뉴 전용"""
    def __init__(
            self,
            main_win : QtWidgets.QMainWindow = None,
            getset_obj : GetSetWidgets = None,
        ):
        super().__init__(main_win=main_win, getset_obj=getset_obj)
        self.tree_widget = self.getset.getTreeWidget()

    def createNewFile(self):
        """사용자가 트리 위젯 아이템들 중 
        선택한 파일이 포함된 상위 폴더의 절대경로에 새 파일 생성."""
        tree_widget = self.getset.getTreeWidget()
        base_name = tree_widget.currentItem().text(0)
        extension = tree_widget.currentItem().text(1)
        if extension != '':
            # 폴더가 아닌 파일임. 반드시 폴더로 지정.
            base_name = tree_widget.currentItem().parent().text(0)
        full_path = os.path.abspath(base_name)
        self.fio.setPath(full_path)
        is_error = self.fio.createNewFile()
        if is_error is not None:
            print("===에러===")
            print(is_error)
            print('=========')
            temp = QtWidgets.QMessageBox.critical(
                self.main_win,
                "에러",
                "에러: 문제가 생겨 새 파일을 생성할 수 없습니다."
            )
            return