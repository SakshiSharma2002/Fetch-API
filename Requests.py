import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(date):
    params = {"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please try again later.")
        return None

def get_user_input():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_date_input():
    date = input("Enter the date (YYYY-MM-DD): ")
    return date

def print_weather_data(weather_data, date, choice):
    hourly_data = [item for item in weather_data["list"] if item["dt_txt"].startswith(date)]
    if not hourly_data:
        print("No data found for the specified date.")
        return

    for item in hourly_data:
        print(f"{item['dt_txt']}:")
        if choice == "1" and "main" in item and "temp_max" in item["main"]:
            print(f"  Max Temperature: {item['main']['temp_max']} K")
        elif choice == "2" and "wind" in item and "speed" in item["wind"]:
            print(f"  Wind Speed: {item['wind']['speed']} m/s")
        elif choice == "3" and "main" in item and "pressure" in item["main"]:
            print(f"  Pressure: {item['main']['pressure']} hPa")
        else:
            print(f"  Data not available for this hour.")
        print()

def main():
    while True:
        choice = get_user_input()

        if choice == "1" or choice == "2" or choice == "3":
            date = get_date_input()
            weather_data = get_weather_data(date)
            if weather_data:
                print_weather_data(weather_data, date, choice)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
