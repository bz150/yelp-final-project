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

from dotenv import load_dotenv
load_dotenv()

def sort_meal_list(meal_list):
    """
    Sorts, fetches information, and adds title from a given list of responses retrieved from the Yelp API.

    Params:
        meal_list (list) the parsed response list for a certain meal, likt breakfast_list[]
    
    Example:
        sorted_list = sort_meal_list(breakfast_list)

    Returns the sorted list of outputs with the corresponding titles through "sorted_list"
    """
    sorted_list = []
    for biz in meal_list: 
        sorted_list.append("Restaurant: " + biz['name'] + " | Category: " + biz['categories'][0]['title'] + " | Location: " + biz['location']['address1'] + " | Rating: " + str(biz['rating']) + " | Price: " + biz['price'])
    return sorted_list



def get_response(destination, days_input, price_limit, food_preference):
    """
    Fetches restaurant results information from the Yelp API, for a given destination, number of days, price limit, and food preference.

    Params:
        destination (str) the requested destination, like "New York"
        days_input (int) the number of days of the vacation, like 3
        price_limit (list) the requested list of prices to search going up to the price limit, like [1,2,3] (for $$$)
        food_preference (str) the requested food cuisine preferences, like "American, Chinese"

    Example:
        breakfast_list, lunch_list, dinner_list = get_response(destination="New York", days_input=3, price_limit=[1,2,3], food_preference="American, Chinese")

    Returns the restaurant information for breakfast, lunch, and dinner through "breakfast_businesses_list", "lunch_businesses_list", "dinner_businesses_list" for the number of vacation days 
    """
    #ACQUIRE API KEY
    API_KEY = os.environ.get("YELP_API_KEY")

    #Endpoint and headers using API Key
    link_endpoint = 'https://api.yelp.com/v3/businesses/search'
    link_headers = {'Authorization': 'bearer %s' % API_KEY}
    
    #BREAKFAST REQUEST
    #Make breakfast parameters
    ###breakfast_list = []
    
    #Read in parameters for the breakfast request using the inputs
    breakfast_parameters = {'term': 'breakfast',
              'limit': days_input, # 1 breakfast per vacation day  
              'offset': 50, #basically lets you do pages
              'price': price_limit, #can change this later
              'radius': 10000, #Change later?
              'categories': food_preference,
              #'categories': [{"alias":"Japanese", "title":"Japanese"}, {"alias":"Mexican", "title":"Mexican"}],
              #'categories': "Italian, Japanese",
              'location': destination,
              'attributes':'good_for_breakfast',
              }


    # Make a request to the Yelp API for breakfast
    breakfast_response = requests.get(url = link_endpoint,
                            params = breakfast_parameters,
                            headers = link_headers)

    # Convert the JSON String to a dictionary for breakfast
    breakfast_parsed_response = json.loads(breakfast_response.text)
    breakfast_businesses_list = breakfast_parsed_response["businesses"]

    #LUNCH REQUEST
    ###lunch_list = []

    #Read in parameters for the lunch request using the inputs
    lunch_parameters = {'term': 'lunch',
                'limit': days_input, 
                'offset': 50, #basically lets you do pages
                'price': price_limit, #can change this later
                'radius': 10000, #Change later?
                'categories': food_preference,
                #'categories': [{"alias":"American", "title":"American"}],
                #'categories': [{"alias":"Italian", "title":"Italian"}, {"alias":"Mexican", "title":"Mexican"}],
                #'categories': "Italian, Japanese",
                'location': destination,
                'attributes':'good_for_lunch'
                }

    # Make a request to the Yelp API for lunch
    lunch_response = requests.get(url = link_endpoint,
                            params = lunch_parameters,
                            headers = link_headers)

    # Convert the JSON String to a dictionary for lunch
    lunch_parsed_response = json.loads(lunch_response.text)
    lunch_businesses_list = lunch_parsed_response["businesses"]

    #DINNER REQUEST
    ###dinner_list = []

    #Read in parameters for the dinner request using the inputs
    dinner_parameters = {'term': 'dinner',
              'limit': days_input, 
              'offset': 50, #basically lets you do pages
              'price': price_limit, #can change this later
              'radius': 10000, #Change later?
              'categories': food_preference,
              #'categories': [{"alias":"American", "title":"American"}],
              #'categories': [{"alias":"Japanese", "title":"Japanese"}, {"alias":"Mexican", "title":"Mexican"}],
              #'categories': "Italian, Japanese",
              'location': destination,
              'attributes':'good_for_dinner'
              }
    # Make a request to the Yelp API for dinner
    dinner_response = requests.get(url = link_endpoint,
                            params = dinner_parameters,
                            headers = link_headers)

    # Convert the JSON String to a dictionary for breakfast
    dinner_parsed_response = json.loads(dinner_response.text)
    dinner_businesses_list = dinner_parsed_response["businesses"]

    #Return separate breakfast, lunch, and dinner lists
    return breakfast_businesses_list, lunch_businesses_list, dinner_businesses_list


if __name__ == "__main__":

    #Create lists to hold the breakfast, lunch, and dinner results
    breakfast_list = []
    lunch_list = []
    dinner_list = []
    #def get_response(response_endpoint, response_parameters, response_headers):
    #    # Make a request to the Yelp API
    #    response = requests.get(url = response_endpoint,
    #                            params = response_parameters,
    #                            headers = response_headers)
    #
    #    # Conver the JSON String to a dictionary
    #    parsed_response = json.loads(response.text)
    #    businesses_list = parsed_response["businesses"]
    #    return businesses_list
    #

    # Define my API Key, My Endpoint, and My Header
    #API_KEY = os.environ.get("YELP_API_KEY")
    #
    #link_endpoint = 'https://api.yelp.com/v3/businesses/search'
    #link_headers = {'Authorization': 'bearer %s' % API_KEY}

    #CAN POTENTIALLY TURN THE INPUTS INTO A FUNCTION

    #INPUTS - read in user inputs
    #Read in the user's destination and number of days for vacation
    destination = input("Where is the destination of your vacation? ")
    days = input("How many days is your vacation? ")

    #
    # Capturing Errors for Price Limit inputs and validating input 
    while True: 
        price_limit = input("What is your price limit on any single meal ($, $$, $$$, or $$$$)? ")
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
    #Stop asking for food preference inputs when user says DONE
    while food_variable == True:
        food_preference = input("What types of food do you like? (Select all that apply, say DONE when done) ...coffee, Chinese, American, Italian? " )
        food_list.append(food_preference.lower())
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

    #Add price limit (and all prices after) into the price list
    for num in range(0, counter_price):
        prices.append(str(num + 1))

    # Change the vacation days input into an integer
    vacation_days = int(days)


    #CALLING THE REQUESTS FROM THE FUNCTION and reading into breakfast, lunch, dinner lists
    breakfast_list, lunch_list, dinner_list = get_response(destination, vacation_days, prices, food_list_structured)


    #
    # OUPUT - BREAKFAST
    #

    #breakfast_list = []
    #
    #breakfast_parameters = {'term': 'breakfast',
    #              'limit': vacation_days, # 1 breakfast per vacation day  
    #              'offset': 50, #basically lets you do pages
    #              'price': prices, #can change this later
    #              'radius': 10000, #Change later?
    #              'categories': food_list_structured,
    #              'location': destination,
    #              'attributes':'good_for_breakfast',
    #              #'open_at':1620226800
    #              }
    #
    #breakfast_list = get_response(link_endpoint, breakfast_parameters, link_headers)

    #Capturing errors for breakfast list if not enough results found
    while True: 
        if len(breakfast_list)==0:
            print("No results for your criteria were found. Please try again!")
            break
        else: 
            break
    #Create list for breakfast list with titles of each output
    sorted_breakfast_list = [ ]
    #Go through breakfast list and add outputs to the sorted list

    #for biz in breakfast_list: 
    #    sorted_breakfast_list.append("Restaurant: " + biz['name'] + " | Category: " + biz['categories'][0]['title'] + " | Location: " + biz['location']['address1'] + " | Rating: " + str(biz['rating']) + " | Price: " + biz['price'])

    sorted_breakfast_list = sort_meal_list(breakfast_list)

    #Capturing errors for lunch list if not enough results found
    while True: 
        if len(lunch_list)==0:
            print("No results for your criteria were found. Please try again!")
            break
        else: 
            break
    
    #Create list for lunch with titles of each output
    sorted_lunch_list = [ ]
    #Go through lunch list and add outputs to the sorted list

    #for biz in lunch_list: 
    #    sorted_lunch_list.append("Restaurant: " + biz['name'] + " | Category: " + biz['categories'][0]['title'] + " | Location: " + biz['location']['address1'] + " | Rating: " + str(biz['rating']) + " | Price: " + biz['price'])

    sorted_lunch_list = sort_meal_list(lunch_list)

    #
    # OUPUT - DINNER
    #

    #dinner_list = []
    #
    #dinner_parameters = {'term': 'dinner',
    #              'limit': vacation_days, 
    #              'offset': 50, #basically lets you do pages
    #              'price': prices, #can change this later
    #              'radius': 10000, #Change later?
    #              'categories': food_list_structured,
    #              'location': destination,
    #              'attributes':'good_for_dinner'
    #              }
    #
    #dinner_list = get_response(link_endpoint, dinner_parameters, link_headers)

    #Capturing errors for dinner list if not enough results found
    while True: 
        if len(dinner_list)==0:
            print("No results for your criteria were found. Please try again!")
            break
        else: 
            break

    #Create list for dinner with titles of each output
    sorted_dinner_list = [ ]

    #Go through dinner list and add outputs to the sorted list

    #for biz in dinner_list: 
    #    sorted_dinner_list.append("Restaurant: " + biz['name'] + " | Category: " + biz['categories'][0]['title'] + " | Location: " + biz['location']['address1'] + " | Rating: " + str(biz['rating']) + " | Price: " + biz['price'])
    sorted_dinner_list = sort_meal_list(dinner_list)



    #WEB APP OUTPUT
    #print(f"RUNNING THE WEATHER SERVICE IN {APP_ENV.upper()} MODE...")

    #
    # FINAL OUTPUT BELOW
    #Print final output
    print(" breakfast")
    print(sorted_breakfast_list)
    print(" lunch")
    print(sorted_lunch_list)
    print(" dinner")
    print(sorted_dinner_list)

    #breakpoint()

    #Add outputs to a dictionary
    meals_data = {
        'Breakfast': sorted_breakfast_list, 
        'Lunch': sorted_lunch_list, 
        'Dinner': sorted_dinner_list
    }

    #Turn outputs dictionary into a dataframe
    meal_itin_df = pd.DataFrame(meals_data)
    print(meal_itin_df)

    meal_itin_df.columns = ["Breakfast", "Lunch", "Dinner"]

    #
    # REFERENCE DATA STRUCTURE
    #

    #ENDPOINT = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)

    # Define a business ID
    #business_id = '4AErMBEoNzbk7Q8g45kKaQ'
    #unix_time = 1546047836


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

