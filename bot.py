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


bot.run(TOKEN)
