import random

print("Random integer", random.randint(0, 100))  # Any random in between
print("Random integer", random.randrange(0, 100, 2))  # With steps

# Randomly shuffles the array
array = [1, 2, 3]
random.shuffle(x=array)
print(array)

# Choose random choices from list. Optional k to specify how many item to choose
print(random.choices(array, k=2))

print(random.choices([True, False]))
