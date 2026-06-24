import requests
import os


maps_key = os.getenv('MAPS_KEY')
gemini_key = os.getenv('GEMINI_KEY')

#converts users location into lat and long coordinates(for geminiapi)
def get_coordinates(location):
    #get the google maps api endpoint later
    url = ("https://maps.googleapis.com/maps/api/geocode/json"f"?address={location}"f"&key={maps_key}")
    response = requests.get(url)
    data = response.json()

    #error check if location does not exist
    if data['status']!= "OK":
        return None
    
    #get lat and long coordinates
    coordinates = data['results'][0]["geometry"]["location"]
    lattitude, longitude = coordinates['lat'],coordinates['lng']
    return (lattitude,longitude)





    