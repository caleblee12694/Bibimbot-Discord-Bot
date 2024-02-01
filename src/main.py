import settings
import discord
from discord.ext import commands
from kanye import kanyequote

# Logging setup (non-functional as of now)
logger = settings.logging.getLogger("bot")


# Run function that sets up the bot and hosts all the commands.
#
# This function is continously listening for events as long as the
# bot is active, so don't try to run anything in main after it,
# because it won't work.
def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!b ", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def huh(ctx):
        url = 'https://tenor.com/bL6rT.gif'
        await ctx.send(url)

    @bot.command()
    async def kanye(ctx):
        quote = kanyequote()
        await ctx.send(quote)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

# Main function
if __name__ == "__main__":
    run()