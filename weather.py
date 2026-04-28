import requests
api_key = "d5cffac688d23a1e2ee94834a7403eff"
city = input("Enter City Name:")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"temperature: {temp}°C")
    print(f"Condition: {weather}")
else:
    print("City not found ❌")