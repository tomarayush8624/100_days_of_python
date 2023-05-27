from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f2cb332113c0e4cac257da37cda93439/flightDeals/prices"
HEADER = {
    "Authorization": "Basic bnVsbDpudWxs"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=HEADER
            )
            print(response.text)
