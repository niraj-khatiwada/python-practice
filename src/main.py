name = "Niraj"

print(f"Length={len(name)}")

# String slices
print("------Slices------")
print(name[0]) # N
print(name[0:2]) # Ni
print(name[-1]) # j
print(name[0:]) # Niraj
print(name[0:-1]) # Nira

print("------Conversion------")
print(name.lower()) # niraj
print(name.upper()) # NIRAJ
print(", ".join(["a","b","c"])) # a, b, c
print("   niraj".strip()) # niraj
