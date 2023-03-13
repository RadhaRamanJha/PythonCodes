def city_description(city_name, country_name, population = 5000000):
    """Generates neatly forated city name"""
    formatted_city_name = f"{city_name.title()}, {country_name.title()}, population = {population}"
    return formatted_city_name

print(city_description("Santiago","Chile"))