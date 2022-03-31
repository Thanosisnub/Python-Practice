from math import remainder


firstnum = int(input("Please enter the first number: "))
secondnum = int(input("Please enter the second number: "))

wholenum = firstnum // secondnum
remaind = firstnum % secondnum

print(firstnum,"divided by", secondnum, "makes", wholenum, "with", remaind, "as the remainder")