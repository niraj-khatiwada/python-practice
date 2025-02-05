import os

filepath = os.path.abspath(__file__)
print("Current file = ", filepath)
dir = os.path.dirname(filepath)
print("Current directory = ", dir)

print("OS = ", os.name)

print("CWD = ", os.getcwd())

# Access environment
print("Term = ", os.environ.get("TERM"))

print("CPU count = ", os.cpu_count())

print("Process id = ", os.getpid())
