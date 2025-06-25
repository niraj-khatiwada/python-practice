num = 1
num = 1.2

boolean = True  # False

name = "niraj"


def print_name(name):
    print(name)


print_name(name)


def sum(a, b):
    return a + b


print("*" * 10)

print(1 * "1")

print("""
hello world
      

      markdown
""")


# Type conversion
year = "1998"

age = 2025 - int(year)

print(type(year).__name__, type(year).__name__ == "str")
print(type(int(year)).__name__, type(int(year)).__name__ == "int")


def hello():
    print("hello")


class Person:
    @staticmethod
    def greet():
        print("Hello World")


print(type("niraj").__name__)  # str
print(type(1).__name__)  # int
print(type(1.0).__name__)  # float
print(type([]).__name__)  # list
print(type(dict([])).__name__)  # dict
print(type(hello).__name__)  # function
print(type(Person).__name__)  # type

is_published_str = 1
is_published = bool(
    is_published_str
)  # This will return True. bool() checks for truthy/falsy values

print(is_published)


# Conversion of int to character
print(chr(97))  # a
print(chr(65))  # A

# Conversion of character to int
# ord means ordinal = numerical position of a character in the Unicode table
print(ord("a"))
print(ord("A"))
