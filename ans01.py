#Program for number-guessing game
import random

SecretNumber = random.randint(1,6)
Guess = int(input("Enter the number: "))

NumberOfGuesses = 1

while Guess != SecretNumber:
    if Guess > SecretNumber:
        Guess = int(input("Guess a smaller number: "))
    if Guess < SecretNumber:
        Guess = int(input("Guess a bigger number: "))
    NumberOfGuesses = NumberOfGuesses + 1

print("Well Done, your guess is correct")
print("You took", NumberOfGuesses, "guesses")