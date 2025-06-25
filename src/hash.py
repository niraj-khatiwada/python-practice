import hashlib

hashed = hashlib.sha256("hello world".encode()).hexdigest()

print("hashed", hashed)
