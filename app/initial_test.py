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
import pandas as pd
import urllib.request # potentially for displaying images
from PIL import Image # potentially for displaying images
# need to add Pillow to requirements.txt if it does work 


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

# Capturing Errors for Price Limit inputs (Condense and make more efficient) 
while True: 
    price_limit = input("What is your price limit on any single meal ($, $$, $$$, or $$$$)?")
    counter_price = len(price_limit)
    if price_limit.isnumeric() == True: 
        print("Oops, that's an invalid input. Please try again!")
        exit()
    elif price_limit.isalpha() == True: 
        print("Oops, that's an invalid input. Please try again!")
        exit()
    elif counter_price > 4:
        print("Oops, that's an invalid input. Please try again!")
        exit()
    else: 
        break

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
# FYI when we do a search with categories ['chinese', 'american'] Yelp returns either chinese OR american. 
# Not restaurants that are a fusion or combination of both
# This is just how the Yelp API works, not sure if we can change it 

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

for num in range(0,counter_price):
    prices.append(str(num + 1))


# Limit for breakfast params 
vacation_days = int(days)
#total_vacation_meals = (vacation_days) * 3

# Inserting images 


#OUPUT - list for breakfast
breakfast = []
breakfast_parameters = {'term': 'breakfast',
              'limit': vacation_days, # 1 breakfast per vacation day  
              'offset': 50, #basically lets you do pages
              'price': prices, #can change this later
              'radius': 10000, #Change later?
              'categories': food_list, 
              'location': destination}


business_list = get_response(link_endpoint, breakfast_parameters, link_headers)


# Capturing errors for business list (if matches were found, business list = 0)
while True: 
    if len(business_list)==0:
        print("No results for your criteria were found. Please try again!")
        break
    else: 
        break


a_dict = { }

for biz in business_list:
    #print("Restauraunt:", biz['name'], "| Category:", biz['categories'][0]['title'])
    a_dict['Restaurant']=biz['name']
    a_dict['Category']=biz['categories'][0]['title']
    print(a_dict)
    #breakfast.append(biz['name'])
    #breakfast.append(biz['categories'][0]['title'])
    #image_url = biz['image_url']
    #image = Image.open(urllib.request.urlopen(image_url))
    #print(image) 
    # displaying images does not work yet - need to figure out

# merging name and category list elements to be one 
# this method is hard because we have to specifiy 1, 2, 3 for each and the list is always changing
# will try dictionary instead 



#OUPUT - list for lunch

#OUPUT - list for dinner



# Breakfast, Lunch, & Dinner in one Dataframe 

#meal_itinerary_df = pd.DataFrame(
#    {
#        "Breakfast": []
#        "Lunch":
#        "Dinner":
#    }
#
#)



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