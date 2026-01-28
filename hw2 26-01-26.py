
# Enter name: Anthony Frtus

import random
# targetWord = "T"
targetWord = "THE"

# def monkeys_typing():
#     guessNumber = random.randint(65, 90)
#     letter1 = chr(guessNumber)
#     count = 1
#     guess = letter1
#     print(guess)
# 
#     while guess != targetWord:
#         guessNumber = random.randint(65, 90)
#         letter1 = chr(guessNumber)
#         guess = letter1
#         print(guess)
#         count +=1 
#     
#     return count
# 
# Total = 0
# for y in range(0,3):
#     Total += monkeys_typing()
# Total = Total / 3
# print("Average number of guesses for three runs is:", round(Total, 2))

def monkeys_typing():
    letter1 = ""
    for y in range(0,3):
        guessNumber = random.randint(65, 90)
        letter1 += chr(guessNumber)
    count = 1
    guess = letter1
    print(guess)

    while guess != targetWord:
        letter1 = ""
        for y in range(0,3):
            guessNumber = random.randint(65, 90)
            letter1 += chr(guessNumber)
        guess = letter1
        print(guess)
        count +=1 
    
    return count

Total = 0
for y in range(0,3):
    Total += monkeys_typing()
Total = Total / 3
print("Average number of guesses for three runs is:", round(Total, 2))
