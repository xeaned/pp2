# capitalize()
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# center()
text = "Python"
print(text.center(10, "-"))  # Output: "--Python--"

# count()
text = "Rapiya"
print(text.count("a"))  # Output: 2

# endswith()
text = "exampleeee"
print(text.endswith("eee"))  # Output: True

# find()
text = "hello"
print(text.find("e"))  # Output: 1

# format()
text = "My name is {name} and I am {age} years old."
print(text.format(name="Rapiya", age=18))  # Output: "My name is Rapiya and I am 18 years old."

# isalnum()
text = "Python3"
print(text.isalnum())  # Output: True

# isalpha()
text = "pp"
print(text.isalpha())  # Output: True

# isdigit()
text = "12345"
print(text.isdigit())  # Output: True

# islower()
text = "pp"
print(text.islower())  # Output: True

# isnumeric()
text = "12345"
print(text.isnumeric())  # Output: True

# join()
words = ["Hello", "world"]
print(" ".join(words))  # Output: "Hello world"

# replace()
text = "I like Python"
print(text.replace("like", "love"))  # Output: "I love Python"

# split()
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

# startswith()
text = "hello world"
print(text.startswith("hello"))  # Output: True

# strip()
text = "  hello world  "
print(text.strip())  # Output: "hello world"

# upper()
text = "allo"
print(text.upper())  # Output: "ALLO"

# zfill()
text = "52"
print(text.zfill(5))  # Output: "00052"