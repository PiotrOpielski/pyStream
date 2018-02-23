from pyStream import Stream


def py_stream_test():
    test = list(range(500))
    Stream(test) \
        .map(str) \
        .filter(lambda x: x != "2") \
        .for_each(lambda x: print(x))


def casual_test():
    test = list(range(500))
    for x in filter(lambda x: x != "2", map(str, test)):
        print(x)
