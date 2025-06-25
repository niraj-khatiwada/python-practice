import base64

text = "hello world"
encoded = base64.encodebytes(text.encode())
print("Encoded = ", encoded)
decoded = base64.decodebytes(encoded)
print("Decoded = ", decoded)

print(text == decoded.decode())
