lst=[1, 2, 3, 4, 5]
square=map(lambda x: x**2, lst)
print(list(square))


lst1=[1, 2, 3, 4, 5]
lst2=[2, 3, 4, 5, 6]
summa=map(lambda x, y: x+y, lst1, lst2)
print(list(summa))

words = ["hello", "world", "python"]
uppercase_words = map(str.upper, words)
print(list(uppercase_words))  


sentence="Hello my dear friend"
words=sentence.split()
print(all(word.isupper() for word in words))

lst=[1, 2, 3, 2, 4]
print(all(i>0 for i in lst))

lst = ["apple", "banana", "cherry", 3]
print(all(isinstance(word, str) for word in lst))
