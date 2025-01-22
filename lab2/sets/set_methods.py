# add() - Adds an element to the set
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {"apple", "banana", "cherry"}

# clear() - Removes all the elements from the set
fruits.clear()
print(fruits)  # set()

# copy() - Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
new_fruits = fruits.copy()
print(new_fruits)  # {"apple", "banana", "cherry"}

# difference() - Returns a set containing the difference between two or more sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # {1}

# difference_update() - Removes the items in this set that are also included in another set
set1 = {1, 2, 3}
set1.difference_update({2, 3})
print(set1)  # {1}

# discard() - Removes the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # {"apple", "cherry"}

# intersection() - Returns a set, that is the intersection of two other sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # {2, 3}

# intersection_update() - Removes the items in this set that are not present in other sets
set1 = {1, 2, 3}
set1.intersection_update({2, 3, 4})
print(set1)  # {2, 3}

# isdisjoint() - Returns whether two sets have a intersection or not
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # True

# issubset() - Returns whether another set contains this set or not
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # True

# issuperset() - Returns whether this set contains another set or not
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # True

# pop() - Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)  # One random element removed

# remove() - Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {"apple", "cherry"}

# symmetric_difference() - Returns a set with the symmetric differences of two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.symmetric_difference(set2))  # {1, 4}

# symmetric_difference_update() - Inserts the symmetric differences from this set and another
set1 = {1, 2, 3}
set1.symmetric_difference_update({2, 3, 4})
print(set1)  # {1, 4}

# union() - Returns a set containing the union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# update() - Updates the set with the union of this set and others
set1 = {1, 2, 3}
set1.update({3, 4, 5})
print(set1)  # {1, 2, 3, 4, 5}
