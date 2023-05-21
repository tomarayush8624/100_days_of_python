import requests

api_key = "367871d6b76fc79714d934a611a55bc3"
API_END = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "appid": api_key,
    "lat": "19.777456",
    "lon": "79.366264",
}
request = requests.get(API_END, params=parameters)
request.raise_for_status()
weather_data = request.json()
print(weather_data["list"][0]["weather"][0]["id"])
weather_codes = []
for i in range(15):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        print("bring am umbrella")
        break

