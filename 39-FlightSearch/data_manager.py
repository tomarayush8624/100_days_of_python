import requests
from pprint import pprint

SHEETY_API = "https://api.sheety.co/f2cb332113c0e4cac257da37cda93439/flightDeals/prices"
HEADER = {
    "Authorization": "Basic bnVsbDpudWxs"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    # pass
    def __init__(self):
        # print("hi")
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_API, headers=HEADER)
        self.sheet_data = (response.json()["prices"])
        pprint(self.sheet_data)
        return self.sheet_data

    def update_sheet_data(self):
        # This function updates the data on Google sheet

        for i in self.sheet_data:
            update_api = f"{SHEETY_API}/{i['id']}"
            data = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            post_response = requests.put(url=update_api, headers=HEADER, json=data)
            post_response.raise_for_status()
