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
        print(f"No flights found.")
        continue

    if flight.price < destination["lowestPrice"]:

        members = lookup_data.get_member_emails()
        emails = [member["email"] for member in members]
        first_names = [member["firstName"] for member in members]

        message = f"A3AJAGBE LOW FLIGHT NOTIFICATION\n" \
                  f"Only €{flight.price} to fly from {flight.origin_city} ({flight.origin_airport} Airport)" \
                  f" to {flight.destination_city} ({flight.destination_airport} Airport), " \
                  f"from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nThere's a stop over for this flight, via {flight.via_city}."

        google_link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date} "
        notification.send_email(message, emails, google_link)
    else:
        print(f"Flight price to {flight.destination_city} higher than target price.")

