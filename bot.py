import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import requests

load_dotenv()
from typing import Optional


TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = ">"
MY_GUILD = discord.Object(id=756127990915661846)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


async def hello_command(message):
    await message.channel.send(f"Hi {message.author}")


async def bye_command(message):
    await message.channel.send(f"Goodbye {message.author}")


# Command dictionary mapping commands to functions
command_dict = {
    "hello": hello_command,
    "bye": bye_command,
    # Add more commands as needed
}


@bot.event
async def on_ready():
    print(f"{bot.user} logged in successfully!")


@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user:
        return

    if message.content.startswith(PREFIX):
        # Remove the prefix and split the message into command and arguments
        command, *args = message.content[len(PREFIX) :].split()
        print(f"Command: {command}")
        # Check if the command is in the command dictionary
        if command in command_dict:
            # Call the corresponding function
            await command_dict[command](message)


# Start each command with the @bot.command decorater
@bot.command()
async def square(ctx, arg):  # The name of the function is the name of the command
    print(arg)  # this is the text that follows the command
    await ctx.send(int(arg) ** 2)  # ctx.send sends text in chat


@bot.command()
async def scrabblepoints(ctx, arg):
    # Key for point values of each letter
    score = {
        "a": 1,
        "c": 3,
        "b": 3,
        "e": 1,
        "d": 2,
        "g": 2,
        "f": 4,
        "i": 1,
        "h": 4,
        "k": 5,
        "j": 8,
        "m": 3,
        "l": 1,
        "o": 1,
        "n": 1,
        "q": 10,
        "p": 3,
        "s": 1,
        "r": 1,
        "u": 1,
        "t": 1,
        "w": 4,
        "v": 4,
        "y": 4,
        "x": 8,
        "z": 10,
    }
    points = 0
    # Sum the points for each letter
    for c in arg:
        points += score[c]
    await ctx.send(points)


bot.run(TOKEN)
