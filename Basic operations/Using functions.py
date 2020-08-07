m = 40


def loc():
    m = 9


def glob():
    global m
    m += 1


def glob2():
    m = 0
    m += 1


def glob3():
    m = 0
    import sys
    glob = sys.modules['thismod']
    glob.var += 1


def test():
    print(m)
    loc()
    glob()
    glob2()
    glob3()
    print(m)


test()
