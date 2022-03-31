name = input("Enter your name: ")
number = int(input("Enter a number: "))

if number < 10:
    for i in range(0,number):
        print(name)
else:
    for i in range(0,3):
        print("Too high")