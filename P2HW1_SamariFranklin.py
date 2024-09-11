# Samari Franklin
# 9/11/2024
# P2HW1
# Assignment assess student ability to edit and enhance exiting programs

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

print("\n---------------Travel Expenses---------------")
print()
print()
print("Location: ",travel_place)
print()
print("initial budget: ", f"${budget:.2f}")
print("\nFuel: ", f"${gas_price:.2f}")
print()
print("Accomdations: "  f"${hotel_price:.2f}")
print()
print("Food: ", f"${Food_cost:.2f}")
print()
print("\nRemaining balance:" "$" ,budget-gas_price-hotel_price-Food_cost)