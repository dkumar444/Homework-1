from math import ceil
#
# print("Enter wall height (feet):")
# height = int(input())
# print("Enter wall width (feet):")
# width = int(input())
# area = height * width
# print(f"Wall area: {area} square feet")
#
# print()
# print("Enter wall height (feet):")
# height = int(input())
# print("Enter wall width (feet):")
# width = int(input())
# area = height * width
# gallon = float(area/350)
# print(f"Paint needed: {gallon:.2f} gallons")
#
# print()
# print("Enter wall height (feet):")
# height = int(input())
# print("Enter wall width (feet):")
# width = int(input())
# area = height * width
# gallon = float(area/350)
# print(f"Paint needed: {gallon:.2f} gallons")
#
# print()
# print("Enter wall height (feet):")
# height = int(input())
# print("Enter wall width (feet):")
# width = int(input())
# area = height * width
# gallon = float(area/350)
# print(f"Paint needed: {gallon:.2f} gallons")
# print(f"Cans needed: {ceil(gallon):.2f} can(s)")
#
# print()
my_dict = {'red':35, 'blue':25, 'green':23}
print("Enter wall height (feet):")
height = int(input())
print("Enter wall width (feet):")
width = int(input())
area = height * width
gallon = float(area/350)
print(f"Wall area: {area} square feet")
print(f"Paint needed: {gallon:.2f} gallons")
print(f"Cans needed: {ceil(gallon)} can(s)")
print()
print('Choose a color to paint the wall:')
color = input()
print(f"Cost of purchasing {color} paint: ${my_dict[color]*ceil(gallon)}")