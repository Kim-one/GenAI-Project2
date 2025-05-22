import random

# Randomly generate a number between 1 and 100
number_to_guess = random.randint(1,100)
print(number_to_guess)

max_attempts = 10 # max number of attempts

# Get user input
user_guess = int(input("Enter your guess (Between 1 and 100): "))

# Keeps track of the number of guesses
count = 1

# While loop to control the number of attempts
while(count<max_attempts):
    # If the user guess is equal to to the random number
    if user_guess==number_to_guess:
        print(f"Congrats! You guessed {user_guess} in {count} attempts.")
        break
    # Checks if the users guess is too high and prints a message
    elif user_guess>number_to_guess:
        print(f"{user_guess} Too high try again")
    # Checks if the users guess is too low and prints a message
    else:
        print(f"{user_guess} Too low. Try again")
    
    # Prompts the user for another guess
    user_guess = int(input("Enter your guess (Between 1 and 100): ")) 
    # Updates the number of attempts
    count+=1

# If the number of attempts equals to max attempts and the user hasn't guessed the correct number 
# Prints a game over message
if count==max_attempts and number_to_guess!=user_guess:
    print("Game Over. Try again")