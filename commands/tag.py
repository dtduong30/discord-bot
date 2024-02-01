import discord

agnes = "341107845523046400"
wakuu = "449456684767641600"  # luckyvippro


async def tag_user(user_id, message, thumb, message_channel):
    mention = f"<@{user_id}>"
    embed = discord.Embed(description=f"{mention} {message}")
    embed.set_thumbnail(url=thumb)
    embed.color = discord.Color.purple()
    await message_channel.send(embed=embed)


async def muoibuon(message):
    await tag_user(
        wakuu,
        "Muối buồn ạ!",
        "https://cdn.discordapp.com/emojis/1117366343231082578.gif?size=128&quality=lossless",
        message.channel,
    )


async def miss_pam(message):
    await tag_user(
        agnes,
        "Anh nhớ chị ạ! Thèm quá",
        "https://cdn.discordapp.com/emojis/1117425666682536056.gif?size=128&quality=lossless",
        message.channel,
    )


async def miss_duong(message):
    await tag_user(
        agnes,
        "Chị nhớ anh!",
        "https://cdn.discordapp.com/emojis/1117425666682536056.gif?size=128&quality=lossless",
        message.channel,
    )


async def luv(message):
    await tag_user(
        agnes,
        "Love you! Yêu yêu yêu ❤️💕",
        "https://cdn.discordapp.com/emojis/827406624339394571.gif?size=128&quality=lossless",
        message.channel,
    )
    await tag_user(
        wakuu,
        "Love you! Yêu yêu yêu ❤️💕",
        "https://cdn.discordapp.com/emojis/827406624339394571.gif?size=128&quality=lossless",
        message.channel,
    )
