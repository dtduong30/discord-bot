# Each command can be defined in a separate file
async def hello_command(message):
    await message.channel.send(f"Hi {message.author}")


async def bye_command(message):
    await message.channel.send(f"Goodbye {message.author}")


async def muoi_buon_command(message):
    await message.channel.send(f"Muối buồn {message.author}")
