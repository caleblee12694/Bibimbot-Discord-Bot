from random import choice, randint
from kanye import kanye

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'SAY SOMETHING.'
    elif 'hello' in lowered:
        return 'haiii >.<'
    elif 'cringe' in lowered:
        return 'CRINGE CRINGE CRINGE\nCRINGE CRINGE CRINGE\nCRINGE CRINGE CRINGE'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif lowered == 'kanye':
        return kanye()
    else:
        return "I couldn't understand."