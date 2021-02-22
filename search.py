import requests
import os
from dotenv import load_dotenv
load_dotenv()

TEQUILA_URL = os.environ.get("KIWI_TEQUILA_URL")
TEQUILA_ENDPOINT = f"{TEQUILA_URL}/locations/query"
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