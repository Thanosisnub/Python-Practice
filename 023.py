#declaration of variables
phrase = str(input("Please input the first line of a nursery rhyme: "))
length = len(phrase)

num1 = int(input("Please input a start number: "))
num2 = int(input("Please input an end number: "))

line = (phrase[num1:num2])

print(line)