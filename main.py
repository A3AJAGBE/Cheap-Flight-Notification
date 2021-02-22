from data import LookUpData
from search import Search
from pprint import pprint

# Class Instances
lookup_data = LookUpData()
search = Search()

# Get the lookup data
sheety_data = lookup_data.get_data()
# print(sheety_data)
# To print a formatted data
# pprint(sheety_data)

# Check if IATA Code column is empty
if sheety_data[0]['iataCode'] == "":
    for row in sheety_data:
        row['iataCode'] = search.get_code(row['city'])
    print(f"Data: \n{sheety_data}")

    lookup_data.data = sheety_data
    lookup_data.update_iate_code()




