# import the code we want to test

from app.yelp import get_response
from app.yelp import sort_meal_list

import pytest
import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()

# expect default environment variable setting of "CI=true" on Travis CI
# see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
CI_ENV = os.getenv("CI") == "true"

#
# GET RESPONSE
#

# test valid input - can find all the necessary inputs
@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_get_response_valid():
    destination = "New York"
    days_input = 2
    price_limit = "1,2,3,4"
    food_preference = "chinese, american"
    test_breakfast_list, test_lunch_list, test_dinner_list = get_response(destination, days_input, price_limit, food_preference) # issues an HTTP request (see function definition below)
    
    # function should return three lists, each having some items
    assert isinstance(test_breakfast_list, list)
    assert isinstance(test_lunch_list, list)
    assert isinstance(test_dinner_list, list)
    
    # make sure results have the right keys
    assert list(test_breakfast_list[0].keys()) == ['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance']
    
    # look for nested keys, what data type each is (e.g. what you could get if accessing 'id')
    assert isinstance(test_breakfast_list[0]["categories"],list) # make sure the categories fall into list
    assert list(test_breakfast_list[0]["categories"][0].keys()) == ['alias', 'title'] # keys of that list should be alias and title
    
    # in ideal circumstance, the function should show the same number of results in each
    assert len(test_breakfast_list) == days_input
    assert len(test_lunch_list) == days_input
    assert len(test_dinner_list) == days_input


# test invalid input - cannot find enough matching restaurants
@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_get_response_invalid():
    destination = "Washington DC"
    days_input = 4
    price_limit = "1,2,3,4"
    food_preference = "chinese"
    test_breakfast_list, test_lunch_list, test_dinner_list = get_response(destination, days_input, price_limit, food_preference) # issues an HTTP request (see function definition below)
    
    # function should return three lists, each having some items
    assert isinstance(test_breakfast_list, list)
    assert isinstance(test_lunch_list, list)
    assert isinstance(test_dinner_list, list)
    
    # breakfast should not be able to find any results
    assert len(test_breakfast_list) == 0
    assert len(test_lunch_list) == days_input
    assert len(test_dinner_list) == days_input

    # make sure lunch results have the right keys
    assert list(test_lunch_list[0].keys()) == ['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count', 'categories', 'rating', 'coordinates', 'transactions', 'price', 'location', 'phone', 'display_phone', 'distance']
    