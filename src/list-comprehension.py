array = [
    {"name": "abc"},
    {"name": "def"},
]


mapped_array = [itm["name"] for itm in array]

print(mapped_array)

# Use enumerate if you want index as well
mapped_array = [{"name": itm["name"], "id": idx} for idx, itm in enumerate(array)]

print(mapped_array)
