from contextlib import contextmanager

# Example of context manager

# with open("README.md", "r") as readme:
#     print(readme.read())


# Custom Context Manager
# 1. Class


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("[FileManager] Entered")
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, *exceptions):
        if self.file:
            self.file.close()
        (exception_type, exception_value, traceback) = exceptions
        if exception_type is not None:
            print(
                "[FileManager] Exception occurred",
                exception_type,
                exception_value,
                traceback,
            )

        print("[Exiting] Exited")


with (
    FileManager("README.md") as file
):  # Here this file alias directly uses the self.file returned from __enter__ method
    print(file.read())


# 2. Function
# We need to use contextmanager generator for functions

print("--------------fn-------------")


@contextmanager
def file_manager(filename):
    print("[FileManager] Entered")
    file = open(filename, "r")
    try:
        yield file
    except Exception as e:
        print("[FileManager] Exception occurred", e)
    finally:
        file.close()
        print("[FileManager] Exited")


with file_manager("README.md") as file:
    print(file.read())
