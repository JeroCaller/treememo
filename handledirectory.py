import os
from PySide6 import QtWidgets


class FileIO():
    def __init__(self, abspath: str=''):
        self.path = abspath

    def getPath(self) -> str: return self.path
    
    def setPath(self, new_abspath: str): 
        self.path = new_abspath

    def readFromFile(self) -> str:
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    
    def createNewFile(self, file_name:str="새 텍스트.txt") -> str | None:
        """주어진 경로에 새 텍스트 파일 생성.
        성공 시 None, 실패 시 에러 내용이 문자열 형태로 리턴됨."""
        txt_name = self.path + "\\" + file_name
        try:
            with open(txt_name, 'w', encoding='utf-8') as file:
                file.write('')
        except Exception as e: return e
        else: return


class HandleDir():
    def __init__(self, dir: str = '', main_win : QtWidgets.QMainWindow = None):
        self.dir = dir
        self.main_win = main_win

    def getDir(self) -> str: return self.dir
    
    def setDir(self, new_dir): 
        self.dir = new_dir

    def askAndGetDir(self, title: str='') -> str:
        dir_dialog = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_win,
            caption=title
        )
        return dir_dialog
    
    def addSubDir(self, dir: str):
        """기존 경로 뒤에 추가 경로를 이어붙인다."""
        joined_dir = os.path.join(self.getDir(), dir)
        self.setDir(joined_dir)

    def tryMakeDir(self, title="정보", message="") -> bool:
        try:
            os.mkdir(self.getDir())
        except FileExistsError:
            QtWidgets.QMessageBox.critical(self.main_win, title, message)
            return False
        else: return True

    def tryMakeFile(self, title:str="정보", message:str=""):
        """선택된 하위 폴더 내에 새 파일 생성"""
        pass

    def getPathOfSelectedFile(
            self, 
            tree_obj: QtWidgets.QTreeWidgetItem, 
            file_name: str
        ) -> str:
        """사용자가 선택한 트리 위젯 아이템의 텍스트에 해당하는 파일 경로 반환.
        최상위 트리 위젯 아이템의 텍스트는 반드시 루트 폴더의 상대 경로명이어야 함.
        file_name은 파일 또는 디렉토리 상대경로."""
        try:
            if os.path.abspath(tree_obj.parent().text(0)) == self.getDir():
                file_name = os.path.dirname(tree_obj.parent().text(0)) + '/' + file_name
                return file_name
            file_name = self.getPathOfSelectedFile(
                tree_obj.parent(), 
                tree_obj.parent().text(0) + '/' + file_name
            )
        except AttributeError: pass  # 해당 에러 무시
        return file_name
    
    def isDir(self, file_or_dir_base_name: str) -> bool:
        return os.path.isdir(file_or_dir_base_name)
    