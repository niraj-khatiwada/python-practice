import math
import random
import sys

print("Square root is ", math.sqrt(10))


v1 = 1 + 2

print(random.randint(1, 100))

v1 = "Niraj"

print(v1)


v2 = 3.14

print(type(v2))

print(sys.maxsize)

print(1.11111111 + 1.1111111111)

print(True, False, type(True))

print("Float to integer", int(3.14))
print("Integer to float", float(3))
print("Integer to str", str(3))
print("Float to str", str(3.14))
print("boolean to str", str(True))
print("Character", chr(97), chr(65))


print(2023, 12, 18, sep="/")
print("No New Line", end="")

print("\n%s %.2f %c %c" % ("Niraj", 3.14, "A", 97))

print(5 % 2)
print(5 // 2)


n = 1
n += 2
print(n)


print(math.inf)
print(math.nan)

print(math.inf - math.inf)  # nan

num1 = 16
output = ""
if num1 % 5 == 0:
    output += "fizz"
if num1 % 3 == 0:
    output += "buzz"
if num1 % 5 != 0 and num1 % 3 != 0:
    output = str(100)

print(output)


# Ternary Operator
random_value = random.randint(1, 100)
yourname = "Niraj" if random_value % 2 == 0 else "Avishek"
print(yourname)


print("Hello World \n")
print(r"Hello World \n")

name = "Niraj Khatiwada"

print("Length is ", len(name))
print("Uppercase ", name.upper())
print("Lowercase ", name.lower())
print("Slice: First, Chunk, Last ", name[0], name[0:2], name[-1])
print(name.split(" "))
print(name.replace("Niraj", "Suraj"))  # Does not replace the original value
print("Contains", "Niraj" in name, "Avishek" not in name)
print("Trim ", "  Niraj".strip(), " Niraj".lstrip(), "Niraj ".rstrip())
print("Join", " ".join(["Niraj", "Khatiwada", "Bro"]))
print("Reverse a string", "Niraj"[::-1])

# Format String
print(f"Hello {'World'} {69}")
print("bc123".isalnum())
print("123".isdigit())
