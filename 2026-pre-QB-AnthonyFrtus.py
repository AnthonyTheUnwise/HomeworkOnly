#Question16_B_HL
#Enter your name here: Anthony Frtus

def summary_report(List):
    average = 0
    for y in range(0, len(List)):
        average += List[y]
    average /= len(List)
    average = round(average, 2)
    return average

positive_reviews = []
negative_reviews = []
reviews = []
end = True
count = 0
while end:
    rate = input("Please enter a rating from 1 - 5:")
    if rate == "done":
        end = False
        break
    rate = int(rate)
    count += 1
    reviews.append(rate)
    if rate < 3:
        negative_reviews.append(rate)
    if rate > 3:
        positive_reviews.append(rate)
print("The negative reviews are:", negative_reviews)
print("The positive reviews are:", positive_reviews)
if len(positive_reviews) > len(negative_reviews):
    print("user satisfaction is high")
if len(positive_reviews) < len(negative_reviews):
    print("user satisfaction is low")
pos_cent = round(((len(positive_reviews) / count) * 100), 2)
print("The percentage of positive results was:", pos_cent, "%")
for y in range(1, 6):
    print(f"{y}-star rating:", "*"*(reviews.count(y)))
print("The average review was:", summary_report(reviews))