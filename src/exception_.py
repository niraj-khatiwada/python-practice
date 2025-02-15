try:
    a = 5 / 0
except ZeroDivisionError as e:
    print("[error]", str(e))
except TypeError:
    print("[error]", "Type error")
else:
    print("[error]", "Unknown error")
finally:
    print("Task completed")


# Custom Exceptions
class ValueTooHighError(Exception):
    pass


try:
    val = input("Provide an integer value: ")
    if int(val) > 100:
        raise ValueTooHighError("Value is too high.")
except ValueTooHighError as e:
    print("[error] value too high", str(e))
except Exception as e:
    print("[error] unknown error", str(e))


class ValueTooSmallError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val


try:
    val = input("Provide an integer value: ")
    if int(val) < 10:
        raise ValueTooSmallError("Value is too small.", val)
except ValueTooSmallError as e:
    print(
        f"[error] Value {e.val} is too small",
    )
except Exception as e:
    print("[error] unknown error", str(e))
