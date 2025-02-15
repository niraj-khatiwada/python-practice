from functools import reduce

sum = lambda a, b: a + b


print(sum(1, 2))

array = [(1, 2), (3, 4), (2, 3)]

# Sorting
sorted_array = sorted(array, key=lambda x: x[1])
print(sorted_array)

# Map
mapped_array = map(lambda x: x[0] * 10, array)
print(list(mapped_array))

# Filter
even_array = filter(lambda x: (x[0] % 2) == 0, array)
print(list(even_array))

# Reduce
reduced_sum = reduce(lambda a, c: a + c[0] + c[1], array, 0)
print(reduced_sum)

reduced_list = reduce(lambda a, c: (a.extend([c[0], c[1]]) or a), array, [])
print(reduced_list)
