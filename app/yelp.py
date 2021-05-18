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



def get_request(term, destination, days_input, price_limit, food_preference):
    """
    Fetches restaurant information from the Yelp API for a given meal term, meal attribute, destination, number of days of vacation, price limit, and food preference.

    Params:
        term (str) the specific meal, like "breakfast"
        destination (str) the requested destination, like "New York"
        days_input (int) the number of days of the vacation, like 3
        price_limit (list) the requested list of prices to search going up to the price limit, like [1,2,3] (for $$$)
        food_preference (str) the requested food cuisine preferences, like "American, Chinese"

    Example:
        breakfast_list, lunch_list, dinner_list = get_request(term="breakfast",destination="New York", days_input=3, price_limit=[1,2,3], food_preference="American, Chinese")


    Returns the request for a specific meal through "meal_response".
    """
    #ACQUIRE API KEY
    API_KEY = os.environ.get("YELP_API_KEY")

    #Endpoint and headers using API Key
    link_endpoint = 'https://api.yelp.com/v3/businesses/search'
    link_headers = {'Authorization': 'bearer %s' % API_KEY}

    #Read in the inputted parameters for a given meal
    meal_parameters = {'term': term,
              'limit': days_input, # 1 breakfast per vacation day  
              'offset': 50, #basically lets you do pages
              'price': price_limit, #can change this later
              'radius': 10000, #Change later?
              'categories': food_preference,
              'location': destination,
              'attributes': "good_for_" + term,
              }
    
    #Make a request to the Yelp API using the correct parameters
    meal_response = requests.get(url = link_endpoint,
                            params = meal_parameters,
                            headers = link_headers)
    print(meal_response)
    
    #Return the request
    return meal_response


def get_response(destination, days_input, price_limit, food_preference):
    """
    Creates a list based on the restaurant results information from the get_request function, for a given destination, number of days, price limit, and food preference for each meal.

    Params:
        destination (str) the requested destination, like "New York"
        days_input (int) the number of days of the vacation, like 3
        price_limit (list) the requested list of prices to search going up to the price limit, like [1,2,3] (for $$$)
        food_preference (str) the requested food cuisine preferences, like "American, Chinese"

    Example:
        breakfast_list, lunch_list, dinner_list = get_response(destination="New York", days_input=3, price_limit=[1,2,3], food_preference="American, Chinese")

    Returns the restaurant information list for breakfast, lunch, and dinner through "breakfast_businesses_list", "lunch_businesses_list", "dinner_businesses_list" for the number of vacation days. 
    """
    
    #BREAKFAST REQUEST
    #Get breakfast request using the correct term and attribute
    breakfast_term = 'breakfast'
    breakfast_response = get_request(breakfast_term, destination, days_input, price_limit, food_preference)
    # Convert the JSON String to a dictionary for breakfast
    breakfast_parsed_response = json.loads(breakfast_response.text)
    breakfast_businesses_list = breakfast_parsed_response["businesses"]
    
    #LUNCH REQUEST
    #Get lunch request using the correct term and attribute
    lunch_term = 'lunch'
    lunch_response = get_request(lunch_term, destination, days_input, price_limit, food_preference)
    # Convert the JSON String to a dictionary for lunch
    lunch_parsed_response = json.loads(lunch_response.text)
    lunch_businesses_list = lunch_parsed_response["businesses"]
    #DINNER REQUEST
    #Get dinner request using the correct term and attribute
    dinner_term = 'dinner'
    dinner_response = get_request(dinner_term, destination, days_input, price_limit, food_preference)
    
    # Convert the JSON String to a dictionary for dinner
    dinner_parsed_response = json.loads(dinner_response.text)
    dinner_businesses_list = dinner_parsed_response["businesses"]
    #Return separate breakfast, lunch, and dinner lists
    return breakfast_businesses_list, lunch_businesses_list, dinner_businesses_list

       
    


if __name__ == "__main__":

    #Create lists to hold the breakfast, lunch, and dinner results
    breakfast_list = []
    lunch_list = []
    dinner_list = []

    #INPUTS - read in user inputs
    #Read in the user's destination and number of days for vacation
    destination = input("Where is the destination of your vacation? ")
    days = input("How many days is your vacation? ")

    # Capturing Errors for Price Limit inputs and validating input 
    while True: 
        price_limit = input("What is your price limit on any single meal ($, $$, $$$, or $$$$)? ")
        counter_price = len(price_limit)
        if price_limit != "$" and price_limit != "$$" and price_limit != "$$$" and price_limit != "$$$$":
            print("Oops, that's an invalid input. Please try again!")
            exit()
        else:
            break

    
    #Create list for food preferences
    food_variable = True
    food_list = []
    #Stop asking for food preference inputs when user says DONE
    while food_variable == True:
        food_preference = input("What types of food do you like? (Select one at a time, say DONE when done) Chinese, American, Italian, Japanese, Mexican, and/or Mediterranean? " )
        food_list.append(food_preference.lower())
        if "done" in food_list:
            food_list.remove("done")
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

    try:
        #CALLING THE REQUESTS FROM THE FUNCTION and reading into breakfast, lunch, dinner lists
        breakfast_list, lunch_list, dinner_list = get_response(destination, vacation_days, prices, food_list_structured)
        # OUPUT - BREAKFAST
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
        sorted_breakfast_list = sort_meal_list(breakfast_list)
        # OUPUT - LUNCH
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
        sorted_lunch_list = sort_meal_list(lunch_list)
        
        
        # OUPUT - DINNER
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
        sorted_dinner_list = sort_meal_list(dinner_list)
        # FINAL OUTPUT BELOW
        #Add outputs to a dictionary
        meals_data = {
            'Breakfast': sorted_breakfast_list, 
            'Lunch': sorted_lunch_list, 
            'Dinner': sorted_dinner_list
        }
        #Turn outputs dictionary into a dataframe and display
        meal_itin_df = pd.DataFrame(meals_data)
        print(meal_itin_df)
        meal_itin_df.columns = ["Breakfast", "Lunch", "Dinner"]
    except:
        print("Invalid inputs, please try again! ")