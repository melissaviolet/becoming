# testing code

def city_country(city, country, population = None ):
    if population:
        name = f"{city}, {country} - population {population}"
        return name.title()
    else:
        name = f"{city}, {country}"
        return name.title()

well = city_country("kampala", "uganda", 500_000)
print(well)

