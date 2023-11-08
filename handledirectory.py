import os
from PySide6 import QtWidgets
from pprint import pprint

class FileIO():
    def __init__(
            self, 
            contents: str | list[str]='', 
            dir: str='', 
            file_mode: bool=True
        ):
        self.contents = contents
        self.dir = dir
        self.file_mode = file_mode

        # 상수 정의
        # 파일 쓰기 모드
        self.NEW_WRITE = True
        self.CONTINUE_WRITE = False

    def setContents(self, new_contents: str | list[str]):
        "파일 입출력을 위한 파일 내용을 설정"
        self.contents = new_contents

    def setDir(self, new_dir: str):
        "쓰거나 읽어올 파일의 절대 경로 설정"
        self.dir = new_dir

    def setFileMode(self, mode: bool):
        self.file_mode = mode

    def writeContentsIntoFIle(self):
        """파일에 쓸 내용을 setContents() 메서드를 통해,
        내용을 쓸 타겟 파일 절대 경로를 setDir() 메서드를 통해 반드시 설정 후 실행."""
        if type(self.contents) == str:
            self.writeStringIntoFIle()
        elif type(self.contents) == list[str]:
            self.writeLinesIntoFile()
        else:
            pass

    def writeStringIntoFIle(self):
        """contents: 파일에 쓸 내용 (텍스트)
        dir : 파일 절대 경로
        file_mode -> True: 새로 쓰기, False: 이어 쓰기
        """
        if self.file_mode:
            file_mode_str = 'w'
        else:
            file_mode_str = 'a'
        with open(self.dir, file_mode_str, encoding='utf-8') as file:
            file.write(self.contents)

    def writeLinesIntoFile(self):
        if self.file_mode:
            file_mode_str = 'w'
        else:
            file_mode_str = 'a'
        with open(self.dir, file_mode_str, encoding='utf-8') as file:
            for line in self.contents:
                file.write(line)

    def readFromFile(self) -> str:
        """타겟 파일 경로를 반드시 setDir()로 먼저 설정해줘야 함."""
        with open(self.dir, 'r', encoding='utf-8') as file:
            contents = file.read()
        return contents


class HandleDir():
    def __init__(
            self,
            dir: str =''
        ):
        self.dir = dir
        self.fileio_obj = FileIO(dir=self.dir)

    def addSubDir(self, new_dir):
        "기존의 파일 경로에 하위 폴더 이름을 추가하여 붙임"
        self.dir = os.path.join(self.dir, new_dir)

    def setDir(self, new_dir):
        self.dir = new_dir

    def getDir(self) -> str:
        return self.dir

    def tryMakeDir(self, title="정보", message="") -> bool:
            try:
                os.mkdir(self.dir)
            except FileExistsError:
                QtWidgets.QMessageBox.critical(self.tlwidget, title, message)
                return False
            else: return True
    
    def writeTreeStructureinTextFile(
            self, 
            file_name : str,
            indent='    '
        ):
        """루트 디렉토리 내의 모든 폴더 및 파일들을 계층에 따라 
        트리 구조로 텍스트 파일에 작성하여 저장."""
        def setTreeStructure(
                indent, 
                root_dir,
                tree_structure: list = [],  
                count=1
            ) -> list[str]:
            tree_structure.append((indent * count) + '\\' + os.path.basename(root_dir) + '\n')
            if os.path.isdir(root_dir):
                for one_item_path in os.listdir(root_dir):
                    full_path = os.path.join(root_dir, one_item_path)
                    setTreeStructure(indent, full_path, tree_structure, count+1)
            return tree_structure
        
        tree_structure = setTreeStructure(indent, self.dir, count=0)
        self.fileio_obj.setContents(tree_structure)
        self.fileio_obj.setDir(file_name + '.txt')
        self.fileio_obj.writeContentsIntoFIle()
    
    def getPathOfSelectedFile(
            self, 
            tree_obj: QtWidgets.QTreeWidgetItem, 
            file_path: str
        ) -> str:
        try:
            if tree_obj.parent().text(0) == self.getDir():
                file_path = os.path.dirname(tree_obj.parent().text(0)) + '/' + file_path
                return file_path
            file_path = self.getPathOfSelectedFile(
                tree_obj.parent(), 
                tree_obj.parent().text(0) + '/' + file_path
            )
        except AttributeError: pass  # 해당 에러 무시
        return file_path

if __name__ == '__main__':
    obj = HandleDir(dir='C:\python\pyside6_study')
    obj.writeTreeStructureinTextFile(file_name=obj.getDir())
