"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint
from geopy.geocoders import Nominatim
geolocator = Nominatim()
#import stopsbylocation


#from googlemaps import GoogleMaps


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    pprint(response_data)
#get_json(GMAPS_BASE_URL)

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    location = geolocator.geocode(place_name)
    address=(location.address)
    lat = (location.latitude)
    lng = (location.longitude)

    #gmaps = GoogleMaps(api_key)
    #address = 'Constitution Ave NW & 10th St NW, Washington, DC'
    
    #lat, lng = gmaps.address_to_latlng(address)
    return lat, lng

print get_lat_long('Olin College')

def get_lat(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    location = geolocator.geocode(place_name)
    address=(location.address)
    lat = (location.latitude)
  

    #gmaps = GoogleMaps(api_key)
    #address = 'Constitution Ave NW & 10th St NW, Washington, DC'
    
    #lat, lng = gmaps.address_to_latlng(address)
    return lat



def get_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    geolocator = Nominatim()
    location = geolocator.geocode(place_name)
    address=(location.address)
    lng = (location.longitude)

    #gmaps = GoogleMaps(api_key)
    #address = 'Constitution Ave NW & 10th St NW, Washington, DC'
    
    #lat, lng = gmaps.address_to_latlng(address)
    return lng
    #json_response_data = get_json(url)

    #latitude = get_json(url)["results"][0]["formatted_address"]
    #Fenway Park, 4 Yawkey Way, Boston, MA 02215, US

#get_lat_long("Fenway Park")

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    userLoc = latitude, longitude
    bounds = geopy.geocoders.bounds.from_point_and_radius(userLoc, 10)
    stations = Station.in_bounds(bounds).all # get all stations within 10 miles
    locations = geolocator.geocode(station.each)
    #args = {'lon' = userLoc[1], 'lat' = userLoc[0], 'key' = }


    return locations



    #station = stop.name(latitude, longitude)
    #local = gmaps.local_search('mbta station near ' + destination)
    #print local['responseData']['results'][0]['titleNoFormatting']
print get_nearest_station(42.346489975,-71.0972243185)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    latitude = get_lat(place_name)
    longitude = get_long(place_name)
    get_nearest_station(latitude, longitude)

    pass

find_stop_near('Fenway Park')