from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
import embodyfunc as ef


class ContextMenuForTreeWidget():
    """오로지 트리 위젯 위에서만 트리 위젯과 관련된 컨텍스트 메뉴가 뜨게 한다."""
    def __init__(
            self,
            main_win = None,
            getset_obj = None,
            handle_dir_obj = None
        ):
        """main_win: MainWindow
        getset_obj: ef.GetSet
        handle_dir_obj: handledirectory.HandleRootDir"""
        
        self.main_win = main_win
        self.getset = getset_obj
        self.hd = handle_dir_obj

        self.tree_widget = self.getset.getRootTreeWidget()
        #self.tree_widget = root_tree_widget
        self.tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_widget.customContextMenuRequested.connect(self.showContextMenu)

        self.root_tree_item = self.getset.getRootTreeItem()

        #self.cont_getset = ef.GetSet()
        #self.cont_getset.setRootTreeWidget(self.tree_widget)
        #self.cont_getset.setRootTreeItem(root_tree_item)
        self.context_funcs = ef.EmbodyFuncInContextTree(
            main_win=main_win,
            getset_obj=self.getset,
            handle_dir_obj=self.hd
        )

    def showContextMenu(self, pos: QtCore.QPoint):
        context = QtWidgets.QMenu(self.tree_widget)

        action_create_new_txt = QtGui.QAction("새 텍스트 파일 생성", self.tree_widget)
        context.addAction(action_create_new_txt)

        action_delete_txt = QtGui.QAction("선택된 텍스트 파일 삭제", self.tree_widget)
        context.addAction(action_delete_txt)
        context.addSeparator()

        action_create_new_dir = QtGui.QAction("새 하위 폴더 생성", self.tree_widget)
        context.addAction(action_create_new_dir)

        action_delete_dir = QtGui.QAction("선택된 하위 폴더 삭제")
        context.addAction(action_delete_dir)
        context.addSeparator()

        action_change_new_name = QtGui.QAction("새 이름", self.tree_widget)
        context.addAction(action_change_new_name)

        # 처음 앱 실행 시 트리 위젯에 아무것도 없는 경우,
        # 모든 컨텍스트 메뉴들을 선택 불가능한 상태로 만든다.
        if self.tree_widget.topLevelItem(0).text(0) == '': context.setEnabled(False)
        else: context.setEnabled(True)

        # 처음 앱 실행이라 트리 위젯에 아무것도 없거나,
        # 기존의 파일 또는 디렉토리를 삭제하여 현재 선택된 트리 위젯 아이템
        # 이 없는 경우에는 slot 메서드들이 실행되지 않도록 방지.
        self.current_item = self.tree_widget.currentItem()
        if self.current_item is not None and len(self.current_item.text(0)) > 0:
            action_create_new_txt.triggered.connect(self.createNewTxtFile)
            action_delete_txt.triggered.connect(self.deleteTxtFile)
            action_create_new_dir.triggered.connect(self.createNewDir)
            action_delete_dir.triggered.connect(self.deleteDir)
            action_change_new_name.triggered.connect(self.changeNewName)

        context.exec(self.tree_widget.mapToGlobal(pos))

    def createNewTxtFile(self): 
        self.getset.setCurrentTreeItem(self.current_item)
        self.context_funcs.createNewTxtFile()
        self.main_win.refreshTreeWidget()

    def deleteTxtFile(self):
        pass

    def createNewDir(self):
        pass

    def deleteDir(self):
        pass

    def changeNewName(self):
        """사용자가 특정 트리 위젯 아이템에서 해당 액션 활성화 시 
        그 파일 또는 폴더 이름을 사용자가 원하는대로 바꿀 수 있도록 해준다."""
        # 테스트 필요.
        self.getset.setCurrentTreeItem(self.current_item)
        self.context_funcs.changeNewName()
        self.main_win.refreshTreeWidget()
    