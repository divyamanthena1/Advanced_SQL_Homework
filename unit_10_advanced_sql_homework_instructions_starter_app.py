# Import everything you used in the starter_climate_analysis.ipynb file, along with Flask modules
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

#################################################
# Database Setup
#################################################
# Create an engine
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model with automap_base() and Base.prepare()
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station
# Instantiate a Session and bind it to the engine
session = Session(engine)
#################################################
# Flask Setup
#################################################
# Instantiate a Flask object at __name__, and save it to a variable called app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Set the app.route() decorator for the base '/'
@app.route("/")
# define a welcome() function that returns a multiline string message to anyone who visits the route
def welcome():
    """List all available api routes."""
# Set the app.route() decorator for the "/api/v1.0/precipitation" route
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/precipitation"
    )
# define a precipitation() function that returns jsonified precipitation data from the database
def precipitation():
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Calculate the date 1 year ago from last date in database
    latest_date = (session
     .query(measurement.date)
     .order_by(measurement.date.desc())
     .first())
    latest_date
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    latest_dates = (session
     .query(measurement.date)
     .filter(measurement.date >= query_date)
     .order_by(measurement.date.desc())
     .all())
    latest_dates
    # Query for the date and precipitation for the last year
    prcp_1 = (session
     .query(measurement.date, measurement.prcp)
     .filter(measurement.date >= '2016-08-23')
     .all())
    prcp_1
    # Create a dictionary to store the date: prcp pairs. 
    # Hint: check out a dictionary comprehension, which is similar to a list comprehension but allows you to create dictionaries
    prcp_2 = pd.DataFrame(prcp_1)
    prcp_2.set_index('date')
    prcp_2
    results = {d['prcm']: d['date'] for d in prcp_2.to_dict(orient='records')}
    # Return the jsonify() representation of the dictionary
    response = jsonify(results=results)
# Set the app.route() decorator for the "/api/v1.0/stations" route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/stations"
    )
# define a stations() function that returns jsonified station data from the database
def stations()
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Query for the list of stations
    stations = (session
     .query(measurement.station)
     .all())
    pd.DataFrame(stations).value_counts()
    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
    # Return the jsonify() representation of the list


# Set the app.route() decorator for the "/api/v1.0/tobs" route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/tobs"
    )
# define a temp_monthly() function that returns jsonified temperature observations (tobs) data from the database
def temp_monthly()
# In the function (logic should be the same from the starter_climate_analysis.ipynb notebook):
    # Calculate the date 1 year ago from last date in database
    stations2 = (session
     .query(measurement.tobs)
     .filter(measurement.station == 'USC00519281'))
    latest_date2 = (session
     .query(measurement.date)
     .filter((measurement.station == 'USC00519281'))
     .order_by(measurement.date.desc())
         .first())
latest_date2
    query_date2 = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    print(query_date2)
    latest_dates2 = (session
     .query(measurement.date)
     .filter(measurement.date <= query_date2)
     .order_by(measurement.date.desc())
     .all())
    latest_dates2
    highest_temps = (session
     .query(measurement.date, measurement.tobs)
     .filter(measurement.station == 'USC00519281', measurement.date >= '2016-08-18')
     .all())
    highest_temps
    highest_temps_2 = pd.DataFrame(highest_temps)
    highest_temps_2.set_index('date')
    frequency = highest_temps_2['tobs'].value_counts()
    frequency
    # Query the primary station for all tobs from the last year
    
    # Unravel results into a 1D array and convert to a list
    # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
    # Return the jsonify() representation of the list


# Set the app.route() decorator for the "/api/v1.0/temp/<start>" route and "/api/v1.0/temp/<start>/<end>" route
# define a stats() function that takes a start and end argument, and returns jsonified TMIN, TAVG, TMAX data from the database
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # If the end argument is None:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        
        # Unravel results into a 1D array and convert to a list
        # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
        # Return the jsonify() representation of the list

    # Else:
        # calculate TMIN, TAVG, TMAX with both start and stop
        
        # Unravel results into a 1D array and convert to a list
        # Hint: checkout the np.ravel() function to make it easier to convert to a list
    
        # Return the jsonify() representation of the list


if __name__ == '__main__':
    app.run()
