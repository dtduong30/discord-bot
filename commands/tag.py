import discord

agnes = "341107845523046400"
wakuu = "449456684767641600"  # luckyvippro


def get_receiver_id(sender_id):
    if str(sender_id) == agnes:
        return wakuu
    elif str(sender_id) == wakuu:
        return agnes
    else:
        return None


async def tag_user(message, msg, thumb, message_channel, is_target=None):
    sender_id = message.author.id
    if is_target is not None:
        receiver_id = is_target
        sender_mention = ""
    else:
        receiver_id = get_receiver_id(sender_id)
        sender_mention = f"<@{sender_id}>"

    if receiver_id is None:
        await message.channel.send("You are not authorized to use this command.")
        return
    receiver_mention = f"<@{receiver_id}>"
    embed = discord.Embed(description=f"{sender_mention} nhắn: {msg}")
    embed.set_thumbnail(url=thumb)
    embed.color = discord.Color.purple()
    await message_channel.send(receiver_mention, embed=embed)


async def muoibuon(message):
    await tag_user(
        message,
        "Muối buồn ạ!",
        "https://cdn.discordapp.com/emojis/1117366343231082578.gif?size=128&quality=lossless",
        message.channel,
        wakuu,
    )


async def miss(message):
    await tag_user(
        message,
        "nhớ lắm!",
        "https://cdn.discordapp.com/emojis/1117425666682536056.gif?size=128&quality=lossless",
        message.channel,
    )


async def luv(message):
    await tag_user(
        message,
        "Love you! Yêu yêu yêu ❤️💕",
        "https://cdn.discordapp.com/emojis/827406624339394571.gif?size=128&quality=lossless",
        message.channel,
    )


async def g9(message):
    await tag_user(
        message,
        "Ngủ ngon ạ, lớp diu ❤️💕",
        "https://cdn.discordapp.com/emojis/827406624339394571.gif?size=128&quality=lossless",
        message.channel,
    )


async def lick(message):
    await tag_user(
        message,
        "Thèm đc liếm ạ ❤️💕",
        "https://cdn.discordapp.com/emojis/995765755075379240.gif?size=96&quality=lossless",
        message.channel,
    )


async def bc(message):
    await tag_user(
        message,
        "Thèm đc bú cu ạ ❤️💕",
        "https://cdn.discordapp.com/emojis/995765755075379240.gif?size=96&quality=lossless",
        message.channel,
        wakuu,
    )


async def touch_cheek(message):
    await tag_user(
        message,
        "Yêu yêu, cụng má ❤️💕",
        "https://i.pinimg.com/originals/9c/94/78/9c9478bb26b2160733ce0c10a0e10d10.gif",
        message.channel,
        agnes,
    )


async def petting(message):
    await tag_user(
        message,
        "Nựng má ❤️💕",
        "https://i.pinimg.com/originals/8d/82/8c/8d828c5055047d95b2e75b533147f0fd.gif",
        message.channel,
        agnes,
    )
