def printName(name):
    print(name)


def sayHi():
    print('hi ot men')


def add(a, b):
    return a+b


def moreComplicated(a, b):
    res = a**5
    b(res)
    # b()


printName('qnko')
print(add(2, 5))


moreComplicated(4, printName)
