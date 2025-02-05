items = set([1, 2, 3, 1])

print(items)
print("Size", len(items))
print("Exists", 1 in items)

for item in items:
    print(item)


items.add(3)
items.add(2)
items.add(5)
print(items)
