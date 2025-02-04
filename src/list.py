fruits = ["apple", "mango", "banana", "tomato"]

# Getter
print("---------------")
print("Length ", len(fruits))  # 4
print(fruits[0])  # "apple"
print(fruits[-1])  # tomato
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[0:-1])  # ["apple", "banana", "mango"]
print(" > ".join(fruits))  # "apple" > "banana" > "mango" > "tomato"
print("apple" in fruits)  # True
print(fruits.index("mango"))  # 1
fruits.sort()
print("sorted", fruits)
fruits.reverse()
print("reversed", fruits)
fruits.reverse()
print("---------------")

# Setter
fruits[3] = "grape"
print(fruits)

# Push
fruits.append("watermelon")
fruits.append("tomato")
print("append ", fruits)

fruits.insert(0, "dragon fruit")
print("insert", fruits)

# Pop
fruits.pop()  # By default removes last
print(fruits)

fruits.pop(0)  # Remove at given index
print(fruits)


# # Delete: But use .pop() instead
# del fruits[3]
# print(fruits)

# Clear all values
fruits.clear()
print(fruits)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0], matrix[0][1])

for row in matrix:
    for num in row:
        print(num)

# Sorting
nums = [2, 3, 1]
nums.sort()
print("ASC", nums)
nums.sort(reverse=True)
print("DESC", nums)


# Clone list
nums_2 = nums.copy()
nums_2[0] = 11
print(nums)  # Wont' be affected
print(nums_2)
