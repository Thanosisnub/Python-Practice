#declaration of variables
rain = input("Is it raining?: ")
rain = str.lower(rain)

#if command
if rain == "yes":
    wind = input("Is it windy?: ")
    wind = str.lower(wind)
    if wind == "yes":
        print("It is too windy for an umbrella!")
    else:
        print("Please take an umbrella!")
else:
    print("Enjoy the day!")

