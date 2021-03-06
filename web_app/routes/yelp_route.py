# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.yelp import get_response

yelp_route = Blueprint("yelp_route", __name__)


#Route to the Yelp input form
@yelp_route.route("/yelp/form")
def yelp_form():
    print("YELP FORM...")
    return render_template("yelp_form.html")

#Route to the Yelp output form
@yelp_route.route("/yelp/results", methods=["GET", "POST"])
def yelp_results():
    print("YELP RESULTS...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    #Request the input information from the Yelp form
    destination = request_data.get("destination") or "New York"
    days_input = request_data.get("days_input") or "3"
    days_input = int(days_input)
    price = request_data.get("price_limit") or ["1", "2", "3"]
    #List to hold price limit
    price_limit = []
    #Add prices to the price limit list
    for num in range(0,len(price)):
        price_limit.append(str(num + 1))

    #Request food preference information from separate checkboxes
    food_preference_1 = request_data.get("food_preference1") 
    food_preference_2 = request_data.get("food_preference2") 
    food_preference_3 = request_data.get("food_preference3") 
    food_preference_4 = request_data.get("food_preference4") 
    food_preference_5 = request_data.get("food_preference5") 
    food_preference_6 = request_data.get("food_preference6") 

    #Create list to hold food preferences
    food_list = []


    #Only add to food preference list if the checkbox is checked
    if food_preference_1 != None:
        food_list.append(food_preference_1)
    if food_preference_2 != None:
        food_list.append(food_preference_2)
    if food_preference_3 != None:
        food_list.append(food_preference_3)
    if food_preference_4 != None:
        food_list.append(food_preference_4)
    if food_preference_5 != None:
        food_list.append(food_preference_5)
    if food_preference_6 != None:
        food_list.append(food_preference_6)
    
    #Create a string to hold final food preference parameter
    food_preference = ""
    
    #Add food preferences into the string through concatenation
    for item in food_list:
        if item != food_list[0]:
            food_preference = str(food_preference + "," + item)
        elif item == food_list[0]:
            food_preference = str(item)
    
    #If none of the checkboxes are checked, use American food as a default category
    if len(food_list) == 0:
        food_preference = "american"

    #Ensure that food preferences start in lowercase to be successfully used in the API
    food_preference = food_preference.lower()

    try:
        #Get response from the original function using web app inputs
        breakfast_results, lunch_results, dinner_results = get_response(destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference)
        
        #If results are able to be found, then display outputs onto yelp results page
        if breakfast_results and lunch_results and dinner_results:
            flash(f"Yelp Results Generated Successfully!", "success")
            return render_template("yelp_results.html", destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference, breakfast_results=breakfast_results, lunch_results=lunch_results, dinner_results=dinner_results)
        #Tell user if results are unable to be found
        #elif breakfast_results.status_code == 500 or lunch_results.status_code == 500 or dinner_results.status_code == 500:
        #    flash(f"Input Error - No Results Found. Please try again with different inputs!", "danger")
        #    return redirect("/yelp/form")
        else:
            flash(f"Input Error - No Results Found. Please try again with different inputs!", "danger")
            return redirect("/yelp/form")
    #Return back to the yelp form if inputs are invalid and request can't be made
    except:
        flash(f"Input Error - No Results Found. Please try again with different inputs!", "danger")
        return redirect("/yelp/form")

    