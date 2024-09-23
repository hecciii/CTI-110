 # Samari Franklin
 # 9/16/2024
 # P2HW2
 # Assignment assess student understanding of Lists

from statistics import mean

grade1 = int(input("Enter grade for module 1: "))
grade2 = int(input("Enter grade for module 2: "))
grade3 = int(input("Enter grade for module 3: "))
grade4 = int(input("Enter grade for module 4: "))
grade5 = int(input("Enter grade for module 5: "))
grade6 = int(input("Enter grade for module 6: "))

modulegrades = []

modulegrades.append(grade1)
modulegrades.append(grade2)
modulegrades.append(grade3)
modulegrades.append(grade4)
modulegrades.append(grade5)
modulegrades.append(grade6)
print()
print("--------------results--------------")
print()
print("Lowest grade: ", end="")
print (min(modulegrades))
print("Highest grade: ", end="")
print (max(modulegrades))
print("Sum of grades: ", end="")
print(sum(modulegrades))
print("Average: ", end="")
print(mean(modulegrades))