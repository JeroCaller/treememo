import os

def splitPathWithSlash(path:str, split_path: list[str]=[]):
    dir_name, base_name = os.path.split(path)
    if dir_name == '':
        split_path.insert(0, base_name)
        return split_path
    elif base_name == '':
        split_path.insert(0, dir_name)
        return split_path
    split_path.insert(0, base_name)
    return splitPathWithSlash(dir_name, split_path)


path = input("경로 입력: ")
split_path = splitPathWithSlash(path)
print(split_path)

"""
path = 'C:/user/wow.txt'
split_path = []
dir_name, base_name = os.path.split(path)
split_path.insert(0, base_name)

dir_name, base_name = os.path.split(dir_name)
split_path.insert(0, base_name)

dir_name, base_name = os.path.split(dir_name)
split_path.insert(0, base_name)

print(dir_name)
print(base_name)
print(split_path)
"""