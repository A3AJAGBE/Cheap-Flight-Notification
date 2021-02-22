import requests
import os
from dotenv import load_dotenv
load_dotenv()


TEQUILA_ENDPOINT = os.environ.get("KIWI_TEQUILA_ENDPOINT")
TEQUILA_API = os.environ.get("KIWI_TEQUILA_API")


class Search:

    def get_code(self, city):
        """This function adds the city IATA CODE"""
        code = "Testing"
        return code