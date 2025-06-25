array = [
    {"name": "abc"},
    {"name": "def"},
]


mapped_array = [{"name": itm["name"], "id": idx} for idx, itm in enumerate(array)]

print(mapped_array)
