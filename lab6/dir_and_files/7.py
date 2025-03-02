with open('/Users/rapiyatleukhan/Desktop/pp2/lab6/dir_and_files/text1.txt', 'r') as file_1:
    with open('newtext.txt', 'w') as file_2:
        sometext = file_1.read()
        file_2.write(sometext)
