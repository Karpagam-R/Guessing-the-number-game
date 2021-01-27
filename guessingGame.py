#import the random 
import random

#Prints the below text on screen like a heading
print("Number guessing game !!!!!")
print("Let's get started :)")

# randint function is used to generate the random number between 1 to 9
number = random.randint(1, 9)

# number of chances to be given to the user to guess the number
# or it is the inputs given by user into input box here number of chances are 5
chances = 0

print("Guess a number (between 1 and 9):")

# While loop to count the number of chances
#note - in the while loop we are also setting the chances as 5
while chances < 5:

    # Enter a number between 1 to 9
    guess = int(input("Enter your guess:- "))

    # Compare the user entered number with the number to be guessed

    if guess == number:
        # if number entered by user is same as the generated
        # number by randint function then break from loop using loop
        # control statement "break"
        print("Congratulation YOU WON!!! \n Good Guess!!!!")
        break

    # Check if the user entered number is smaller than the generated number
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    # The user entered number is greater than the generated number
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances += 1

# Check whether the user guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)