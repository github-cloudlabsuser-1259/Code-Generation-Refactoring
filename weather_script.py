import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f"Weather in {city}: {weather}, Temperature: {temp}°C")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Weather Fetcher")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
