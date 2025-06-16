import requests

API_KEY = "d5aa73ee84e5c00367ba2e12717ff007"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, unit): # FUnction to get the weather of a city
    # dictionary to hold queries
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" if unit == "C" else "imperial"
    }
    # Try block to get data from the api
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ Error: {data.get('message', 'Unable to fetch weather data')}")
            return

        name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]
        unit_symbol = "°C" if unit == "C" else "°F"

        print(f"\n📍 Weather in {name}:")
        print(f"   Temperature: {temp}{unit_symbol}")
        print(f"   Condition: {description}")
        print(f"   Humidity: {humidity}%")
        print(f"   Wind Speed: {wind_speed} {'m/s' if unit == 'C' else 'mph'}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

def main():
    print("🌤️  Weather Checker")
    unit = ""
    while unit not in ["C", "F"]:
        unit = input("Choose temperature unit - (C)elsius or (F)ahrenheit: ").strip().upper()

    cities = input("Enter city names (comma separated): ").split(",")
    for city in cities:
        city = city.strip()
        if city:
            get_weather(city, unit)

main()