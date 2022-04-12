#declaration of variables
compnum = 50
guess = int(input("Can you guess the number I am thinking of?: "))
count = 1

#while command 
while guess != compnum:
    if guess < compnum:
        print("Too low!")
    else:
        print("Too high!")
    count = count + 1
    guess = int(input("Have another guess?: "))

print("Well done, you took", count, "attempts.")