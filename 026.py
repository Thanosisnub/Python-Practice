input = input("Please give any word: ")
first = input[0]
length = len(input)
rest = input[1:length]

if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    print(input + "way")
else:
    print(rest + first + "ay")
