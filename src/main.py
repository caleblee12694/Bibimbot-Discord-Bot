import settings
import discord
from discord.ext import commands
from kanye import kanyequote

logger = settings.logging.getLogger("bot")

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

if __name__ == "__main__":
    run()