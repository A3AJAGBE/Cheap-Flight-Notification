import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Sheety configs
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_MEMBER_ENDPOINT = os.environ.get("SHEETY_MEMBER_ENDPOINT")
SHEETY_HEADERS = {
    "Authorization": os.environ.get('SHEETY_AUTH')
}


class LookUpData:

    def __init__(self):
        self.data = {}
        self.member_data = {}

    def get_data(self):
        """This function get the data from the google sheets using sheety"""
        sheety_response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = sheety_response.json()
        self.data = data['prices']
        return self.data

    def update_iata_code(self):
        """This add the city's IATA Code"""
        for city in self.data:
            update_code = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            PUT_ENDPOINT = f"{SHEETY_ENDPOINT}/{city['id']}"
            response = requests.put(PUT_ENDPOINT, json=update_code, headers=SHEETY_HEADERS)
            print(response.text)

    def get_member_emails(self):
        """This function gets the member emails"""
        response = requests.get(SHEETY_MEMBER_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.member_data = data["members"]
        return self.member_data
