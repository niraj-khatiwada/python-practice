name = "Niraj"

no_name = None

if name == "Niraj":
    print("Awesome name!")
elif name == "niraj":
    print("Okay")
else:
    print("Cap")


if no_name is None:
    print("Wait, no name?")
else:
    print("has name")


# Ternary
conditional_name = "Rust is still best" if no_name is None else "Python is fine too"
print(conditional_name)


is_hot = True

if is_hot is True:
    print("it's hot today")
else:
    print("cold")


# Equivalent &&
if is_hot and name is not None:
    print("Hot and has name")

# Equivalent to ||
if no_name is not None or conditional_name == "Rust is still best":
    print("Marvelous")
else:
    print("meh!")


# Equivalent to !is_hot
if not is_hot:
    print("Is not hot")
else:
    print("is hot")
