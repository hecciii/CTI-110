# Samari Franklin
# 9/11/2024
# P2LAB1
# Assignment tests student's knowledge of how to write code that uses a dictionary 

# create a dictionary 
cars = {"Camaro":18.21, "Prius": 52.36,"Model S": 110, "Silverado": 26}
keys = cars.keys()
print(keys)
print()
# get user input assign to varible
user_car = input("Enter a vehicle to see its mpg: ")
print("The", user_car ,"gets" , cars [user_car], "mpg.")
# Get miles to drive from user
drive_miles = int(input("How many miles will you drive in the " + user_car + "? "))
print()
print(drive_miles)
print()
gallons_needed = drive_miles / cars[user_car]
print(round(gallons_needed, 2),"of gas are needed to drive the", user_car , drive_miles , "miles.")