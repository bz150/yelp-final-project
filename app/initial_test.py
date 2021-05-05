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
#from PIL import Image # potentially for displaying images
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
    if price_limit != "$" and price_limit != "$$" and price_limit != "$$$" and price_limit != "$$$$":
        print("Oops, that's an invalid input. Please try again!")
        exit()
    else:
        break


#for testing, change later
#Create list for food preferences
#VALIDATE CATEGORY ENTRIES FROM USER (try / except function?)
food_variable = True
food_list = []
while food_variable == True:
    food_preference = input("What types of food do you like? (Select all that apply, say DONE when done) ...coffee, Chinese, American, Italian?")
    food_list.append(food_preference)
    if "DONE" in food_list:
        food_list.remove("DONE")
        food_variable = False

# Sturcture new food inputs as one comma delimited string
food_list_structured = ""
for x in food_list:
    if x != food_list[0]:
        food_list_structured = str(food_list_structured + "," + x)
    elif x == food_list[0]:
        food_list_structured = str(x)

#Create list for price
prices = []

for num in range(0,counter_price):
    prices.append(str(num + 1))

# Limit for breakfast params 
vacation_days = int(days)
#total_vacation_meals = (vacation_days) * 3


#
# BREAKFAST
#

#OUPUT - dictionary for breakfast
breakfast_list = []
breakfast_dict = { }

breakfast_parameters = {'term': 'breakfast',
              'limit': vacation_days, # 1 breakfast per vacation day  
              'offset': 50, #basically lets you do pages
              'price': prices, #can change this later
              'radius': 10000, #Change later?
              'categories': food_list_structured,
              'location': destination
              }

breakfast_list = get_response(link_endpoint, breakfast_parameters, link_headers)

# Capturing errors for breakfast list (if matches were found, breakfast list = 0)
while True: 
    if len(breakfast_list)==0:
        print("No results for your criteria were found. Please try again!")
        break
    else: 
        break

for biz in breakfast_list:
    #print("Restauraunt:", biz['name'], "| Category:", biz['categories'][0]['title'])
    breakfast_dict['Restaurant']=biz['name']
    breakfast_dict['Category']=biz['categories'][0]['title']
    print(breakfast_dict)
    #breakfast_list.append(breakfast_dict)
    #image_url = biz['image_url']
    #image = Image.open(urllib.request.urlopen(image_url))
    #print(image) 
    # displaying images does not work yet - need to figure out


#OUPUT - LUNCH
lunch_list = []
lunch_dict = { }

lunch_parameters = {'term': 'lunch',
              'limit': vacation_days, 
              'offset': 50, #basically lets you do pages
              'price': prices, #can change this later
              'radius': 10000, #Change later?
              'categories': food_list_structured,
              'location': destination
              }

lunch_list = get_response(link_endpoint, lunch_parameters, link_headers)

# Capturing errors for lunch list
while True: 
    if len(lunch_list)==0:
        print("No results for your criteria were found. Please try again!")
        break
    else: 
        break

for biz in lunch_list:
    lunch_dict['Restaurant']=biz['name']
    lunch_dict['Category']=biz['categories'][0]['title']
    print(lunch_dict)


#OUPUT - DINNER
dinner_list = []
dinner_dict = { }

dinner_parameters = {'term': 'dinner',
              'limit': vacation_days, 
              'offset': 50, #basically lets you do pages
              'price': prices, #can change this later
              'radius': 10000, #Change later?
              'categories': food_list_structured,
              'location': destination
              }

dinner_list = get_response(link_endpoint, dinner_parameters, link_headers)

# Capturing errors for dinner list
while True: 
    if len(dinner_list)==0:
        print("No results for your criteria were found. Please try again!")
        break
    else: 
        break

for biz in dinner_list:
    dinner_dict['Restaurant']=biz['name']
    dinner_dict['Category']=biz['categories'][0]['title']
    print(dinner_dict)



#
# PIN'S WORK ON OUTPUT BELOW
#


# Compiled Breakfast, Lunch, & Dinner in one Dataframe 

#meal_itinerary_df = pd.DataFrame(breakfast_list)
#print(meal_itinerary_df)





#
# REFERENCE DATA STRUCTURE
#

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

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
#link_parameters = {'term': 'food',
#              'limit': 50,
#              'offset': 50, #basically lets you do pages
#              'radius': 10000,
#              'location': 'San Diego'}

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

