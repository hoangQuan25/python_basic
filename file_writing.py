import os

filename = 'crud.txt'
text = 'I wanna add this line\nThis line as well\n'

try:
    with open(filename, 'w') as f:
        f.write(text) # Each time we open a file to write, everything existing before in the file will be rewritten
        f.write('Appended more data') # If we write more, this will be appended to the end of the file, and the file won't be rewritten
                                      # Until we close
    with open(filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('file not found')