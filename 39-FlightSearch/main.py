import requests
from pprint import pprint
from data_manager import DataManager


data_manager = DataManager()
sheet_data_lst = data_manager.get_sheet_data()


##These lines will add iata code to the respective country names

# for i in sheet_data_lst:
#     if i["iataCode"] == "":
#         from flight_search import FlightSearch
#         flight = FlightSearch()
#         iata_code = flight.get_city_info(i["city"])
#         i["iataCode"] = iata_code
#
# data_manager.update_sheet_data()

from flight_search import FlightSearch
flight = FlightSearch()
flight.get_flight_info(data=sheet_data_lst)


