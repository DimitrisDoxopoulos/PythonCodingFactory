import sys
from pathlib import Path

path = Path('cf42023.txt')

def read_from_file(path):
    try:
        with open(path) as f:
            contents = f.read()
        return contents
    except OSError as e:
        print(e, file = sys.stderr)

def write_to_file(path, text):
    try:
        with open(path, 'a') as f:
            f.write(text)
    except OSError as e:
        print('Error: could not write to file', path, e)

import os

def delete_file(path):
    try:
        os.remove(path)
        print('File', path, 'deleted')
    except OSError:
        print('Error: could not delete file', path)
