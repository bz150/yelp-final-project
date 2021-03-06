# yelp-final-project

Bon Appeteat is a Python application intended to help travelers going on a vacation who need an itinerary of restauraunts to go to for each meal during a future trip, so that they have an easy way to plan a trip without having to search individually for each meal.

This app was created as part of the OPIM 244 class at Georgetown. Requirements are linked [here](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/freestyle/implementation.md#evaluation).

## Prerequisites
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](http://github.com/bz150/yelp-final-project) under your own control, then "clone" or download your remote copy onto your local computer.

Navigate to the repository from the command-line:

```sh
cd yelp-final-project
```

Use Anaconda to create and activate a new virtual environment called "yelp-env":

```sh
conda create -n yelp-env python=3.8
conda activate yelp-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup
Obtain an API Key from [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3/authentication) in order to issue a request. Follow the instructions on Yelp Fusion API to create an app to obtain the API Key. 

 In the root directory of your local repository, create a new file called ".env", and store the API Key value in the ".env" file (replace "abc123" with the correct API Key):
 ```
  YELP_API_KEY = "abc123"
 ```

## Usage 
Run the program in the terminal:
`python app/yelp.py` or `python -m app.yelp`

## Web App
Run the web app for a better user interface. Use the following commands:

Mac OS: 
```
FLASK_APP=web_app flask run
```
Windows OS: 
```
export FLASK_APP=web_app 
flask run
```

## Testing
Run tests to ensure functions are working properly. Running all tests can be done using the following:
```
pytest

# in CI mode:
CI=true pytest
```

## Deploying
Deploy to Heroku to host your own web app. Original instructions via Prof. Rossetti [here](https://github.com/bz150/daily-briefings-py/blob/main/DEPLOYING.md).

### Prerequisites and Setup
Start by [signing up](https://signup.heroku.com/) for a Heroku account and [installing](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/clis/heroku.md#installation) the Heroku CLI.

Set up a server:
```
heroku create yelp-app # choose your own, unique name
```
Verify that the app was created and that the local repo is linked to the Heroku address.
```
heroku apps
git remote -v
```
Server configuration:
```
heroku config:set YELP_API_KEY = "____" # set env variable
heroku config # make sure production environment was properly configured
```
Deploy to Heroku:
```
git push heroku main
```

### Running the Deployed App on Heroku
Your web app should now run live on the server. You can use the following commands:
```
heroku run bash # login to server
exit # logout
```

(Adapted from Professor Rossetti's markdown)
