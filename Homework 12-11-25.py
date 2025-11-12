# Question 16(a)
# Student name: Anthony Arundel
import random
def dice_game():
    print("welcome to my dice game!!")

dice_game()

your_name = input("Please enter your name: ")
lucky_number = int(input("Please select a lucky number between 1 and 6:"))
Good = 0
while Good == 0:
    if lucky_number < 7:
        if lucky_number > 0:
            Good = 1
            break
    lucky_number = int(input("Please select a lucky number between 1 and 6:"))
computer_die_roll = random.randint(1,6) #Initialise dice roll
print(f"{your_name}'s lucky number was: {lucky_number}")
print("The computer rolled: ", computer_die_roll)
if lucky_number < computer_die_roll:
    print("You guessed too low!")
elif lucky_number > computer_die_roll:
    print("You guessed too high!")
elif lucky_number == computer_die_roll:
    print("You guessed correct, well done!")