import requests
from pprint import pprint


SERVER = "https://api.tequila.kiwi.com/"
HEADER = {
    "apiKey": "_lYiPJsOpTd0g9sMhyt8X8zMWwOiFBD2",
}

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        # self.data = {}
        pass

    def get_rel_info(self, data):
        endpoint_location = f"{SERVER}/locations/query"
        for i in data:
            config_info = {
                "term": f"{i['city']}",
                "location_types": "country",
                "limit": 10,
            }
            print(config_info)
            response_city_details = requests.get(url=endpoint_location, headers=HEADER, params=config_info)
            response_city_details.raise_for_status()
            pprint(response_city_details.json())
