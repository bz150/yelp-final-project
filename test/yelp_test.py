# import the code we want to test

from app.yelp_app import function
from app.yelp_app import get_response

import pytest
import os
import requests
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

def test_function():
    assert function(10) == 20

# expect default environment variable setting of "CI=true" on Travis CI
# see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_get_response():
    destination = "1804 N Quinn St Rosslyn VA 22209"
    days_input = 1
    price_limit = "1,2"
    food_preference = "American"
    test_breakfast_list, test_lunch_list, test_dinner_list = get_response(destination, days_input, price_limit, food_preference) # issues an HTTP request (see function definition below)

    #assert isinstance(test_parsed_response, dict)
    assert test_breakfast_list[0]["id"] == "NzFNtnlxyifE3MPTB0kupA"


# expect default environment variable setting of "CI=true" on Travis CI
# see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_get_response():
    destination = "1804 N Quinn St Rosslyn VA 22209"
    days_input = 1
    price_limit = "1,2"
    food_preference = "American"
    test_breakfast_list, test_lunch_list, test_dinner_list = get_response(destination, days_input, price_limit, food_preference) # issues an HTTP request (see function definition below)
    
    # function should return three lists, each having some items
    assert isinstance(test_breakfast_list, list)
    assert isinstance(test_lunch_list, list)
    assert isinstance(test_dinner_list, list)

    # make sure results have the right keys
    assert list(test_breakfast_list[0].keys()) == ['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance']
    
    # look for nested keys, what data type each is (e.g. what you could get if accessing 'id')


# consider making this a fixture
#mock_products_filepath = os.path.join(os.path.dirname(__file__),"mock_data","mock_products.csv")
#mock_products_df = read_csv(mock_products_filepath)
#mock_products = mock_products_df.to_dict("records")

#
# TEST THE GET_RESPONSE FUNCTION
# calls the Yelp API

#def test_get_response():
#    # with valid product id, returns the product info:
#    valid_result = lookup_product("8",mock_products)
#    assert valid_result == {
#        'aisle':'Aisle C',
#        'department':'snacks',
#        'id':8,
#        'name':'Product 8',
#        'price':10.0
#    }
#    # with invalid product id, returns None:
#    invalid_result = lookup_product("88888888",mock_products)
#    assert invalid_result == None




#
# FROM ROBO_TEST.PY
#

#import os
#import pytest
#
#from app.robo import get_response
#
## expect default environment variable setting of "CI=true" on Travis CI
## see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
#CI_ENV = os.getenv("CI") == "true"
#
#@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
#def test_get_response():
#    symbol = "NFLX"
#    parsed_response = get_response(symbol) # issues an HTTP request (see function definition below)
#
#    assert isinstance(parsed_response, dict)
#    assert parsed_response["Meta Data"]["2. Symbol"] == symbol



#
# FROM GAME_TEST.PY
#

#from app.game import determine_winner

# TODO: test the code

#def test_determination_of_the_winner():
#    assert determine_winner("rock", "rock") == None
#    assert determine_winner("rock", "paper") == "paper"
#    assert determine_winner("rock", "scissors") == "rock"
#    assert determine_winner("paper", "rock") == "paper"
#    assert determine_winner("paper", "paper") == None
#    assert determine_winner("paper", "scissors") == "scissors"
#    assert determine_winner("scissors", "rock") == "rock"
#    assert determine_winner("scissors", "paper") == "scissors"
#    assert determine_winner("scissors", "scissors") == None
#

# running all of these shows that the game is actually working
