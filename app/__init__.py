
#
# this is the app/__init__.py file
#
# the presence of this file, even if empty,
# ... facilitates local imports from one file to another,
# ... including importing app code for testing purposes
#
#
#
#import os
#import requests
#import json
#import pandas as pd
#
#from dotenv import load_dotenv
#load_dotenv()
#
#
#def function(x):
#    return x+x
#
#def get_response(destination, days_input, price_limit, food_preference):
#    #ACQUIRE API KEY
#    API_KEY = os.environ.get("YELP_API_KEY")
#
#    link_endpoint = 'https://api.yelp.com/v3/businesses/search'
#    link_headers = {'Authorization': 'bearer %s' % API_KEY}
#    
#    #BREAKFAST REQUEST
#    #Make breakfast parameters
#    breakfast_list = []
#
#    breakfast_parameters = {'term': 'breakfast',
#              'limit': days_input, # 1 breakfast per vacation day  
#              'offset': 50, #basically lets you do pages
#              'price': price_limit, #can change this later
#              'radius': 10000, #Change later?
#              'categories': food_preference,
#              'location': destination,
#              'attributes':'good_for_breakfast',
#              }
#
#
#    # Make a request to the Yelp API for breakfast
#    breakfast_response = requests.get(url = link_endpoint,
#                            params = breakfast_parameters,
#                            headers = link_headers)
#
#    # Convert the JSON String to a dictionary for breakfast
#    breakfast_parsed_response = json.loads(breakfast_response.text)
#    breakfast_businesses_list = breakfast_parsed_response["businesses"]
#
#    #LUNCH REQUEST
#    lunch_list = []
#
#    lunch_parameters = {'term': 'lunch',
#                'limit': days_input, 
#                'offset': 50, #basically lets you do pages
#                'price': price_limit, #can change this later
#                'radius': 10000, #Change later?
#                'categories': food_preference,
#                'location': destination,
#                'attributes':'good_for_lunch'
#                }
#
#    # Make a request to the Yelp API for breakfast
#    lunch_response = requests.get(url = link_endpoint,
#                            params = lunch_parameters,
#                            headers = link_headers)
#
#    # Convert the JSON String to a dictionary for breakfast
#    lunch_parsed_response = json.loads(lunch_response.text)
#    lunch_businesses_list = lunch_parsed_response["businesses"]
#
#    #DINNER REQUEST
#
#    dinner_list = []
#
#    dinner_parameters = {'term': 'dinner',
#              'limit': days_input, 
#              'offset': 50, #basically lets you do pages
#              'price': price_limit, #can change this later
#              'radius': 10000, #Change later?
#              'categories': food_preference,
#              'location': destination,
#              'attributes':'good_for_dinner'
#              }
#    # Make a request to the Yelp API for breakfast
#    dinner_response = requests.get(url = link_endpoint,
#                            params = dinner_parameters,
#                            headers = link_headers)
#
#    # Convert the JSON String to a dictionary for breakfast
#    dinner_parsed_response = json.loads(dinner_response.text)
#    dinner_businesses_list = dinner_parsed_response["businesses"]
#
#
#
#    return breakfast_businesses_list, lunch_businesses_list, dinner_businesses_list
#
#
#
#
##def function(my_price):
##    """
##    Formats a number as currency (USD) with dollar sign, two decimals, and thousands separator
##    
##    Params: my_price (numeric, int or float) to be formatted
##    
##    Examples: to_usd(21.645)
##    """
##    return f"${my_price:,.2f}"
##