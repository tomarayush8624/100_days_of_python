import requests
from urllib import request,response
from pprint import pprint
from datetime import datetime

ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADER = {
    # "apiKey": "_lYiPJsOpTd0g9sMhyt8X8zMWwOiFBD2",
    "apiKey": "HtR3ra240KaaEvQaxHE0WrN94yhgG2po",
}
CONFIG = {
    "location_types": "city",
    "limit": 1,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data = {}
        self.search_config = {}

    # def get_city_info(self, name):
    #     # name = "london"
    #     CONFIG["term"] = name
    #     response = requests.get(url=ENDPOINT, params=CONFIG, headers=HEADER)
    #     response.raise_for_status()
    #
    #     return response.json()["locations"][0]["code"]

    def get_flight_info(self, data):

        day, month, year = int(datetime.today().strftime('%d')), int(datetime.today().strftime('%m')), int(
            datetime.today().strftime('%Y'))

        month1 = month + 6
        year1 = year
        if month1 > 12:
            month1 = month % 12
            year1 = year + 1

        print(f"{day + 1}/{month}/{year}")
        print(f"{day}/{month1}/{year1}")
        for i in data:
            self.search_config = {
                "fly_from": "LON",
                "fly_to": f"{i['iataCode']}",
                "date_from": "28/05/2023",
                "date_to": "25/06/2023",
                # "flight_type": "round",
                # "curr": "GBP",
            }
            print(self.search_config)
        data = requests.get(url=SEARCH_ENDPOINT, headers=HEADER, params=self.search_config)
        data.raise_for_status()
        print(data.json())
