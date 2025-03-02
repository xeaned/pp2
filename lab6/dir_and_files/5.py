my_list = ['car', 'fruit', 'cherry', 'chery']

with open('/Users/rapiyatleukhan/Desktop/pp2/lab6/dir_and_files/text.txt', 'w') as my_file:
    for words in my_list:
        my_file.write(words+'\n')