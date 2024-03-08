import os

path = 'C:\\programming\\ThucHanhOOP\\reports\\Bao_cao_lab_01.pdf'
if os.path.exists(path):
    print('file exists')
    if os.path.isfile(path):
        print('that is a file')

filename, extension = os.path.splitext(path)
print(f'name: {filename}, extension: {extension}')

basename = os.path.basename(path)
print(basename)

dirname = os.path.dirname(path)
print(dirname)