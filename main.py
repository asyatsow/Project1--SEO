import requests
import os


API_KEY = os.getenv()
#converts users location into lat and long coordinates(for geminiapi)
def get_coordinates(location):
    url = "https://maps.googleapis.com/maps/api/geocode/"


    