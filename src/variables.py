num = 1
num = 1.2

boolean = True  # False

name = "niraj"


def print_name(name):
    print(name)


print_name(name)


def sum(a, b):
    return a + b


print("*"*10)

print(1 * "1")

print('''
hello world
      

      markdown
''')


# Type conversion
year = "1998"

age = 2025 - int(year)

print(type(year).__name__, type(year).__name__=="str")
print(type(int(year)).__name__, type(int(year)).__name__=="int")

is_published_str = 1
is_published = bool(is_published_str) # This will return True. bool() checks for truthy/falsy values

print(is_published)

