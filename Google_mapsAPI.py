import os
from google import genai 

#Dummy_file to tets out if our apis work as intended
# 1. Grab your Maps API key from the terminal environment
maps_key = os.getenv('MAPS_KEY')
gemini_key = os.getenv('GEMINI_KEY')


# 2. Initialize the Google Maps client
gmaps = googlemaps.Client(key=maps_key)
genai = genai.Client(api_key = gemini_key)
# 3. Test it by searching for local businesses (e.g., bakeries in New York)

places_result = gmaps.places(query='bakery in New York')

# 4. Print out the first result to make sure it works
if places_result['results']:
    first_business = places_result['results'][0]
    print(f"Business Name: {first_business['name']}")
    print(f"Address: {first_business['formatted_address']}")
    print(f"Rating: {first_business.get('rating', 'No rating')}")
else:
    print("No businesses found or API key issue.")