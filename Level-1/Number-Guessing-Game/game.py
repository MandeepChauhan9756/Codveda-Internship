import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 to 100")
print(f"You have {max_attempts} attempts. \n")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1
        
        if guess > secret_number:
            print("Too High \n")
        elif guess < secret_number:
            print("Too Low \n")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break
    
    except ValueError:
        print("Please enter a valid number.")
        
if guess != secret_number:
    print(f"Game Over! The number was {secret_number}")
