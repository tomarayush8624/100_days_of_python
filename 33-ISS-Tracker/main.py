import requests
import datetime
import time

MY_LAT = 26.751497
MY_LONG = 800.806197


def close_by():
    print("hi")
    if (MY_LAT - 5 <= float(latitude) >= MY_LAT + 5) and (MY_LONG - 5 <= float(latitude) >= MY_LONG + 5):
        print("nearby")
        if sunrise <= time_now >= sunset:
            print("dark")
            time.sleep(60)
            close_by()


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

position = (latitude, longitude)
print(position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.datetime.now().hour
print(time_now)
close_by()
