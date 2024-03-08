import os

path = 'crud.txt'
try:
    with open(path, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('file not found')