import os
from pprint import pprint

#path = 'wow.txt'
path = 'C:\\'
other_path = 'd'
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(os.path.splitext(path))
print(os.path.join(path, other_path))
