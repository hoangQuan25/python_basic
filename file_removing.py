import os
path = 'crud_copyfile.txt'
os.remove(path)

print(os.path.exists(path))