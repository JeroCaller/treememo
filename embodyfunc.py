import os
from PySide6 import QtWidgets
from PySide6 import QtCore
import handledirectory as handledir
import mysomefuncs as msf
import usererror as userr


def getAbsPathOfFile(
        tree_item: QtWidgets.QTreeWidgetItem, 
        path: str='',
        root_dir_path: str=''
        ) -> str:
    """사용자가 선택한 트리 위젯의 파일 또는 폴더의
    루트 경로를 제외한 전체 경로를 반환."""
    if tree_item.parent() is None:
        # 이미 최상위 트리 위젯 아이템인 경우, 루트 절대경로의 basename 리턴.
        return os.path.basename(root_dir_path)
    if tree_item.parent().text(0) == root_dir_path:
        return path
    path = tree_item.parent().text(0) + '/' + path
    return getAbsPathOfFile(tree_item.parent(), path, root_dir_path)


def findTreeItem(
        tree_widget: QtWidgets.QTreeWidget, 
        target_text: str
        ):
    """찾고자 하는 텍스트가 있는 트리 위젯 아이템을 찾아준다."""
    match_condition = QtCore.Qt.MatchRecursive | QtCore.Qt.MatchExactly
    result = tree_widget.findItems(target_text, match_condition, 0)
    return result


class GetSet():
    """여러 위젯들을 설정 또는 반환하기 위한 getset기이다."""
    def __init__(
            self,
            root_tree_item: QtWidgets.QTreeWidgetItem = None,
            root_tree_widget: QtWidgets.QTreeWidget = None,
            current_tree_item: QtWidgets.QTreeWidgetItem = None
            ):
        self.root_tree_item = root_tree_item
        self.root_tree_widget = root_tree_widget
        self.current_tree_item = current_tree_item

    def getRootTreeItem(self) -> QtWidgets.QTreeWidgetItem:
        userr.QtWidgetNoneError().setTryExcept(
            self.root_tree_item,
            GetSet.getRootTreeItem.__name__
            )
        return self.root_tree_item
    
    def setRootTreeItem(
            self, 
            new_root_tree_item: QtWidgets.QTreeWidgetItem
            ):
        self.root_tree_item = new_root_tree_item

    def getRootTreeWidget(self) -> QtWidgets.QTreeWidget: 
        userr.QtWidgetNoneError().setTryExcept(
            self.root_tree_item,
            GetSet.getRootTreeWidget.__name__
            )
        return self.root_tree_widget
    
    def setRootTreeWidget(
            self,
            new_root_tree_widget: QtWidgets.QTreeWidget
            ):
        self.root_tree_widget = new_root_tree_widget

    def getCurrentTreeItem(self) -> QtWidgets.QTreeWidgetItem:
        userr.QtWidgetNoneError().setTryExcept(
            self.root_tree_item,
            GetSet.getCurrentTreeItem.__name__
            )
        return self.current_tree_item
    
    def setCurrentTreeItem(
            self, 
            new_current_tree_item: QtWidgets.QTreeWidgetItem
            ):
        self.current_tree_item = new_current_tree_item


class EmbodyFunc():
    """ui을 이루는 위젯을 구현하는 복잡한 알고리즘 구현"""
    def __init__(
            self,
            main_win = None,
            getset_obj: GetSet = None,
            handle_dir_obj: handledir.HandleRootDir = None
            ):
        """main_win: MainWindow"""
        self.main_win = main_win
        self.getset = getset_obj
        self.hd = handle_dir_obj
        self.fio = handledir.FileIO()

    def setRootDir(self, new_dir:str): self.hd.setRootDir(new_dir)

    def createNewRootDir(self) -> bool:
        """True: 수행 성공.
        False: 사용자가 중간에 수행을 취소함."""
        dir_dialog = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_win,
            caption="새 폴더를 추가할 경로 선택"
        )

        # 사용자가 QFileDialog에서 취소를 누른 경우.
        # 그냥 QFileDialog 창을 닫고 아무런 행동을 하지 않는다.
        if dir_dialog == '': return False

        while True:
            root_dir_name, ok = QtWidgets.QInputDialog.getText(
                self.main_win, 
                "루트 폴더 이름 입력", 
                "루트 폴더 이름을 입력하세요.", 
                text="root"
            )
            if not ok: return False # 사용자가 취소를 누름. 루트 폴더 생성 취소
            elif root_dir_name == "":
                # 사용자가 이름을 아무것도 입력하지 않을 경우 다시 입력하도록 함
                QtWidgets.QMessageBox.critical(
                        self.main_win, "정보", "이름을 입력해야 합니다."
                        )
                continue
            else:
                self.hd.setRootDir(dir_dialog)
                self.hd.addSubDir(root_dir_name)
                is_error = self.hd.tryMakeRootDir()
                if is_error is not None: 
                    # 기존 디렉토리 존재 시 다른 이름을 입력하도록 권고.
                    QtWidgets.QMessageBox.critical(self.main_win, "정보", is_error)
                    continue
                return True

    def openRootDir(self) -> bool:
        """True: 성공적으로 수행.
        False: 사용자가 중간에 수행 취소."""
        dir_dialog = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_win,
            caption="폴더 열기"
        )
        if dir_dialog == '': return False
        self.hd.setRootDir(dir_dialog)
        return True
        
    def showTree(self):
        """현재 선택된 루트 디렉토리 내의 전체 파일 또는 폴더들을
        계층을 구분하여 트리 위젯에 보여줌."""
        def setTree(
            root_path: str,
            super_tree_item: QtWidgets.QTreeWidgetItem
            ):
            """루트 디렉토리 경로로부터 모든 하위 디렉토리 및 파일들을
            트리 위젯에 보이도록 설정한다."""
            base = os.path.basename(root_path)
            file_name, ext = os.path.splitext(base)
            tree_item = QtWidgets.QTreeWidgetItem(super_tree_item)
            tree_item.setText(0, file_name)
            tree_item.setText(1, ext)
            if os.path.isdir(root_path):
                for file_or_dir in os.listdir(root_path):
                    full_path = os.path.join(root_path, file_or_dir)
                    setTree(full_path, tree_item)

        root_dir_path = self.hd.getRootDir()
        root_tree_item = self.getset.getRootTreeItem()
        root_tree_item.setText(0, root_dir_path)
        setTree(root_dir_path, root_tree_item)
        tree_widget = self.getset.getRootTreeWidget()
        tree_widget.addTopLevelItem(root_tree_item)
        tree_widget.resizeColumnToContents(0)
        tree_widget.show()
        tree_widget.expandAll()  # 트리 내 모든 하위 폴더 및 파일들을 펼쳐 보여줌.
    
    def removeAllTreeWidgets(self):
        """트리 위젯에 있는 모든 트리 위젯 아이템 삭제.
        사용자 눈에는 빈 트리 위젯만 보이도록 한다."""
        root_tree_item = self.getset.getRootTreeItem()
        if root_tree_item.childCount() == 0:
            return
        root_tree_item.takeChildren()
        self.getset.setRootTreeItem(root_tree_item)

    def getTextFromCurrentTreeItem(self) -> str | None:
        """사용자가 트리 위젯 아이템 중 하나를 더블클릭 시 
        해당 텍스트 파일 내용을 문자열로 반환.
        사용자가 폴더 클릭 시 None 반환하여 아무 작업 실행하지 않도록 함."""
        current_tree_item = self.getset.getCurrentTreeItem()
        if current_tree_item.text(1) == '':
            # 폴더인 경우. 무시한다.
            return None
        file_name = current_tree_item.text(0) + current_tree_item.text(1)
        root_dir_name = os.path.dirname(self.hd.getRootDir())
        file_basename = getAbsPathOfFile(
            current_tree_item, file_name, self.hd.getRootDir()
        )
        file_abspath = root_dir_name + '/' + file_basename
        print('file_abspath: ', file_abspath)  # 테스트용.
        self.fio.setTargetDir(file_abspath)
        content = self.fio.readTextFile()
        return content


class EmbodyFuncInContextTree(EmbodyFunc):
    def __init__(
            self,
            main_win = None,
            getset_obj: GetSet = None,
            handle_dir_obj: handledir.HandleRootDir = None
            ):
        """main_win: MainWindow"""
        super().__init__(
            main_win=main_win, 
            getset_obj=getset_obj,
            handle_dir_obj=handle_dir_obj
        )

    def createNewTxtFile(self):
        """사용자가 트리 위젯에서 마우스 우클릭한 곳과 가장 가까운 폴더에
        새 텍스트 파일을 생성한다."""
        current_tree_item = self.getset.getCurrentTreeItem()
        if current_tree_item.text(1) != '':
            # 파일이 아닌 폴더가 대상이어야 함.
            current_tree_item = current_tree_item.parent()
        current_folder_name = current_tree_item.text(0)
        current_folder_path = os.path.dirname(self.hd.getRootDir()) \
        + '/' +  getAbsPathOfFile(
            current_tree_item, 
            current_folder_name, 
            self.hd.getRootDir()
            )
        print("current_folder_path: ", current_folder_path)
        current_time_str = msf.TimeForFileName().currentTimeForFileName()
        text_file_name = '새 텍스트 ' + current_time_str + '.txt'
        target_path = current_folder_path + '/' + text_file_name
        self.fio.setTargetDir(target_path)
        self.fio.makeTextFile()

    def changeNewName(self):
        """사용자가 파일 또는 폴더 이름을 바꿀 수 있도록 하고, 
        사용자로부터 새로 입력받은 이름을 바로 파일 또는 폴더명에 적용한다."""
        while True:
            new_name, ok = QtWidgets.QInputDialog.getText(
                    self.main_win, 
                    "새 이름 입력", 
                    "새 이름을 입력하세요."
                )
            if not ok: return  # 사용자가 입력을 취소함.
            elif new_name == '':
                # 사용자가 이름을 아무것도 입력하지 않을 경우 다시 입력하도록 함
                QtWidgets.QMessageBox.critical(
                        self.main_win, "정보", "이름을 입력해야 합니다."
                        )
                continue
            find_tree_items_with_same_text = findTreeItem(
                self.getset.getRootTreeWidget(),
                new_name
            )
            for one_tree_item in find_tree_items_with_same_text:
                if one_tree_item.text(0) == new_name:
                    message = "루트 폴더 내 계층, 또는 폴더나 파일 상관없이 이름의 중복을 허용하지 않습니다."
                    QtWidgets.QMessageBox.critical(
                        self.main_win, "정보", message
                        )
                    new_name += msf.TimeForFileName().currentTimeForFileName()
                    break
            break 
        current_tree_item = self.getset.getCurrentTreeItem()
        current_file_or_dir_name = current_tree_item.text(0) + current_tree_item.text(1)
        current_path = getAbsPathOfFile(
            current_tree_item,
            current_file_or_dir_name,
            self.hd.getRootDir()
        )
        current_path = os.path.join(os.path.dirname(self.hd.getRootDir()), current_path)
        ...

        #current_tree_item.setText(0, new_name)
        # 실제 해당 파일 또는 폴더의 이름을 바꿔주는 코드 작성 필요.
        


if __name__ == '__main__':
    getset_obj = GetSet()
    print(getset_obj.getRootTreeItem())