import os
from PySide6 import QtWidgets
from ver1.handledirectory import HandleDir, FileIO

class EmbodyFunc():
    def __init__(self):
        self.root_dir = ''
        self.hd = HandleDir()
        self.fileio = FileIO()

    def removeAllTreeWidgets(
            self, 
            root_tree_item : QtWidgets.QTreeWidgetItem
        ):
        if root_tree_item.childCount == 0:
            return
        root_tree_item.takeChildren()

    def printAllTreeWidgetItems(
            self,
            root_tree_item : QtWidgets.QTreeWidgetItem
        ):
        if root_tree_item.childCount() == 0:
            print("자식 트리 위젯 아이템 없음")
            return
        for i in range(root_tree_item.childCount()):
            child = root_tree_item.child(i)
            print(child.text(0), child.text(1))

    def setTree(
            self,
            root_abspath : str,
            parent_tree : QtWidgets.QTreeWidgetItem):
        base = os.path.basename(root_abspath)
        file_and_ext = base.rsplit('.', 1)
        if len(file_and_ext) == 2:
            item = QtWidgets.QTreeWidgetItem(parent_tree, [file_and_ext[0], file_and_ext[1]])
        else:
            item = QtWidgets.QTreeWidgetItem(parent_tree, [file_and_ext[0]])
        if os.path.isdir(root_abspath):
            for file_or_dir in os.listdir(root_abspath):
                full_path = os.path.join(root_abspath, file_or_dir)
                self.setTree(full_path, item)



if __name__ == '__main__':
    inst = EmbodyFunc()
    inst.setTree()