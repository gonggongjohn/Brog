import os
import asyncio

FILE_DIR = os.path.join(os.path.dirname(__file__), 'files')
print('store all uploaded files at: %s' % FILE_DIR)

def read_xml(filename):
    with open(os.path.join(FILE_DIR, 'xml', filename), 'rb') as f:
        if f: yield f.read(512)

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), 'pdf2txt.py')
def pdf_to_xml(pdf_path, xml_path):
    return lambda: os.system('python %s -o %s %s'%(SCRIPT_DIR, xml_path, pdf_path))