# Usually we want to assign stringified of parsed json to a class. For this we need to write a corresponding json encoder and decoder
# Encoder = stringify
# Decoder = parse

from json import JSONEncoder, JSONDecodeError
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                "name": obj.name,
                "age": obj.age,
                "__name__": obj.__class__.__name__,
            }

    @staticmethod
    def decode(obj):
        print(obj, type(obj).__name__)
        if "__name__" in obj and obj["__name__"] == User.__name__:
            return User(obj["name"], obj["age"])
        raise JSONDecodeError("Invalid user object supplied.")


user = User(name="Niraj", age=27)
stringified = UserEncoder().encode(user)  # Class is directly stringified
print("stringified= ", stringified, type(stringified).__name__)

parsed = json.loads(stringified, object_hook=UserEncoder.decode)

print(
    "Parsed= ", parsed, isinstance(parsed, User)
)  # Stringified json is directly converted to user class
