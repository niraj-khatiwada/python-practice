def print_age():
    """
    Asks for user's age and prints it.
    """
    age_str = input("what is your age? ")
    try:
        age = int(age_str)
        print(f"Your age is {age}")
    except Exception as e:
        print(
            f'Invalid age supplied "{age_str}"\n{str(e)}',
        )


print_age()
