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


def get_response(response_endpoint, response_parameters, response_headers):
    # Make a request to the Yelp API
    response = requests.get(url = response_endpoint,
                            params = response_parameters,
                            headers = response_headers)

    # Conver the JSON String to a dictionary
    parsed_response = json.loads(response.text)
    businesses_list = parsed_response["businesses"]
    return businesses_list



# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = os.environ.get("YELP_API_KEY")

#ENDPOINT = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)
link_endpoint = 'https://api.yelp.com/v3/businesses/search'
link_headers = {'Authorization': 'bearer %s' % API_KEY}

#INPUTS - read in user inputs
destination = input("Where is the destination of your vacation?")
days = input("How many days is your vacation?")
price_limit = input("What is your price limit on any single meal ($, $$, $$$, or $$$$)?")
#for testing, change later
#Create list for food preferences
food_variable = True
food_list = []
while food_variable == True:
    food_preference = input("What types of food do you like? (Select all that apply, say DONE when done) ...coffee, Chinese, American, Italian?")
    food_list.append(food_preference)
    if "DONE" in food_list:
        food_list.remove("DONE")
        food_variable = False 


# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
link_parameters = {'term': 'food',
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


#businesses = parsed_response["businesses"]
#business_data = response.json()
#print(parsed_response.keys())
#print(parsed_response)

#for biz in businesses:
#    print(biz['name'])


#Create list for price
prices = []
counter_price = len(price_limit)
for num in range(0,counter_price):
    prices.append(str(num + 1))

# prices should be integers 



#OUPUT - list for breakfast
breakfast = []
breakfast_parameters = {'term': 'breakfast',
              'limit': 50, 
              'offset': 50, #basically lets you do pages
              'price': prices, #can change this later
              'radius': 10000, #Change later?
              'categories': food_list, # we don't want the DONE keyword in
              'location': destination}


# compile this price properly 


business_list = get_response(link_endpoint, breakfast_parameters, link_headers)
#print(business_list[0].keys())

while True: 
    if len(business_list)==0:
        print("No results for your criteria were found. Please try again!")
        break
    else:
        print(business_list[0].keys())
        break


# if list index is out of range, we want to return an error: not found


for biz in business_list:
    print(biz['name'])
    print(biz['categories'])
    # if we input 2+ categories, Yelp will search for one OR the other 



#OUPUT - list for lunch

#OUPUT - list for dinner




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