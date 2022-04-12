#declaration of variables
name = input("Enter your first name: ")
surname = input("Enter your surname: ")
fullname = name+surname

#if command
if len(name) < 5:
    print(fullname.upper())
else:
    print(name.upper())