# Filter out all the empty strings from the list below.
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
new_places = []
for i in places:
    if i.strip() != '':
        new_places.append(i)
print(new_places)
