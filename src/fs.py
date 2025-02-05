import shutil
import os

filepath = os.path.abspath(__file__)
print("Current file = ", filepath)
dir = os.path.dirname(filepath)
print("Current directory = ", dir)

# Copy file
shutil.copyfile(os.path.join(dir, "classes.py"), os.path.join(dir, "classes(copy).py"))

# Create folder
os.mkdir(os.path.join(dir, "new-folder"))

# Rename a folder
os.rename(os.path.join(dir, "new-folder"), os.path.join(dir, "new-folder2"))

# Create a file
with open(os.path.join(dir, "new_file.txt"), "w") as file:
    file.write("hello world!")

# Check if path exists
print(
    "Folder exists = ",
    os.path.exists(os.path.join(dir, "new-folder2")),
)
print("File exists = ", os.path.exists(os.path.join(dir, "new_file.txt")))


# Remove path
os.rmdir(os.path.join(dir, "new-folder2"))
os.remove(os.path.join(dir, "new_file.txt"))
os.remove(os.path.join(dir, "classes(copy).py"))
