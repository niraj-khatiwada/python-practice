while True:
    try:
        number = input("Please enter an even number\n")
        if int(number) % 2 != 0:
            raise Exception(f"{number} is not an even number")
        print(f"Nice number {number}")
        break
    except ValueError:
        print("You didn't enter a value")
