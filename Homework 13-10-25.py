Items = []
Prices = []
Total = 0
High = 0
Low = 1000.0
Amount = int(input("Enter the amount of items:"))
for y in range(0, Amount):
    Item = input("Enter your item:")
    Price = float(input(f"Enter your price for {Item}:"))
    while Price < 0.01:
        print("Price is too low!!!")
        Price = float(input(f"Enter your price for {Item}:"))
    Items.append(Item)
    Prices.append(Price)
    Total += Price
    if Price > High:
        High = y
    if Price < Low:
        Low = y
Average = round((Total / Amount), 2)
print("\nYour shopping list")
for y in range(0, Amount):
    print(f"{Items[y]}: €{Prices[y]}")
print("\nShopping Summary")
print(f"Total cost: €{Total}")
print(f"Highest cost: {Items[High]} (€{Prices[High]})")
print(f"Lowest cost: {Items[Low]} (€{Prices[Low]})")
print(f"Average cost: €{Average}")
Budget = float(input("Enter your budget:"))
if Total > Budget:
    print("You are over budget!")
    print(f"Additional money needed: €{Total-Budget}")
else:
    print("You are within budget!")
    print(f"Money left over: €{Budget-Total}")
for y in range(0, Amount):
        Sort = Prices[y]
        while Prices[y-1] > Sort and y > 0:
            Prices[y], Prices[y-1] = Prices[y-1], Prices[y]
            Items[y], Items[y-1] = Items[y-1], Items[y]
            y = y - 1
Items.reverse()
Prices.reverse()
print("\nYour shopping list from high to low:")
for y in range(0, Amount):
    print(f"{Items[y]}: €{Prices[y]}")