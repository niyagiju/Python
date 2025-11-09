import random
upperrange=int(input("Enter the upper limit for the number guessing game: "))
lowerange=int(input("Enter the lower limit for the number guessing game: "))
random=random.randint(lowerange, upperrange)
guesses=0
while True:
    guess=int(input(f"Guess a number between {lowerange} and {upperrange}: "))
    if guess < random:
        print("Too low! Try again.")
    elif guess > random:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        
        break
    guesses+=1
    
print(f"You took {guesses} attempts to guess the number.")



