import requests
import os
from dotenv import load_dotenv

load_dotenv()
maps_key =  os.getenv('MAPS_KEY')
#gemini_key = os.getenv('GEMINI_KEY')


#converts users location into lat and long coordinates(for geminiapi)
def get_coordinates(location):
    #get the google maps api endpoint later
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    response = requests.get(url,params = {"address": location, "key": maps_key})
    data = response.json()


    #error check if location does not exist
    if data['status']!= "OK":
        return None
    
    #get lat, long coordinates and formatted string address
    coordinates = data['results'][0]["geometry"]["location"]
    formatted_address = data["results"][0]["formatted_address"]
    lattitude, longitude = coordinates['lat'],coordinates['lng']
    return (formatted_address,lattitude,longitude)

#location = input("Where are you heading? ")
address,lat,long = get_coordinates("Brooklyn, NY")
print(address,lat,long)


    





    