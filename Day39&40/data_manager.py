import requests
import config

SHEETY_ENDPOINT = config.Sheety_Endpoint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        pass

    def get_data(self):
        """Gets Google Sheet data using API request and returns the json file"""
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_IATA_data(self, destination):
        """Updates the IATA code in the Google Sheet for the destination called"""
        new_data = {
            "price": {
                "iataCode": destination["iataCode"]
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{destination['id']}", json=new_data)
        # print(response.text)

    def update_price_data(self, destination, price):
        """Updates the price with the new lowest price found"""
        new_data = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{destination['id']}", json=new_data)
        # print(response.text)
        print(f"Updating price data for {destination['city']}...")
