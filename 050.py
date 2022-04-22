num = int(input("Please enter a number: "))

while num < 10 or num > 20:
    if num < 10:
        print("Too low!")
    else:
        print("Too high!")
print("Thank you!")