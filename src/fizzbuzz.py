rs = ""

num = int(input("Enter a number: "))

if num % 3 != 0 and num % 5 != 0:
    print(num)
else:
    if num % 3 == 0:
        rs += "fizz"
    if num % 5 == 0:
        rs += "buzz"
    print(rs)
