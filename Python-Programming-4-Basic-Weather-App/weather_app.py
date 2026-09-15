import json
import os
import urllib.error
import urllib.parse
import urllib.request


def c_to_f(celsius):
    return (celsius * 9 / 5) + 32


def get_weather(city, api_key):
    query = urllib.parse.urlencode({"q": city, "appid": api_key, "units": "metric"})
    url = f"https://api.openweathermap.org/data/2.5/weather?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": "OIBSIP-Basic-Weather-App/1.0"})
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    print("=== Basic Weather App ===")
    city = input("Enter a city name or ZIP code: ").strip()
    if not city:
        print("Error: location cannot be empty.")
        return

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY is not set.")
        print("Set your OpenWeatherMap API key as an environment variable and run again.")
        return

    try:
        data = get_weather(city, api_key)
        temp_c = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print(f"Location: {data.get('name', city)}")
        print(f"Temperature: {temp_c:.1f} °C / {c_to_f(temp_c):.1f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
        print(f"Wind speed: {wind_speed} m/s")
    except urllib.error.HTTPError as exc:
        if exc.code == 401:
            print("Error: invalid API key.")
        elif exc.code == 404:
            print("Error: city/location not found.")
        else:
            print(f"Error: weather service returned HTTP {exc.code}.")
    except urllib.error.URLError:
        print("Error: network connection failed or timed out.")
    except (KeyError, json.JSONDecodeError):
        print("Error: unexpected weather API response.")


if __name__ == "__main__":
    main()
