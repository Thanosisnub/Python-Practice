num = int(input("How many friends do you want to invite to the party?: "))
if num < 10:
    for i in range(0,num):
        name = input("Please enter the name of the friend: ")
        print(name, "has been invited.")
else:
    print("Too many people!")