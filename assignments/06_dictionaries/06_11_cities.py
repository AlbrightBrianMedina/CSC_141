"""
 Brian Medina

 Around the World
 Locations and info about them
"""

cities = {
    'New York city': {
          'population':'8.58 million',
           'country': 'United states',
           'fact': 'most popular city in the us',
           },

    'London': {
           'population': '9.1 million',
            'country': 'england',
            'fact': 'London is the capital and largest city of the United Kingdom'
            },

    'Paris': {
        'population': '2.04 million',
        'country': 'France',
        'fact': 'Paris has no traditional stop signs left anywhere in the city'
        }}

for name, city_info in cities.items():
    print(f"City Name: {name}")
    population_number = city_info["population"]
    country_location = city_info["country"]
    fact_info = city_info["fact"]

    print(f"\tPopulation: {population_number.title()}")
    print(f"\tCountry: {country_location.title()}")
    print(f'\tFact: {fact_info.title()}')