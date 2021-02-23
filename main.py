from data import LookUpData
from search import Search
from notifications import Notification
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Class Instances
lookup_data = LookUpData()
search = Search()
notification = Notification()

# Get the lookup data
sheety_data = lookup_data.get_data()


# Check if IATA Code column is empty
if sheety_data[0]['iataCode'] == '':
    for row in sheety_data:
        row['iataCode'] = search.get_code(row['city'])
    lookup_data.data = sheety_data
    lookup_data.update_iata_code()


# Get tomorrow's date and the date in 6 months time
tomorrow = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow.strftime("%d/%m/%Y")
six_months = tomorrow + relativedelta(months=+6)
six_months_time = six_months.strftime("%d/%m/%Y")

ORIGIN_CITY_IATA = "DUB"

for destination in sheety_data:
    flight = search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow_date,
        to_time=six_months_time
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        # notification.send_email(
        #     message=f"Low price alert! "
        #             f"Only {flight.price}(EUR) to fly from {flight.origin_city}-{flight.origin_airport} to "
        #             f"{flight.destination_city}-{flight.destination_airport}, "
        #             f"from {flight.out_date} to {flight.return_date}. "
        #             f"From: A3AJAGBE LOW FLIGHTY"
        # )
        # notification.send_sms(
        #     message=f"Low price alert! "
        #             f"Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
        #             f"{flight.destination_city}-{flight.destination_airport}, "
        #             f"from {flight.out_date} to {flight.return_date}. "
        # )
        print(f"{flight.price} for {flight.destination_city}")
