total = 0
for i in range(0,5):
    number = int(input("Enter a number: "))
    answer = input("Do you want this to be included?: ")
    if answer == "y":
        total = total + number
print(total)