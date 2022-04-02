print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

my_dict={'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12, 'No service':0}


print("Select first service:")
s1 = input()
if s1 =='-':
    s1 = 'No service'
print("Select second service:")
s2 = input()
if s2 =='-':
    s2 = 'No service'

print("\nDavy's auto shop invoice")
print()
if s1!='No service':
    print(f"Service 1: {s1}, ${my_dict[s1]}")
    pass
else:
    print(f"Service 1: {s1}")
    pass
if s2!='No service':
    print(f"Service 2: {s2}, ${my_dict[s2]}")
    pass
else:
    print(f"Service 2: {s2}")
    pass
print()
print(f"Total: ${my_dict[s1]+my_dict[s2]}")