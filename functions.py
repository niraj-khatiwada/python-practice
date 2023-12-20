def sum(a, b):
    return a + b


def sum_all(*args):
    sum = 0
    for item in args:
        sum += item
    return sum


print(sum_all(1, 2, 3))


def destructure():
    return 1, 2


i1, i2 = destructure()
print(i1, i2)


# Anonymous functions
print((lambda x: x * 2)(100))
