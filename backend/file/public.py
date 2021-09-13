import os
from sys import executable


FILE_DIR = os.path.join(os.path.dirname(__file__), 'files')
print('store all uploaded files at: %s' % FILE_DIR)


def read_xml(filename):
    with open(os.path.join(FILE_DIR, 'xml', filename), 'rb') as f:
        if f:
            yield f.read(512)


SCRIPT_DIR = os.path.join(os.path.dirname(__file__), 'pdf2txt.py')


def pdf_to_xml(pdf_path, xml_path):
    return lambda: os.system('python %s -o %s %s' % (SCRIPT_DIR, xml_path, pdf_path))


def markdown_bold_to_link(md_name, put_to_database):
    mdStr = ""
    with open(os.path.join(FILE_DIR, "md", md_name), 'r') as f:
        if f:
            mdStr = f.read()
    msk = False
    splited = mdStr.split("**")
    for x in splited:
        if msk:
            x = "[%s](%s)" % (x, put_to_database(x.strip(" ")))
        msk = not msk
