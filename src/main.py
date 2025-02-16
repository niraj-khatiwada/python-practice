s = {1, 2, 3, 3}

print(s)
print("Length= ", len(s))
print("Exists= ", 1 in s)

s.add(4)
s.add(1)
s.remove(3)

print(s)

# Merge two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
merged = {*s1, *s2}
print("Merged= ", merged)  # 1, 2, 3, 4, 5
