import json

stringified = json.dumps([1, 2, 3])

print(stringified, type(stringified).__name__)

parsed = json.loads(stringified)

print(parsed, type(parsed).__name__)

stringified = json.dumps({"name": "Niraj"}, indent=3)

print(stringified, type(stringified).__name__)

parsed = json.loads(stringified)

print(parsed, type(parsed).__name__)
