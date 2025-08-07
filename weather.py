from weather_utils import fetch_weather

def display_weather(data):
    print("\n📍 City:", data["city"])
    print("🌡️ Temperature:", data["temperature"], "°C")
    print("☁️ Description:", data["description"].capitalize())
    print("💧 Humidity:", data["humidity"], "%")
    print("🍃 Wind Speed:", data["wind_speed"], "m/s")
    print("-" * 40)

def main():
    print("==== Weather Dashboard ====\n")

    while True:
        city = input("Enter city name (or 'q' to quit): ").strip()
        if city.lower() == 'q':
            print("Exiting Weather Dashboard. 👋")
            break

        data = fetch_weather(city)
        if data:
            display_weather(data)
        else:
            print("❌ Error: City not found or API issue.")

if __name__ == "__main__":
    main()
