class IterableEx:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end - 1

    def __iter__(self):
        #Called at the start of loops
        return self

    def __next__(self):
        #Called at each loop increment
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start

class Iterable:
    def __init__(self, repo):
        self.__repo = repo
        self.__index = -1
        self.__length = len(repo)

    def __getitem__(self, index):
        return self.__repo[index]

    def __setitem__(self, index, value):
        self.__repo[index] = value

    def __delitem__(self, index):
        del self.__repo[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__length - 1 == self.__index:
            raise StopIteration
        else:
            self.__index += 1
            return self.__repo[self.__index]

def compare(e1, e2, sign):
    operator = {"<": (lambda x, y: x < y), ">": (lambda x, y: x > y), "=": (lambda x, y: x == y),
                "<=": (lambda x, y: x <= y), ">=": (lambda x, y: x >= y)}
    return operator[sign](e1, e2)

def sort(list, compare):
    pos = 0
    while pos < len(list):
        if pos == 0 or compare(list[pos], list[pos - 1], ">="):
            pos += 1
        else:
            list[pos], list[pos - 1] = list[pos - 1], list[pos]
            pos -= 1
    return list

def filter(list, accept):
    i = 0
    while i < len(list):
        if not accept(list[i]): #don't keep element
            list.pop(i)
    return list

'''class SortFunction:
    def __init__(self, list):
        self.__list = list
        #Comparisson/acceptance function? f(a,b)?

    def sort(self):
        pos = 0
        while pos < len(self.__list):
            if pos == 0 or self.__list[pos] >= self.__list[pos - 1]:
                pos += 1
            else:
                self.__list[pos], self.__list[pos - 1] = self.__list[pos - 1], self.__list[pos]
                pos -= 1
        return self.__list

    def accept(self):
        pass'''

if __name__ == '__main__':
    #for c in Iterable1(0, 5):
    #    print(c)
    #print("=============\n")
    i2 = Iterable([2,4,6,8,10])
    for v in i2:
        print(v)