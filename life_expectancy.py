import requests

def calculate_life_expectancy(age, country):
    # Use the World Bank API to look up the life expectancy in the given country
    api_url = "http://api.worldbank.org/v2/country/" + country + "/indicator/SP.DYN.LE00.IN"
    api_response = requests.get(api_url)
    print(api_response)

    # Get the life expectancy value from the API response
    life_expectancy = api_response[1][0]['value']

    # Calculate the number of years the person has left to live based on their age and life expectancy
    years_left = life_expectancy - age

    return years_left

# Test the function with a few different ages and countries
print(calculate_life_expectancy(30, "ITA"))
print(calculate_life_expectancy(50, "USA"))
print(calculate_life_expectancy(70, "JPN"))