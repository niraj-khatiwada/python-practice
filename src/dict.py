# obj = dict([["name", "niraj"]])
# OR
obj = {"name": "niraj"}

print(len(obj))
print(obj.get("name"))
print("age" in obj)  # False
print(obj.get("age", 21))  # default value if entry is not found
print(list(obj.keys()))
print(list(obj.values()))

for item in obj.items():
    # item would be a tuple here
    print(item[0], item[1])


obj["name"] = "Niraj"
print(obj)
