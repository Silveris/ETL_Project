import requests
import pandas as pd
from config import api_key
import json
from pprint import pprint
import requests
import datetime as datetime
import time

################### FUNC #######################
def(cities_weatherapi):#
################################################

url = f"http://api.openweathermap.org/data/2.5/group?id=4887398,4644585,4463523,5809844,5856195,4164138,5074472,4699066,5308655,5454711&units=imperial&appid={api_key}&q="
response = requests.get(url)
cities = response.json()

# set up lists to hold reponse info
city_name = []
date = []
high = []
low = []
current = []
feels_like = []
humidity = []
pressure = []

dashes = "---------------------------------"

# Loop through the list of cities and perform a request for data on each

#     response = requests.get(url + city).json()
counter = 0
for counter in range(10):
    #     response = requests.get(url + city).json()
    city_name.append(cities['list'][counter]['name'])
    date.append(cities['list'][counter]['dt'])
    high.append(cities['list'][counter]['main']['temp_max'])
    low.append(cities['list'][counter]['main']['temp_min'])
    current.append(cities['list'][counter]['main']['temp'])
    feels_like.append(cities['list'][counter]['main']['feels_like'])
    humidity.append(cities['list'][counter]['main']['humidity'])
    pressure.append(cities['list'][counter]['main']['pressure'])
    counter += 1

# create a data frame from cities, lat, and temp
cities_dict = {
    "City": city_name,
    "Date": datetime.datetime.today(),
    "Daily High (F)": high,
    "Daily Low (F)": low,
    "Current Temp (F)": current,
    "Feels Like": feels_like,
    "Humidity (%)": humidity,
    "Pressure (mb)": pressure,
}
cities_df = pd.DataFrame(cities_dict)
cities_df.to_csv("api.csv")

################# RUN FUNC ##########################
run(cities_weatherapi)
#####################################################
