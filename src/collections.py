from collections import Counter, namedtuple, OrderedDict, deque

# Counts the occurrence
str_counter = Counter("nirajn")
print("String counter ", str_counter)

list_counter = Counter([1, 2, 3, 4, 1])
print("List counter ", list_counter)

# Named Tuple
Point = namedtuple("Point", "x,y")
point = Point(1, 2)
print(point.x, point.y)


# Order Dictionary: Preserves the order in which the entries are inserted. Just like LinkedHashMap in Java
obj = OrderedDict({"b": "b"})
obj["c"] = "c"
obj["a"] = "a"
print((obj.keys()))


# Queue
queue = deque([1, 2, 3])
queue.append(4)  # push to end
queue.appendleft(5)  # push from start
print(queue.pop())  # Pop from right
print(queue.popleft())  # Pop from left
print(queue[0])  # peek left
print(queue[-1])  # peek right
