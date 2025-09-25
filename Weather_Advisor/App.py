# We import 'requests' so we can call a web address and get data back.
import requests

while True:
    # 1) Ask the user for a city name
    city = input("Type a city name (e.g., Perth): ").strip()

    # 🛑 Check: reject if empty or numbers
    if not city or city.isnumeric():
        print("Error: Please type a valid city name (letters, not just numbers).\n")
        continue  # go back to the top of the loop

    # 2) Build a special URL that returns weather in JSON (computer-friendly text).
    #    wttr.in is a free service that doesn’t need an API key.
    url = f"https://wttr.in/{city}?format=j1"

    try:
        # 3) Call the website
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        print("Network error. Please check your internet and try again.\n")
        continue

    # 4) If response is bad
    if response.status_code != 200:
        print("Weather service unavailable. Try again later.\n")
        continue

    # 5) Turn the downloaded text into a Python dictionary (JSON → dict).
    data = response.json()

    # 🛑 Extra check: if no valid current_condition in response
    if "current_condition" not in data:
        print("City not found in the database. Please try again.\n")
        continue

    # 6) Pick out the pieces we need:
    #    - current temperature in Celsius
    #    - a short description like "Partly cloudy"
    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    description = current["weatherDesc"][0]["value"]

    # 7) Print a simple sentence.
    print(f"{city}: {temp_c}°C, {description}" "\n" )
    continue
