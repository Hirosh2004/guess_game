import random

def guess_number():
    number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")
    
    while True:
        guess = int(input("Take a guess: "))
        
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed it!")
            break

guess_number()
