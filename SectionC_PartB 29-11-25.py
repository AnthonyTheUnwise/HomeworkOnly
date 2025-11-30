from random import choice

fruits = ["apple", "cherry", "orange"]
print("The initial list of fruits is:\n", fruits)
fruits.append(input("Enter an additional fruit:"))
print("The list of four fruits is:\n", fruits)
Winner = input("Nominate your winning fruit:")
while fruits.count(Winner) == 0:
    print("Error: winning fruit must be in the list")
    Winner = input("Nominate your winning fruit:")
print("The winning fruit you selected is", Winner)
Counter = 0
while True:
    Chosen = []
    Counter += 1
    Chosen.append(choice(fruits))
    Chosen.append(choice(fruits))
    Chosen.append(choice(fruits))
    if Chosen.count(Winner) == 3:
        break
print("Winner after", Counter, "times")