import requests
from datetime import datetime
from decouple import config

APP_ID = config("app_id")
API_KEY = config("api_key")
ENDPOINT_NUTRI = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "MALE"
WEIGHT_KG = config("weight")
HEIGHT_CM = config("height")
AGE = config("age")

time_data = datetime.now()
date = time_data.strftime("%d/%m/%Y")
# print(date)
time = time_data.strftime('%H:%M:%S')
# print(time)

input_query = input("Tell me which exercise you did: ")
# input_query = "Ran 2 miles and walked for 3 km"
header_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

config_nutri = {
    "query": input_query,
    "gender": "male",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=ENDPOINT_NUTRI, headers=header_nutri, json=config_nutri)
nutri_json = response.json()["exercises"]
# print(nutri_json)

sheety_endpoint = config("sheety_endpoint")
header_sheety = {
    "Authorization": config("sheety_auth")
}

for i in nutri_json:
    exercise = i["user_input"].title()
    duration = i["duration_min"]
    calories = i["nf_calories"]

config_sheety = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

print(config_sheety["workout"]["exercise"])

response1 = requests.post(url=sheety_endpoint, headers=header_sheety, json=config_sheety)
print(response1.text)
