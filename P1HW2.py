
# Samari Franklin
# 9/4/2024
# P1HW2
# Basic Math on numbers entered 
print()
print()
print("---------This program calculates and dislays travel expenses----------")
print()
print()
budget = int(input("Enter a Budget: "))
travel_place = input("Enter your travel destination: ")
gas_price = int(input("How much do you think you will spend on gas? "))
hotel_price = int(input("How much do you think you will spend on Accomodations/Hotel? "))
Food_cost = int(input("Lastly, How much do you need for food "))

print("---------------Travel Expenses---------------")
print()
print()
print("Location: ",travel_place)
print("initial budget: ", budget)
print()
print()
print("Fuel: ", gas_price)
print("Accomdations: ", hotel_price)
print("Food: ", Food_cost)
print()
print()
print("Remaining balance: ",budget-gas_price-hotel_price-Food_cost)