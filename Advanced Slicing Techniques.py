#Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temp = temperatures[7:14]
print(second_week_temp)

#Task 2: Extract all the temperatures above 100
#Created a new list to store the results we get 
temps_above_100 = []

for temp in temperatures:
    if temp > 100:
        temps_above_100.append(temp)
print(temps_above_100)