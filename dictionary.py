obj = dict(
    [
        (
            "name",
            "Niraj",
        ),
        (
            "age",
            26,
        ),
    ]
)

print(len(obj))
print(list(obj.keys()))  # Object.keys()
print(list(obj.values()))  # Object.entries()

obj["name"] = "Suraj"

print(obj["name"], obj["age"])

del obj["name"]

print(obj)


print("age" in obj)

for key in list(obj.keys()):
    print(key)

for value in list(obj.values()):
    print(value)

for key, value in list(obj.items()):
    print(key, value)


dict1 = {"Name": "Niraj", "age": 26}

print(dict1)
