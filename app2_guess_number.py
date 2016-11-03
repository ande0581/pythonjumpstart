import random

print('----------------------------------')
print('     Guess the Number App')
print('----------------------------------')
print()

answer = random.randint(0, 100)

while True:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < answer:
        print('Sorry but {} is LOWER than the number'.format(guess))
    elif guess > answer:
        print('Sorry but {} is HIGHER than the number'.format(guess))
    else:
        print("YES! You've got it. The number was {}".format(guess))
        exit()
