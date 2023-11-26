import random
def guessing_game():
    print("Welcome to the Number Guessing Game!")
    min_value = 1  
    max_value= 100  
    number = random.randint(min_value, max_value)
    attempts=0
    while True:
        guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
        if guess < number:
            attempts+=1
            print("Too low, please try again!")
            print("Your attempts:",attempts)

        elif guess > number:
            attempts+=1
            print("Too high, please try again!")
            print("Your attempts:",attempts)
        else:
            attempts+=1
            print(f"Congratulations! {number} is the correct number you have guessed!")
            print("You have guessed correctly at ",attempts," attempts.")
            break

guessing_game()
