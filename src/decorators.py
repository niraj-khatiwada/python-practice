import inspect
import functools

# Function Decorators


# Decorator without arguments
def print_fn(fn):
    print(f"Function name = {fn.__name__}. Args = {inspect.signature(fn)}")

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("do something before")
        rs = fn(*args, **kwargs)
        print("do something after")
        return rs

    return wrapper


@print_fn
def greet(name):
    print(f"hello world {name}")
    pass


greet(name="Niraj")
print(
    greet.__name__
)  # This will say wrapper if we don't apply the `@functools.wraps(fn)` decorator since a wrapper function is being returned from print_fn decorator


# Decorator with arguments
def repeat(num):
    def fn_wrapper(fn):
        def wrapper(*args, **kwargs):
            for _ in range(0, num, 1):
                fn(*args, **kwargs)

        return wrapper

    return fn_wrapper


@repeat(num=3)
def greet_repeat(name):
    print(f"Hello {name}")


greet_repeat("Niraj")


# Class Decorators


class CountFnCalls:
    def __init__(self, fn):
        self.fn = fn
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Executing `{self.fn.__name__}` function. Executed {self.count} times.")
        return self.fn(*args, **kwargs)


@CountFnCalls
def greet_class(name):
    print(f"Hello {name}")


greet_class("Niraj")
greet_class("Niraj")
