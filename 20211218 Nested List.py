country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                ["New York", "Dallas", "San Francisco"]]

long_cities = []
for country in country_list:
    for city in country:
        if len(city) >= 6:
            long_cities.append(city)

print(long_cities)

long_cities = [city for country in country_list for city in country if len(city) >= 6]

print(long_cities)
