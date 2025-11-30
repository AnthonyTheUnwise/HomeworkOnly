# Question 16 (a)
# Examination Number: 356933
from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits)
print("Random fruit 1:", random_fruit_1)
random_fruit_2 = choice(fruits)
print("Random fruit 2:", random_fruit_2)
random_fruit_3 = choice(fruits)
print("Random fruit 3:", random_fruit_3)
if random_fruit_1 == "cherry":
    print("First fruit is cherry")
if random_fruit_1 == random_fruit_2:
    print("First pair is match")