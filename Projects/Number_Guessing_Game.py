import random


def start_game(): #defining the main game function
    print("Wlcome to the number geussing game!")
    
    #set the range & attempts
    lower_bound = 1
    upper_bound = 100
    max_attempts = 7
    
    #Generate a random number
    secret_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0 #initialize attempts counter
    while attempts < max_attempts: #using while loop
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}:"))
        except ValueError:
            print("please enter a valid number.")
            continue #skip to the next iteration if input is not a number
        
        if guess < lower_bound or guess > upper_bound: #check if the guess is out of bounds
            print(f"please choose a number within the range {lower_bound} to {upper_bound}")
            continue
        
        attempts += 1 #Increment the attempt count
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the right number {secret_number} in {attempts} attempts.")
            break #Exit the loop if the guess is correct
        elif guess < secret_number:
            print("too low! try again.")
        else:
            print("Too high! try again.")
            
    else:
        #If player runs out of attempts
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}")
        
if __name__ == "__name__":
    start_game() #start the game