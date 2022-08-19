# Written by Daniel C
# This is a basic Discord bot built on hikari and lightbulb,
# and includes features useful to IB communities.

import lightbulb
import hikari
from math import *
import os

discord_token = 'YOUR TOKEN HERE'
guilds = ("SERVER ID HERE")

bot = lightbulb.BotApp(token=discord_token, default_enabled_guilds=guilds)

@bot.command
@lightbulb.command(name="sanitycheck", description="Sends sample text to check if the bot is working correctly.")
@lightbulb.implements(lightbulb.SlashCommand)
async def sanity(ctx: lightbulb.SlashCommand):

    await ctx.respond(hikari.File("ascii-art.txt"))
    await ctx.respond("If you see an IB logo, then the bot is working correctly!")

@bot.command
@lightbulb.option("math", "Math to calculate.", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command("calculate", "Calculates a basic equation using the Python math syntax.")
@lightbulb.implements(lightbulb.SlashCommand)
async def calculate(ctx: lightbulb.SlashContext):

    try:
        answer = eval(ctx.raw_options["math"])
        await ctx.respond(answer)
    except Exception:
        await ctx.respond("Something went wrong when calculating. Check your syntax!")

@bot.command
@lightbulb.command("codereview", "Shows the bot's source code. This is for you, Liam.")
@lightbulb.implements(lightbulb.SlashCommand)
async def code(ctx):
    os.chdir("..")
    await ctx.respond(hikari.File("main.py"))
    os.chdir("files")

@bot.command
@lightbulb.command("credits", "Shows the credits for the bot. These things don't code themselves!")
@lightbulb.implements(lightbulb.SlashCommand)
async def credits(ctx: lightbulb.context.slash.SlashContext):
    credits = """
* Credits for IB Bot *
Code written by Daniel C, IB Session May 2023.
Written entirely in Python using the hikari
and lightbulb frameworks.
Both projects can be found linked on this project's
GitHub page (accessible using the /github command).
All reference documents courtesy of the IBO.
"""
    await ctx.respond(credits)

@bot.command
@lightbulb.command('github', "Returns the GitHub page for this project.")
@lightbulb.implements(lightbulb.SlashCommand)
async def github(ctx: lightbulb.SlashContext):
    await ctx.respond("https://github.com/daniel-c5656/ib-bot")

@bot.command
@lightbulb.command('const', 'Contains all numerical constants found in IB data booklets.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def constants():
    pass

@constants.child
@lightbulb.command("physics", "Returns the page of constants from the physics data booklet.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def phys_consts(ctx: lightbulb.context.slash.SlashContext):
    await ctx.respond(hikari.File("phys_consts.png"))

@constants.child
@lightbulb.command("chemistry", "Returns the page of constants from the chemistry data booklet.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def chem_consts(ctx: lightbulb.context.slash.SlashContext):
    await ctx.respond(hikari.File("chem_consts.png"))

@bot.command
@lightbulb.command('db', 'All the data booklets you might need!')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def data_booklets():
    pass

@data_booklets.child
@lightbulb.command("physics", "Returns a pdf of the physics data booklet.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def phys_db(ctx: lightbulb.SlashContext):
    await ctx.respond(hikari.File('phys_db.pdf'))

@data_booklets.child
@lightbulb.command("chem", "Returns a pdf of the chemistry data booklet.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def chem_db(ctx: lightbulb.SlashContext):
    await ctx.respond(hikari.File('chem_db.pdf'))

if __name__ == "__main__":
    os.chdir('files')
    bot.run()