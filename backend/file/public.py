import os
import json

FILE_DIR = os.path.join(os.path.dirname(__file__), 'files')
print('store all uploaded files at: %s' % FILE_DIR)


def read_xml(filename):
    with open(os.path.join(FILE_DIR, 'xml', filename), 'rb') as f:
        if f:
            yield f.read(512)


SCRIPT_DIR = os.path.join(os.path.dirname(__file__), 'pdf2txt.py')


def pdf_to_xml(pdf_path, xml_path):
    return lambda: os.system('python %s -o %s %s' % (SCRIPT_DIR, xml_path, pdf_path))


def recPrint(dic, indent=""):
    for x in dic:
        print(indent, x)
        try:
            recPrint(dic[x], indent=indent + "   ")
        except:
            continue


def md_to_tree(md_str: str):
    rowList = md_str.splitlines(keepends=False)
    def recDiv(rows: list[str], divby):
        if divby == "####### ":
            return ""
        subDict = {"": []}
        y = ""
        for x in rows:
            if x.startswith(divby):
                subDict[x] = []
                y = x
            else:
                subDict[y].append(x)

        for x in subDict:
            tmp = recDiv(subDict[x], "#"+divby)
            if tmp != '':
                subDict[x] = tmp

        if subDict[""] == []:
            return ""
        return subDict
    return json.dumps(recDiv(rowList, divby="# "))