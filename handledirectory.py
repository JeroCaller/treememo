import os
import itertools
from pprint import pprint
import usererror as uerer

def splitPathWithSlash(path:str, split_path: list[str]=[]) -> list[str]:
    """경로 내 슬래시를 기준으로 경로 문자열을 분할하여 리스트 요소로 반환.
    문자열의 .split('/')와 같은 기능."""
    dir_name, base_name = os.path.split(path)
    if dir_name == '':
        split_path.insert(0, base_name)
        return split_path
    elif base_name == '':
        split_path.insert(0, dir_name)
        return split_path
    split_path.insert(0, base_name)
    return splitPathWithSlash(dir_name, split_path)


class HandleRootDir():
    def __init__(self, path:str=''): self.root_dir = path
    
    def getRootDir(self) -> str:
        try:
            attr_split = splitPathWithSlash(self.root_dir)
            os_split = splitPathWithSlash(os.getcwd())
            zip_data = itertools.zip_longest(
                attr_split, os_split, fillvalue=''
            )
            for attr, os_data in zip_data:
                if attr != os_data:
                    raise uerer.CurrentDirectoryNotSetted()
        except uerer.CurrentDirectoryNotSetted as e: 
            print(e)
            print("속성에 저장된 경로: {}".format(self.root_dir))
            print("os.getcwd(): {}".format(os.getcwd()))
        #print("self.root_dir: ", self.root_dir)
        #print("os.getcwd(): ", os.getcwd())
        return self.root_dir

    def setRootDir(self, new_root_dir:str): 
        self.root_dir = new_root_dir
        try: os.chdir(self.root_dir)
        except FileNotFoundError as e: 
            print(e)

    def getRootBaseName(self) -> str: return os.path.basename(self.root_dir)

    def tryMakeRootDir(self) -> str | None:
        """에러 발생 시 에러문을 문자열로 리턴.
        에러가 없으면 None을 반환."""
        try: os.mkdir(self.root_dir)
        except FileExistsError: 
            return "이미 같은 이름의 폴더가 있습니다. 다른 이름을 입력하세요."
        else:
            # os.chdir()은 실제로 존재하는 경로만 다룸.
            os.chdir(self.root_dir)
            return None

    def addSubDir(self, sub_dir: str):
        """이미 설정된 루트 디렉토리 경로에 sub_dir를 뒤에 덧붙임."""
        #new_root_absdir = os.path.join(self.root_dir, sub_dir)
        #self.root_dir = new_root_absdir
        self.root_dir += '\\' + sub_dir


class FileIO():
    def __init__(
            self, 
            target_path: str='',
            content: str=''
            ):
        """
        target_dir: 새 파일 경로 또는 읽어올 파일 경로. 확장자명도 포함시켜야 함.
        content: 파일에 쓰거나 읽어올 텍스트 내용
        """
        self.target_path = target_path
        self.content = content

    def setTargetDir(self, new_path:str): self.target_path = new_path
    def getTargetDir(self) -> str: return self.target_path
    def setContent(self, new_content): self.content = new_content
    def getContent(self) -> str: return self.content

    def readTextFile(self) -> str:
        """텍스트 파일로부터 내용을 읽어옴."""
        with open(self.target_path, 'r', encoding='utf-8') as file_obj:
            txt_data = file_obj.read()
        return txt_data
    
    def makeTextFile(self):
        """텍스트 파일을 만든다. 만드는 용도이므로 
        안에 내용은 따로 넣지 않는다."""
        with open(self.target_path, 'w', encoding='utf-8') as file_obj:
            file_obj.write('')
        

if __name__ == '__main__':
    root_dir = input("루트 디렉토리의 절대경로명 입력: ")
    hd = HandleRootDir(root_dir)
    pprint(hd.getGroupedStructure())
    # hd.getGroupedStructure()

    # C:\Users\Jeong_Jae_Hwan\Desktop\종합폴더\jwFreeNote_5.10.r6