from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
import ver2.embodyfunc as ef
import ver2.mainmemo as mainmemo


class ContextMenuForTreeWidget():
    """오로지 트리 위젯 위에서만 트리 위젯과 관련된 컨텍스트 메뉴가 뜨게 한다."""
    def __init__(
            self,
            main_win=None,
            tree_widget: QtWidgets.QTreeWidget=None,
            root_tree_item: QtWidgets.QTreeWidgetItem=None,
        ):
        """main_win: MainWindow"""
        self.main_win = main_win

        self.tree_widget = tree_widget
        self.tree_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_widget.customContextMenuRequested.connect(self.showContextMenu)

        self.cont_getset = ef.GetSetWidgets()
        self.cont_getset.setTreeWidget(self.tree_widget)
        self.cont_getset.setRootTree(root_tree_item)
        self.context_funcs = ef.EmbodyFuncInContextTree(
            main_win=main_win,
            getset_obj=self.cont_getset
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
        self.context_funcs.createNewFile()
        self.main_win.refreshTreeWidget()

    def deleteTxtFile(self):
        pass

    def createNewDir(self):
        pass

    def deleteDir(self):
        pass

    def changeNewName(self):
        pass