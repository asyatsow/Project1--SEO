import os
import googlemaps

# 1. Grab your Maps API key from the terminal environment
my_api_key = os.getenv('GENAI_KEY')

# 2. Initialize the Google Maps client
gmaps = googlemaps.Client(key=my_api_key)
 
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