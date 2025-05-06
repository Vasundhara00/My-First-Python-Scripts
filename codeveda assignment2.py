import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

# Loop until the user guesses correctly
while True:
    # Take input from the user
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    # Check if the guess is correct
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
        break  # Exit the loop when the user guesses correctly
