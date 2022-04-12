repeat = "y"
people = 0
while repeat == "y":
    person = input("Please enter the person who you want to invite to the party: ")
    people = people + 1
    print(person, "has been invited!")
    repeat = input("Do you wanna invite more people?: ")

print(people, "people are invited to the party!")