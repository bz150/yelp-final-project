# source: https://github.com/areed1192/sigma_coding_youtube/blob/master/python/python-api/yelp-api/Yelp%20API%20-%20Business%20Search.py

#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

# Import the modules
import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()

# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = os.environ.get("YELP_API_KEY")

#ENDPOINT = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
PARAMETERS = {'term': 'food',
              'limit': 50,
              'offset': 50, #basically lets you do pages
              'radius': 10000,
              'location': 'San Diego'}

# BUSINESS MATCH PARAMETERS - EXAMPLE
#PARAMETERS = {'name': 'Peets Coffee & Tea',
#              'address1': '7845 Highland Village Pl',
#              'city': 'San Diego',
#              'state': 'CA',
#              'country': 'US'}

# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String to a dictionary
parsed_response = json.loads(response.text)
businesses = parsed_response["businesses"]
#business_data = response.json()
#print(parsed_response.keys())
#print(parsed_response)

for biz in businesses:
    print(biz['name'])


#for biz in business_data['businesses']:
#    print(biz['name'])
# print the response
#print(json.dumps(business_data, indent = 3))


# FULL LIST OF PARAMS

#PARAMETERS = {'term':'good food',
#    'location':'San Diego',
#    'latitude':32.7,
#    'longitude':-117,
#    'radius':10000,
#    'categories':'bars,french',
#    'locale':'en_US',
#    'limit':50,
#    'offset':150,
#    'sort_by':'best_match',
#    'price':'1',
#    'open_now':True,
#    'open_at':unix_time,
#    'attributes':'hot_and_new'
#    }