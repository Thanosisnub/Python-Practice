
# Code to reverse the number!

Number = int(input("Enter the number: "))
Behind = 0
Remain = 0
while (Number > 0):
  Remain = Number % 10
  Behind = (Behind * 10) + Remain
  Number = Number // 10
print ("Reverse of entered number is", Behind)

# code to find the palindrome!

Number = int(input("Enter a number: "))
A = Number
Reverse = 0
while(Number > 0):
    Remainder = Number % 10
    Reverse = Reverse * 10 + Remainder
    Number = Number // 10
if (A == Reverse):
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")
