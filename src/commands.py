import requests
import json

# Kanye API endpoint
kanye_url = "https://api.kanye.rest/"

def kanyequote():
    # GET request to endpoint
    response = requests.get(kanye_url)

    # print the response
    response_json = response.json()
    quote = str(response_json['quote'])

    return quote

# League of Legends ping GIF
def huhgif():
    url = 'https://tenor.com/bL6rT.gif'
    
    return url