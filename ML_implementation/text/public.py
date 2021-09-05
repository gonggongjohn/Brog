from private_async import *
from math import sqrt


def wordDiv(input: list[str]) -> list[str]:
    output = []
    return output


class LocalTFIDFFilter:
    def __init__(self, windowSize=lambda x: sqrt(x), topRank=10, wordCount=None, stopWords=None, autoSave=1e3) -> None:
        self.winSz = windowSize
        self.tpRk = topRank
        self.tf = wordCount if (wordCount != None) else dict()
        self.stop = stopWords if (stopWords != None) else {"是", "好", "可以"}
        self.sv = autoSave
        self.cnt = 0
        pass

    def __call__(self, wordSeq: list[str]) -> list[str]:
        asyncTF(wordSeq,
                   self.winSz(len(wordSeq)),
                   rollStep=self.skip,
                   global_tf=self.tf)


class Embedding:
    def __init__(self) -> None:
        pass
