count = 0
while True:
    count += 1
    if count > 10:
        break


print(count)

for x in range(0, 10):
    print(x, end=" ")

print()

# Iterators
iterators = iter([1, 2, 3])

print(next(iterators))
print(next(iterators))
print(next(iterators))
# print(next(iterators)) throw error


generated_list = list(range(0, 10, 2))
print(generated_list)

# Tuples

tuples = (1, "Hello", "World")
print(tuples)
print(tuples[0])
print(tuples[-1])
print(tuples[::-1])
