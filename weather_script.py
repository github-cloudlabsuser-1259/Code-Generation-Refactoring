# Fetch weather data from OpenWeatherMap API and print it
import requests
def fetch_weather(city, api_key):
    """Fetch weather data for a given city using OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise ValueError(f"Error fetching weather data: {response.status_code} - {response.text}")

# Create function which uses the response from fetch_weather and prints information
# about temperature, humidity, and weather description. Give a list of other available data also
# that can be printed.
def print_weather_info(weather_data):
    """Print weather information from the fetched data."""
    if 'main' in weather_data and 'weather' in weather_data:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description'].capitalize()}")
        
        # Print other available data
        print("\nOther available data:")
        for key, value in weather_data.items():
            if key not in ['main', 'weather']:
                print(f"{key}: {value}")
    else:
        print("Invalid weather data received.")

# Main function to run the weather script
def main():
    """Main function to run the weather script."""
    city = input("Enter the city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    try:
        weather_data = fetch_weather(city, api_key)
        print_weather_info(weather_data)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()