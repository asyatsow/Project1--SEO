import os
from google import genai
from google.genai import types

my_api_key = os.getenv('GENAI_KEY')

client = genai.Client(api_key=my_api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=" Provide concise, clear info on reccomended places based on my interest."
    ), # 👈 Added a comma here to separate config from contents
    contents="What are the best food prices based on my budget?", # 👈 Removed the accidental 'ls.' and closed the parenthesis ) here
)

print(response.text)