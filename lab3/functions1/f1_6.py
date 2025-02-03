def reverse_words():
    string = input("sentence: ")
    words = string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

result = reverse_words()
print(result)