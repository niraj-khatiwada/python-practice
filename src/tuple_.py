tuples = (1, 2, 3)
# or
# tuples = tuples([1,2,3])

print(len(tuples))
print(tuples[0])

# Destructuring
[a, b, c] = tuples
print(a, b, c)

my_tuple = (1, 2, 3, 4, 5)

(a, *rest) = my_tuple

print(a, rest)


# Weird behavior

# tuples_2 = (1) # This will not be a tuple. This'll be treated as tuples_2 = 1
# We need to atleast have a comma at the end to have a single value tuple

tuples_2 = (1,)
