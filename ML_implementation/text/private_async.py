import gevent
from math import log2, sqrt
from gevent import monkey


def asyncMap(func, lst, step=5):
    # step 每步长异步执行多少任务, 不同步长之间先后执行
    result = []

    def div():
        sz, cnt = 0, 0
        divided = [[]]
        for x in lst:
            divided[cnt].append(x)
            sz = sz + 1
            if sz == step:
                divided.append([])
                sz, cnt = 0, cnt + 1
        return divided
    divList = div()  # 如果传入指定步长则按照步长规定执行
    for lis in divList:
        g_list = list()
        for i in lis:
            g = gevent.spawn(func, i)
            g_list.append(g)
        gevent.joinall(g_list)
        for g in (g_list):
            result.append(g.value)
    return result


def asyncTF(wordList, windowSize, rollStep=1, global_idf=dict()) -> dict[str, list[float]]:
    # O(len(wordList * windowSize / rollStep))
    tf, df = dict(), dict()

    def somethingpp(sth):
        def inner(x):
            if x in sth:
                sth[x] += 1
            else:
                sth[x] = 1
        return inner
    dfpp = somethingpp(df)
    asyncMap(dfpp, wordList)

    def oneStep(x):
        local_tf = dict()
        local_tfpp = somethingpp(local_tf)
        asyncMap(local_tfpp, x)
        frac = [0.0, ]

        def local_tfsq(w):
            tmp = local_tf[w]
            frac[0] += tmp
            local_tf[w] = tmp
        asyncMap(local_tfsq, local_tf.keys())

        def tfsqpp(w):
            if w in tf:
                tf[w] += local_tf[w] / frac[0]
            else:
                tf[w] = local_tf[w] / frac[0]
        asyncMap(tfsqpp, local_tf.keys())

    asyncMap(oneStep, [
        wordList[i:i+windowSize]
        for i in range(0, len(wordList), rollStep)
    ])

    frac = rollStep / windowSize

    def divByWinSize(x):
        tf[x] = frac * df[x] * tf[x]

    asyncMap(divByWinSize, tf.keys())

    return tf