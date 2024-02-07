#!/usr/bin/env python3

import settings
import discord
from discord.ext import commands
from commands import kanyequote, huhgif, parse_emoji
import requests

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
        res = huhgif()
        await ctx.send(res)

    @bot.command()
    async def kanye(ctx):
        res = kanyequote()
        await ctx.send(res)

    @bot.command()
    async def smack(ctx, who):
        embed = discord.Embed(
            color=discord.Colour.dark_purple(),
            description=f'{str(ctx.message.author.display_name) + " smacked " + who + "!"}',
            title='SMACK'
        )
        embed.set_image(url="https://cdn3.emoji.gg/emojis/6132-pixel-toro-punch.gif")
        await ctx.send(embed=embed)

    @bot.command()
    async def flail(ctx, who):
        embed = discord.Embed(
            color=discord.Colour.dark_purple(),
            description=f'{str(ctx.message.author.display_name) + " is flailing " + who + "!"}',
            title='OH NO'
        )
        embed.set_image(url="https://media1.tenor.com/m/JbdTmeTpEZEAAAAC/hoseokmaraj-stan-twitter.gif")
        await ctx.send(embed=embed)

    @bot.command()
    async def destroy(ctx, who):
        embed = discord.Embed(
            color=discord.Colour.dark_purple(),
            description=f'{str(ctx.message.author.display_name) + " ended " + who + "!"}',
            title=f'{"🪦 Goodbye " + who + " 🪦"}'
        )
        embed.set_image(url="https://media1.tenor.com/m/78926NmBQEwAAAAC/blue-fighting.gif")
        await ctx.send(embed=embed)

    @bot.command()
    async def steal(ctx, args):
        if not args:
            await ctx.send("Put some emojis to yoink.")
            return
        
        made_emojis = []
        for raw_emoji in args:
            emoji, error = parse_emoji(raw_emoji)
            if error:
                await ctx.send(error)
                continue
            
            try:
                response = requests.get(emoji['url'])
                created_emoji = await ctx.guild.create_custom_emoji(name=emoji['name'], image=response.content)
                made_emojis.append(f"<{'a' if emoji['is_animated'] else ''}:{created_emoji.name}:{created_emoji.id}>")
                await ctx.send(f"Yoinked: `{emoji['url']}`!")
            except Exception as e:
                if 'Maximum number of emojis reached (50)' in str(e):
                    await ctx.send('Maximum number of emojis reached! (50)')
                    break
                else:
                    await ctx.send('An error occurred whilst adding the emojis!')
                    print(e)
        
        if made_emojis:
            await ctx.send('Addded emojis: ' + ' '.join(made_emojis))

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)



# Main function
if __name__ == "__main__":
    run()