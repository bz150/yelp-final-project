# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.yelp_app import get_response

yelp_route = Blueprint("yelp_route", __name__)

#@yelp_route.route("/yelp/results.json")
#def yelp_results_api():
#    print("YELP RESULTS...")
#    print("URL PARAMS:", dict(request.args))
#
#
#    destination = request.args.get("destination") or "New York"
#    days_input = request.args.get("days_input") or "3"
#    price_limit = request.args.get("price_limit") or "$$$"
#    #Change this to categories
#    food_preference = request.args.get("food_preference") or "Chinese, American"
#
#    breakfast_results, lunch_results, dinner_results = get_response(destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference)
#    if breakfast_results and lunch_results and dinner_results:
#        return jsonify(results)
#    else:
#        return jsonify({"message":"Invalid Inputs. Please try again."}), 404

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
    price_limit = request_data.get("price_limit") or "$$$"
    #Change this to categories
    food_preference = request_data.get("food_preference") or "Chinese, American"

    breakfast_results, lunch_results, dinner_results = get_response(destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference)
    if breakfast_results and lunch_results and dinner_results:
        flash(f"Yelp Results Generated Successfully!", "success")
        return get_response("yelp_results.html", destination=destination, days_input=days_input, price_limit=price_limit, food_preference=food_preference, breakfast_results=breakfast_results, lunch_results=lunch_results, dinner_results=dinner_results)
    else:
        flash(f"Input Error. Please try again!", "danger")
        return redirect("/yelp/form")