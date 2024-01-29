from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Loading Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Startup Handling
@client.event
async def on_read() -> None:
    print(f'{client.user} is not running!')

# Incoming Messages Handling
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()