import requests

def fetch_weather(city):
    api_key = 'fa85025657bd641f0da961d07ef6bca3'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException:
        return {"error": "City not found"}

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = fetch_weather(city)
    if "error" in weather:
        print(weather["error"])
    else:
        print(f"City: {weather['name']}")
        print(f"Temperature: {weather['main']['temp']} °C")
        print(f"Description: {weather['weather'][0]['description']}")
