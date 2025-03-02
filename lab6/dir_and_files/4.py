with open('/Users/rapiyatleukhan/Desktop/pp2/lab6/dir_and_files/text.txt', 'r') as mfile:
    cnt = 0
    for line in mfile:
        if line:  
            cnt += 1
print(cnt)