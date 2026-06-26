#This file handles all the API Interactions with Maps and Gemini
import requests
import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
gemini_key = os.getenv('GEMINI_KEY')
genai.api_key = gemini_key
client = genai.Client(api_key=gemini_key)
maps_key =  os.getenv('MAPS_KEY')



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




def create_activities(lat,long,budget):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction= "You are a travel tour guide recommending people activities." \
        "Generate realistic activties near the provided coordinates. " \
        "Only include activties that do not excede the user's budget" \
        "Return only valid JSON, dont include any markdown, or explanations"),
        contents = f"""Find at most 5 activites to do near:
        Latitude: {lat}
        Longitude: {long}
        Budget limit: {budget}

        Return JSON in the following format:
        - for free activties make the cost 0. P

        [{{"name": "Activity name",
            "location": "Activity location"
            "cost": "cost of the activty"}}
        ]
        
        """
    )
    return json.loads(response.text)

