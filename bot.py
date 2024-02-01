import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from commands.list_cmds import command_dict

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = ">"
MY_GUILD = discord.Object(id=756127990915661846)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


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
            try:
                await command_dict[command](message)
            except commands.MissingRequiredArgument as e:
                await message.channel.send(f"Missing argument: {e}")
            except commands.CommandInvokeError as e:
                await message.channel.send(f"Command error: {e}")
                print(
                    f"An error occurred while executing command '{command}': {e.original}"
                )
        else:
            await message.channel.send(
                "Unknown command. Use !help to see available commands."
            )


bot.run(TOKEN)
