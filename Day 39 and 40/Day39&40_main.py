# Day 39/40 Capstone Project - Flight Finder

from data_manager import DataManager
from flight_search import FlightSearch
# import pprint

data_manager = DataManager()  # Initialise DataManager only once
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
# pprint(sheet_data)

for i in range(len(sheet_data)):
    if sheet_data[i]["iataCode"]:
        #print(f"IATA code is {sheet_data[i]['iataCode']} for {sheet_data[i]['city']}")
        pass
    else:
        #print(f"IATA code does not exist for {sheet_data[i]['city']}")
        pass
        code = flight_search.get_IATA(sheet_data[i])
        sheet_data[i]["iataCode"] = code
        data_manager.update_IATA_data(sheet_data[i])

    flight = flight_search.check_flight(sheet_data[i], 'LON', 0)

    if flight is None:
        user_stopover = input(f"Unable to find flights to {sheet_data[i]['city']} with the specified parameters"
                              f"\nWould you like to search for flights with stopovers? Y/N ")
        if user_stopover == 'Y':
            flight = flight_search.check_flight(sheet_data[i], 'LON', 2)
            print(f"Flight found to {sheet_data[i]['city']} with a stopover via {flight.stopover_city}")
        else:
            continue

    if sheet_data[i]["lowestPrice"] > flight.price:
        data_manager.update_price_data(sheet_data[i], flight.price)

#pprint(sheet_data)
