import requests
import json

# API endpoint
url = "https://api.kanye.rest/"

def kanye():
    # GET request to endpoint
    response = requests.get(url)

    # print the response
    response_json = response.json()
    quote = str(response_json['quote'])

    return quote