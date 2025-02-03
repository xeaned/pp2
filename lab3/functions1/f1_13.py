from random import randint
name = input('Hello! What is your name? ')
print("Well, " + name + ', I am thinking of a number between 1 and 20.')

num = randint(1, 21)
cnt = 0
while(True):
    print("Take a guess.")
    guessed_num = int(input())
    if guessed_num < num:
        print("Your guess is too low.")
        cnt += 1
    elif(guessed_num > num):
        print("Your guess is too high.")
        cnt += 1
    else:
        print("Good job, " + name + "! You guessed my number in " + str(cnt + 1) + " guesses")
        break