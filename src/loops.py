num = 0
while num < 100:
    print(num)
    num += 1

while num >= 100:
    print(num)
    num += 1
    if num == 150:
        break

# range(start, end, step)
for i in range(200, 250, 5):  # 250 is exclusive
    print(i)


# String
for ch in "niraj":
    print(ch)

# List
for itm in [1, 2, 3]:
    print(itm)

# Tuples
for itm in (1, 2, 3):
    print(itm)
