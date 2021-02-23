import requests
import os
from flight_info import FlightInfo
from dotenv import load_dotenv

load_dotenv()

TEQUILA_URL = os.environ.get("KIWI_TEQUILA_URL")
TEQUILA_ENDPOINT = f"{TEQUILA_URL}/locations/query"
TEQUILA_SEARCH_ENDPOINT = f"{TEQUILA_URL}/v2/search"
HEADERS = {
    "apikey": os.environ.get("KIWI_TEQUILA_API")
}


class Search:

    def get_code(self, city):
        """This function adds the city IATA CODE"""
        PARAMETERS = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(TEQUILA_ENDPOINT, headers=HEADERS, params=PARAMETERS)
        data = response.json()['locations']
        for d in data:
            code = d['code']
            return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """This function checks for flight"""
        PARAMETERS = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "EUR"
        }

        response = requests.get(TEQUILA_SEARCH_ENDPOINT, headers=HEADERS, params=PARAMETERS)
        try:
            data = response.json()['data'][0]
        except IndexError:
            return None

        flight_info = FlightInfo(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs=1,
            via_city=data["route"][0]["cityTo"]
        )
        return flight_info
