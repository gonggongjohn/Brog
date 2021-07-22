import os

FILE_DIR = os.path.join(os.path.dirname(__file__), 'files')

def read_binary_file(filename):
    with open(filename, 'rb') as f:
        if f: yield f.read(512)

def store_binary_file(filename, file):
    with open(filename, 'wb') as f:
        for line in file.chunks():
            pass
