import random

number = random.randint(0,100)
correct = False

while correct == False:
    guess = int(input("Enter your guess:"))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Congratulations!")
        correct = True

        