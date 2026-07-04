import requests # The library we just installed
import json     # The AI data format you learned yesterday

print("Agent is connecting to the internet...")

# 1. We are using a free public API that returns a random joke in JSON format
url = "https://official-joke-api.appspot.com/random_joke"

# 2. We send a "GET" request (asking for data)
response = requests.get(url)

# 3. Check if the connection was successful (Status code 200 means OK!)
if response.status_code == 200:
    print("Connection Successful! Data received.\n")
    
    # 4. Convert the incoming JSON into a Python Dictionary
    data = response.json()
    
    # 5. Print the specific parts of the dictionary
    print("Setup:", data["setup"])
    print("Punchline:", data["punchline"])
else:
    print(f"Failed to connect. Error code: {response.status_code}")