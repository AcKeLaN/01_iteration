from random import randint
number = randint(1, 10)

guess = int(input("Guess a number between 1 and 10... "))

guesses = 1

lives = 3

while guess != number and guesses < 3:
    guesses += 1
    lives -= 1
    print("Incorrect!")
    print(f"You have {lives} lives left!")

    if guess > number:
        print("The number is lower... ")
    else:
        print("The number is higher... ")

    guess = int(input("Guess a number between 1 and 10... "))

if guess != number and guesses >= 3:
    print("Incorrect. Guess limit reached.")
    print(f"The number was {number}.")

else:
    print("You win!")
    print(f"You guessed the number in {guesses} attempts!")
