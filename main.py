from data import LookUpData
from search import Search

# Class Instances
lookup_data = LookUpData()
search = Search()

# Get the lookup data
sheety_data = lookup_data.get_data()

# Check if IATA Code column is empty
if sheety_data[0]['iataCode'] == '':
    for row in sheety_data:
        row['iataCode'] = search.get_code(row['city'])
    lookup_data.data = sheety_data
    lookup_data.update_iata_code()

