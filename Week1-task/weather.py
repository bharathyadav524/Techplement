import json
import sys
import time
import requests
import argparse

# Function to fetch weather data for a given city
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ff2ec6aa0f38106e4dfaf67b2f938efd"
    response = requests.get(url)
    data = response.json()
    return data

# Function to add a city to favorites list
def add_favorite(city):
    with open('favorites.json', 'r+') as file:
        favorites = json.load(file)
        favorites.append(city)
        file.seek(0)
        json.dump(favorites, file)

# Function to list favorite cities
def list_favorites():
    with open('favorites.json', 'r') as file:
        favorites = json.load(file)
        print("Favorite Cities:")
        for city in favorites:
            print(city)

# Main function to handle command-line arguments and execute appropriate actions
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Command Line Weather Application")
    parser.add_argument('city', nargs='?', help="City name to check weather")
    parser.add_argument('--add', help="Add city to favorites")
    parser.add_argument('--list', action='store_true', help="List favorite cities")
    parser.add_argument('--auto-refresh', action='store_true', help="Auto refresh weather every 15-30 seconds")
    args = parser.parse_args()

    if args.city:
        try:
            while True:  # Enter an infinite loop for auto-refreshing if enabled
                # Fetch weather data for the specified city
                weather_data = fetch_weather(args.city)
                print(f"Weather in {args.city}:")
                print(f"Description: {weather_data['weather'][0]['description']}")
                print(f"Temperature: {weather_data['main']['temp'] - 273.15}°C")
                if not args.auto_refresh:  # If auto-refresh is disabled, break the loop
                    break
                time.sleep(15)  # Wait for 15 seconds before fetching data again (adjust as needed)
        except Exception as e:
            print("Error:", str(e))

    if args.add:
        add_favorite(args.add)  # Add the specified city to favorites
        print(f"{args.add} added to favorites.")

    if args.list:
        list_favorites()  # List all favorite cities

# Entry point of the script
if __name__ == "__main__":
    main()
