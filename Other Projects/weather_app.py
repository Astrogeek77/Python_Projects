import requests
from pprint import pprint

API_KEY = 'fcd707b89bf58e6d4f214ba0f6eb623f'

city = input("Enter a city name: ")

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + city

response = requests.get(base_url).json()

pprint(response)