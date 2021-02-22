import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_ENDPOINT = os.environ.get("SHEETY_API")
SHEETY_HEADERS = {
    "Authorization": os.environ.get('SHEETY_AUTH')
}
sheety_response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADERS)

print(sheety_response.text)