import random

flag = True
while flag:
    num = input('Type a number for an upper bound: ')

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print("Invalid input! Please try again.")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input('Please enter a number between 1 and ' + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print('You guessed right!')
    else:
        print('Not quite... try again!')
        count += 1

print('It took you', count, 'guesses!')