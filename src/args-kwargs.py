def unknown_args(*args, **kwargs):
    print("Args", type(args).__name__, args)  # Args are tuple
    print("Kwargs", type(kwargs).__name__, kwargs)  # Kwargs are dict


unknown_args(1, 2, 3, name="Niraj")
