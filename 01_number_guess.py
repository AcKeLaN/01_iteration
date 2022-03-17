from random import randint
number = randint(1, 10)

guess = int(input("Guess a number between 1 and 10... "))

guesses = 1

while guess != number and guesses < 3:
    guesses += 1
    print("Incorrect!")
    guess = int(input("Guess a number between 1 and 10... "))

if guess != number and guesses >= 3:
    print("Incorrect. Guess limit reached.")

else:
    print("You win!")
    print(f"You guessed the number in {guesses} attempts!")
