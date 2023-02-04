def city_description(city_name, country_name, population = 5000000):
    formatted_city_name = f"{city_name.title()}, {country_name.title()}, population = {population}"
    return formatted_city_name
print(city_description("Santiago","Chile",5000000))
print(city_description("Santiago","Chile"))