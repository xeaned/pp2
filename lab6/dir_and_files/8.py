import os

path = '/Users/rapiyatleukhan/Desktop/pp2/lab6/dir_and_files/text3.txt'

if os.path.exists(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
    else: 
        print('file is not accessible')
else:
    print('file does not exist')