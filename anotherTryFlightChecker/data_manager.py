import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/f2cb332113c0e4cac257da37cda93439/flightDeals/prices"

HEADER = {
    "Authorization": "Bearer fdsfasdfasdfasdfsadf"
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=HEADER)
        response.raise_for_status()
        return response.json()["prices"]
