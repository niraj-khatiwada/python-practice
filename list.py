import functools

list = [1, 2, 3]
print(len(list))

print(list == [1, 2, 3])  # Lists are value pointed

# slice
print(list[:1], list[-1], list[1:])

# push
list.append(4)
print(list)

# pop
list.pop()
print(list)

# remove by value
list.remove(1)

# add to beginning
list = [0] + list

print(list)

print("Contains ", 0 in list)
print("Min", min(list))
print("Max", max(list))

print("Reverse a list ", list[::-1])


# Array.map()
array = [1, 2, 3]
print(list(map(lambda x: x**2, array)))

# Array.filter()
print(
    list(
        filter(lambda x: x % 2 == 0, array),
    )
)

# Array.reduce()
print(functools.reduce(lambda x, y: x + y, range(1, 10)))
