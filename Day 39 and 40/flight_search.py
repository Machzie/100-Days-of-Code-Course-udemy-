import requests
from flight_data import FlightData
import datetime as dt
import config

FLT_SEARCH_API_KEY = config.Tequila_Key
FLT_SEARCH_ENDPOINT = config.Tequila_Endpoint
DT_NOW = dt.datetime.now()


class FlightSearch:
    def __init__(self):
        pass

    def get_IATA(self, destination):
        header = {
            "apikey": FLT_SEARCH_API_KEY
        }
        parameters = {
            "term": destination["city"],
            "location_types": "airport"
        }
        response = requests.get(url=f"{FLT_SEARCH_ENDPOINT}/locations/query", headers=header, params=parameters)
        IATA_code = response.json()["locations"][0]["id"]
        return IATA_code

    def check_flight(self, destination, origin_city_code, num_stopovers):
        header = {
            "apikey": FLT_SEARCH_API_KEY
        }
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination["iataCode"],
            "date_from": DT_NOW.strftime("%d/%m/%Y"),
            "date_to": (DT_NOW + dt.timedelta(3*30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "max_stopovers": num_stopovers,
            "curr": "GBP"
        }
        response = requests.get(url=f"{FLT_SEARCH_ENDPOINT}/search", headers=header, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            return None
        else:
            if num_stopovers == 0:
                layover_city = "None"
            else:
                layover_city = data["route"][0]["cityTo"]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["cityFrom"],
                origin_airport=data["flyFrom"],
                destination_city=data["cityTo"],
                destination_airport=data["flyTo"],
                out_date=dt.datetime.utcfromtimestamp(int(data["route"][0]["dTime"])).strftime("%d/%m/%Y"),
                return_date=dt.datetime.utcfromtimestamp(int(data["route"][0]["dTime"])).strftime("%d/%m/%Y"),
                stopover_city=layover_city
            )

        print(f"Price to {flight_data.destination_airport}: £{flight_data.price} on {flight_data.out_date}")
        return flight_data
