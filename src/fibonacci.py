# 0 1 1 2 3 5 8
def fibonacci(num):
    array = [0]
    i = 0
    if num <= 0:
        return array
    array.append(1)
    i += 1
    while array[i] <= num:
        n = array[i] + array[i - 1]
        if n <= num:
            array.append(n)
            i += 1
        else:
            break
    return array


print(fibonacci(100))
