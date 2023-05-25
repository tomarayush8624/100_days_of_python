import requests
from pprint import pprint

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADER = {
    "apiKey": "_lYiPJsOpTd0g9sMhyt8X8zMWwOiFBD2",
}
CONFIG = {
            "location_types": "city",
            "limit": 1,
        }
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data ={}

    def get_city_info(self, name):


        # name = "london"
        CONFIG["term"] = name
        response = requests.get(url=ENDPOINT, headers=HEADER, params=CONFIG)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]


    def get_flight_info(self):
