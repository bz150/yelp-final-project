# yelp-final-project

A Python application intended to help travelers going on a vacation who need an itinerary of restauraunts to go to for each meal during a future trip, so that they have an easy way to plan a trip without having to search individually for each meal.

# Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](http://github.com/bz150/yelp-final-project) under your own control, then "clone" or download your remote copy onto your local computer.

After cloning the repo, navigate there from the command-line:

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

## Usage 

Run the program: 
```sh
python app/yelp_app.py


Run the web app:
FLASK_APP=web_app flask run
```

