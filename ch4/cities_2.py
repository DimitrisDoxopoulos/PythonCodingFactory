# Map, filter and Lambdas

cities = ['london', 'paris', 'barcelona', 'athens', 'casablanka']

cap_length_cities = list(
    map(lambda city: city.title(), filter(
        lambda city: len(city) > 5, cities
    ))
)

print(cap_length_cities)
