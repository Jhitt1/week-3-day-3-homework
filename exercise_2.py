# Write an anonymous function that sorts this list by last names.
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
x = sorted(authors, key=lambda name: name.split(" ")[-1].lower())
print(authors)
print(x)