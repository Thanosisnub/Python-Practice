num1 = int(input("Please enter a number: "))
total = num1
again = "y"

while again == "y":
    num2 = int(input("Please enter a number to add to the last one: "))
    total = total + num2
    again = input("Do you want to add another number: ")

print(total, "was the total.")