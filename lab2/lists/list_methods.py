# append() - Adds an element at the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# clear() - Removes all the elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []

# copy() - Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # ["apple", "banana", "cherry"]

# count() - Returns the number of elements with the specified value
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # 3

# extend() - Add the elements of a list (or any iterable) to the end of the current list
fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# index() - Returns the index of the first element with the specified value
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1

# insert() - Adds an element at the specified position
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "cherry"]

# pop() - Removes the element at the specified position
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)  # ["apple", "cherry"]

# remove() - Removes the item with the specified value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]

# reverse() - Reverses the order of the list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # ["cherry", "banana", "apple"]

# sort() - Sorts the list
fruits = ["cherry", "banana", "apple"]
fruits.sort()
print(fruits)  # ["apple", "banana", "cherry"]
