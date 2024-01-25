import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
import json
import requests

load_dotenv()
from typing import Optional


TOKEN = os.getenv("DISCORD_TOKEN")

MY_GUILD = discord.Object(id=756127990915661846)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(">hello"):
        await message.channel.send("Hello!")


bot.run(TOKEN)
