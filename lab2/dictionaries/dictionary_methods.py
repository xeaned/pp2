# clear() - Removes all the elements from the dictionary
thisdict = {"a": 1, "b": 2, "c": 3}
thisdict.clear()
print(thisdict)  # {}

# copy() - Returns a copy of the dictionary
thisdict = {"a": 1, "b": 2, "c": 3}
new_dict = thisdict.copy()
print(new_dict)  # {"a": 1, "b": 2, "c": 3}

# fromkeys() - Returns a dictionary with the specified keys and value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {"a": 0, "b": 0, "c": 0}

# get() - Returns the value of the specified key
thisdict = {"a": 1, "b": 2, "c": 3}
value = thisdict.get("b")
print(value)  # 2

# items() - Returns a list containing a tuple for each key-value pair
thisdict = {"a": 1, "b": 2, "c": 3}
print(thisdict.items())  # dict_items([("a", 1), ("b", 2), ("c", 3)])

# keys() - Returns a list containing the dictionary's keys
thisdict = {"a": 1, "b": 2, "c": 3}
print(thisdict.keys())  # dict_keys(["a", "b", "c"])

# pop() - Removes the element with the specified key
thisdict = {"a": 1, "b": 2, "c": 3}
thisdict.pop("b")
print(thisdict)  # {"a": 1, "c": 3}

# popitem() - Removes the last inserted key-value pair
thisdict = {"a": 1, "b": 2, "c": 3}
thisdict.popitem()
print(thisdict)  # {"a": 1, "b": 2}

# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key with the specified value
thisdict = {"a": 1, "b": 2}
value = thisdict.setdefault("c", 3)
print(thisdict)  # {"a": 1, "b": 2, "c": 3}
print(value)  # 3

# update() - Updates the dictionary with the specified key-value pairs
thisdict = {"a": 1, "b": 2}
thisdict.update({"c": 3, "d": 4})
print(thisdict)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# values() - Returns a list of all the values in the dictionary
thisdict = {"a": 1, "b": 2, "c": 3}
print(thisdict.values())  # dict_values([1, 2, 3])
