# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.yelp import get_response

yelp_route = Blueprint("yelp_route", __name__)

@yelp_route.route("/yelp/results.json")
def yelp_results_api():
    print("YELP RESULTS...")
    print("URL PARAMS:", dict(request.args))


    destination = request.args.get("destination") or "New York"
    days_input = request.args.get("days_input") or "3"
    days_input=int(days_input)
    price = request.args.get("price_limit") or ["1", "2", "3"]
    price_limit = []
    for num in range(0,len(price)):
        price_limit.append(str(num + 1))
    #Change this to categories
    #food = []
    food_preference = request.args.get("food_preference") or "American"
    #food_preference = ""
    #for item in food:
    #    if item != food[0]:
    #        food_preference= str(food_preference + "," + item)
    #    elif item == food[0]:
    #        food_preference = str(item)
    breakfast_results, lunch_results, dinner_results = get_response(destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference)
    if breakfast_results and lunch_results and dinner_results:
        return jsonify(breakfast_results, lunch_results, dinner_results)
    else:
        return jsonify({"message":"Invalid Inputs. Please try again."}), 404

@yelp_route.route("/yelp/form")
def yelp_form():
    print("YELP FORM...")
    return render_template("yelp_form.html")

@yelp_route.route("/yelp/results", methods=["GET", "POST"])
def yelp_results():
    print("YELP RESULTS...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    destination = request_data.get("destination") or "New York"
    days_input = request_data.get("days_input") or "3"
    days_input = int(days_input)
    price = request_data.get("price_limit") or ["1", "2", "3"]
    price_limit = []
    for num in range(0,len(price)):
        price_limit.append(str(num + 1))
    #Change this to categories
    #food = []
    food_preference = request_data.get("food_preference") or "American"
    #food_preference = ""
    #for item in food:
    #    if item != food[0]:
    #        food_preference= str(food_preference + "," + item)
    #    elif item == food[0]:
    #        food_preference = str(item)

    breakfast_results, lunch_results, dinner_results = get_response(destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference)
    if breakfast_results and lunch_results and dinner_results:
        flash(f"Yelp Results Generated Successfully!", "success")
        return get_response("yelp_results.html", destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference, breakfast_results=breakfast_results, lunch_results=lunch_results, dinner_results=dinner_results)
    else:
        flash(f"Input Error. Please try again!", "danger")
        return redirect("/yelp/form")