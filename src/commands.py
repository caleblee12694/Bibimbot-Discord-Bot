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

# Parses an emoji string
def parse_emoji(emoji):
    if not emoji.startswith('<'):
        return 'The emoji you specified is not a real emoji.', None
    is_animated = emoji.startswith('<a:')
    parts = emoji.split(':')
    name = parts[1]
    id_ = parts[2].replace('>', '')
    url = f"https://cdn.discordapp.com/emojis/{id_}{'.gif' if is_animated else '.png'}"
    return {'name': name, 'id': id_, 'is_animated': is_animated, 'url': url}, None