num = 10
while num>0:
    print("There are", num, "green bottles hanging on the wall.")
    print(num, "bottles hanging on the wall.")
    print("And if 1 bottle accidentally fell down.")
    num = num - 1
    answer = int(input("How many bottles will be hanging on the wall now?: "))
    if answer == num:
        print("There will be", num,"bottles hanging on the wall.")
    while answer != num:
        answer = int(input("Try again: "))
print("There are no more bottles on the wall!")