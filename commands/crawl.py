import requests
import json
import discord


def desired_string(link):
    start_index = link.find("p.")
    if start_index == -1:
        return None  # Return None if "p." is not found in the link
    start_index += len("p.")

    # Find the end index of the desired string, accounting for "?"
    end_index = link.find("?")
    if end_index != -1:
        desired_string = link[start_index:end_index]
    else:
        desired_string = link[
            start_index:
        ]  # If "?" is not found, take the substring until the end of the link

    return desired_string


async def crawl_bee_cost(message):
    # Extract the link from the message content
    link = message.content.split(" ")[1]
    print(link)
    product_base_id = desired_string(link)
    print(product_base_id)
    if product_base_id == "":
        print("Product ID:", product_base_id)
        await message.channel.send("Failed to fetch data from API")
        return

    # Call the API to get product details
    response = requests.get(
        f"https://apiv3.beecost.vn/product/detail?product_base_id={product_base_id}&type=new"
    )

    if response.status_code == 200:
        data = response.json()["data"]["product_base"]
        # print(data)
        name = data.get("name", "")
        price = data.get("price", 0)
        price_before_discount = data.get("price_before_discount", 0)
        img = data.get(
            "url_thumbnail",
            "https://cdn.discordapp.com/emojis/1113660133877235803.webp?size=128&quality=lossless",
        )
        # print(f"Name: {name} \n Price: {price} \n Price before discount: {price_before_discount}")
        # Format the price to VND currency
        formatted_price = "{:,.0f} đ".format(price)
        formatted_price_before_discount = "{:,.0f} đ".format(price_before_discount)
        # Create an embed with the message content
        embed = discord.Embed(title="Product Details", color=0x00FF00)  # Green color
        embed.add_field(name="Name", value=name, inline=False)
        embed.add_field(name="Price", value=formatted_price, inline=False)
        embed.add_field(
            name="Price before discount",
            value=formatted_price_before_discount,
            inline=False,
        )
        embed.set_image(url=img)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/1113660133877235803.webp?size=128&quality=lossless"
        )

        # Send the response to the Discord channel
        await message.channel.send(embed=embed)
    else:
        await message.channel.send("Failed to fetch data from API")
