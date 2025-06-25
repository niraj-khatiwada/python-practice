def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

print(next(gen))

# There's no way to check if the next value yielded by generators exist or not. So it is better to always provide a default fallback value for next()
print(next(gen, None))
print(next(gen, None))

# print(next(gen)) # crashes
print(next(gen, None))
