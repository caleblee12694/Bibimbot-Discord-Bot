from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'SAY SOMETHING.'
    elif 'hello' in lowered:
        return 'haiii >.<'
    else:
        return choice(['wat...?',
                       'I dunno wym',
                       'ok...'])