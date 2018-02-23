class Stream:

    def __init__(self, parameter):
        self.object = parameter

    def for_each(self, l):
        for x in self.object:
            l(x)

    def map(self, l):
        self.object = map(l, self.object)
        return self

    def filter(self, l):
        self.object = filter(l, self.object)
        return self

    def to_list(self):
        return list(self.object)
