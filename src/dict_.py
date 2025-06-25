import copy

# obj = dict([["name", "niraj"]])
# OR
obj = {"name": "niraj", "nested": {"items": [1, 2, 3]}}


# Another way of initialization
my_dict = dict(name="niraj", age=100)

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

# Shallow copy
obj2 = obj.copy()

obj2["name"] = "Boss"  # Won't be changed in obj
obj2["nested"]["items"].append(4)  # Mutates obj as well

print(obj, obj2)

obj = {"name": "niraj", "nested": {"items": [1, 2, 3]}}

# Deep Copy
obj3 = copy.deepcopy(obj)

obj3["name"] = "Boss"  # Won't be changed in obj
obj3["nested"]["items"].append(4)  # # Won't be changed in obj

print(obj, obj3)

# Merge two dicts

dict1 = {"a": "a", "b": "b"}
dict2 = {"c": "c", "d": "d"}
merged = {**dict1, **dict2}
print("Merged= ", merged)
