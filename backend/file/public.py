import os

FILE_DIR = os.path.join(os.path.dirname(__file__), 'files')
print('store all uploaded files at: %s' % FILE_DIR)

def read_binary_file(filename):
    with open(filename, 'rb') as f:
        if f: yield f.read(512)