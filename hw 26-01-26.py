
# Enter name:

county = ["Dublin", "Laois", "Dublin", "Dublin", "Dublin", "Dublin", "Dublin", "Kildare", "Laois", "Kildare", "Dublin", "Laois", "Dublin"]

rent = [2500, 1200, 2000, 2100, 1900, 1999, 1790, 1500, 1000, 1390, 1980, 1105, 1999]

# Part i
print("The total people in the survey is:", len(county))

# Part ii

county.append(input("Please enter your county:"))
rent.append(int(input("Please enter your monthly rent amount:")))

print("-"*18)
print("{:<12}".format("County")+"{:<12}".format("Rent €"))
print("-"*18)
for index in range(len(county)):
    print("{:<12}".format(county[index])+"{:<12}".format(rent[index]))

# Part iii

Total=0
for y in range(0, len(rent)):
    Total += rent[y]
print("Average rent for all counties: €", round(Total/len(rent),2))

# Part iv
Check = []
Count = []
Place =[]
for y in range(0, len(county)):
    Check.append(county[y])
    if Check.count(county[y]) < 2:
        Count.append(rent[y])
        Place.append(county[y])
    else:
        for z in range(0, len(Place)):
            if county[y] == Check[z]:
                Count[z] += rent[y]
for y in range(0, len(Place)):
    print("Average rent for", Place[y], ": €", round(Count[y]/county.count(Place[y]), 2))
                
