import requests

API_KEY = "fcd707b89bf58e6d4f214ba0f6eb623f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# city = input("Enter a city name: ")
city = 'ludhiana'
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    pressure = round(data["main"]["pressure"] / 100, 2)
    deg = round(data["wind"]["deg"])
    speed = round(data["wind"]["speed"])
    name = data["name"]

    print("Weather in", name, ": ", weather)
    print("Temperature:", temperature, "celsius")
    print("Pressure:", pressure, "bar")
    print("Wind:",deg, "°, ",speed, "KM/H")
else:
    print("An error occurred.")
