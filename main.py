import requests
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
load_dotenv()

# Get tomorrow's date and the date in 6 months time
tomorrow = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow.strftime("%m/%d/%Y")
six_months = tomorrow + relativedelta(months=+6)
six_months_time = six_months.strftime("%m/%d/%Y")
print(tomorrow_date)
print(six_months_time)

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_HEADERS = {
    "Authorization": os.environ.get('SHEETY_AUTH')
}
sheety_response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADERS)

flight_data = sheety_response.text




