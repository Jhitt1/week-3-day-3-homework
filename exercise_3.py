# convert the list from celsius to farhenheit using the map funtion with lambda.
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
Fahrenheit = list(map(lambda x:(float(9)/5)*x + 32))
print(places)
