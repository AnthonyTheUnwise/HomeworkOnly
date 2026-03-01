#Question16_a_HL
#Enter your name here: Anthony Frtus

print("Welcome to my feedback tracker")

ratings = []
average = 0
fives = 0
end = True

#for y in range (0, 5):
while end:
    rating = int(input("Please enter a rating from 1-5:"))
    if rating > 0:
        if rating < 6:
            ratings.append(rating)
    if rating == -1:
        end = False
for y in range(0, len(ratings)):
    average += ratings[y]
    if ratings[y] == 5:
        fives += 1
print("Thge list of ratings is:", ratings)
average /= 5
print("The average rating was:", average)
print("The number of 5-star ratings was:", fives)
ratings.sort()
ratings.reverse()
print("The ratings list sorted from largest to smallest is:", ratings)
