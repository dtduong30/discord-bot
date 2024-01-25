# async def send_message_to_channel(bot, guild_id, channel_id, message):
#     # Get the target guild using its ID
#     target_guild = bot.get_guild(guild_id)
#     print(target_guild)

#     # Check if the target guild exists
#     if target_guild:
#         # Get the target channel using its ID
#         target_channel = target_guild.get_channel(channel_id)

#         # Check if the target channel exists
#         if target_channel:
#             # Send a message to the target channel
#             await target_channel.send(message)
#         else:
#             print(f"Target channel not found in guild {guild_id}.")
#     else:
#         print(f"Target guild not found: {guild_id}.")


# # EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
# @bot.event
# async def on_ready():
#     # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
#     guild_count = 0

#     # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
#     for guild in bot.guilds:
#         # PRINT THE SERVER'S ID AND NAME.
#         print(f"- {guild.id} (name: {guild.name})")

#         # INCREMENTS THE GUILD COUNTER.
#         guild_count = guild_count + 1

#     # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
#     print("Bot is in " + str(guild_count))


# # EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
# # Define another command
# @bot.command(name="ping", help="Responds with Pong!")
# async def ping(ctx):
#     await ctx.send("Pong!")


# @bot.command(name="hello", help="Responds with Hello!")
# async def hello():
#     await send_message_to_channel(
#         bot, "756127990915661846", "852545901141426217", "Hello from the bot!"
#     )


# def run_bot():
#     client = discord.Client()

#     @client.event
#     async def on_ready():
#         # await send_message_to_channel(
#         #     bot, "756127990915661846", "852545901141426217", "Hello from the bot!"
#         # )
#         print("Bot is running")

#     @client.event
#     async def on_message(message):
#         # await send_message_to_channel(
#         #     bot, "756127990915661846", "852545901141426217", "Hello from the bot!"
#         # )
#         print("Bot is running")
