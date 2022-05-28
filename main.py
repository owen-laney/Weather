# Weather Logic
# * Gets data from owm
# * Handles data storage
# * Everything is a function that can be called by ui.py

from xml.etree.ElementInclude import include
from pkg_resources import require
from pyowm.utils import timestamps
from pyowm.owm import OWM
import json

data = json.load(open('data.json'))

def writeData(city, country, key):
    data = {'city': 'Paris', 'country': 'FR', 'key': '7996d03492a1b1217f3c1337e518f08c'}
    with open('data.json', 'w') as f:
        json.dump(data, f)


owm = OWM(data['key'])

def getWeather():
    mgr = owm.weather_manager()

    data = json.load(open('data.json'))
    location = str(data['city'] + ',' + data['country'])
    currentWeather = str(mgr.weather_at_place(location).weather)
    
    # Hardcoded statuses, deinitely not the best way to do this
    if 'clouds' in currentWeather: currentWeather = 'Cloudy'
    elif 'clear' in currentWeather: currentWeather = 'Clear'
    elif 'rain' in currentWeather: currentWeather = 'Raining'
    else: currentWeather = 'Unknown'

    return currentWeather

def futureWeather():
    mgr = owm.weather_manager()
    
    data = json.load(open('data.json'))
    location = str(data['city'] + ',' + data['country'])
    
    futureWeather = mgr.forecast_at_place(location, '3h')
    futureWeather = str(futureWeather.get_weather_at(timestamps.tomorrow()))

    if 'clouds' in futureWeather: futureWeather = 'Cloudy'
    elif 'clear' in futureWeather: futureWeather = 'Clear'
    elif 'rain' in futureWeather: futureWeather = 'Raining'
    else: futureWeather = 'Unknown'

    return futureWeather
