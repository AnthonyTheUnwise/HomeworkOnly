#Question 16 (b)
#Student name: Anthony 
import random
ticket = []

for y in range(0, 3):
    user_number = int(input ("Please pick a number between 1 and 10: "))
    ticket.append(user_number)

print ("Your ticket is: ", ticket)
print ("The draw will start now, good luck!")
drum = [1,2,3,4,5,6,7,8,9,10]
result = []
def lotto (ticket):
    for times in range (3):
        draw = drum [random.randint (0,len (drum))-(1+times)]
        result.append (draw)
        drum.remove (draw)
    print("The draw was: ", result)
    result.sort()
    ticket.sort()
    if result == ticket:
        print("You win!")
    else:
        print("You lose!")
     
lotto (ticket)