print("1) Square")
print("2) Triangle")
print()

selection = int(input("Please choose one of the option: "))
if selection == 1:
    lenght = int(input("Please enter the length of one of the side: "))
    print(lenght * 4)
elif selection == 2:
    base = int(input("Please enter the base of the triangle: "))
    height = int(input("Please enter the height of the triangle: "))
    area = (base * height)/2
    print(area)
else:
    print("Choose a suitable option. Try again")
