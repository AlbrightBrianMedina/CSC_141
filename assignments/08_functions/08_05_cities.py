# Brian Medina
#
# making a def function but inputing data from other variables

def describe_city(city, country = "Ghana"):
    print(f"{city} is in {country}.")

describe_city("Kiev", 'Ukraine')
describe_city("Accra")
describe_city("Savannah")
describe_city(country = "Ukraine", city = "Kiev")