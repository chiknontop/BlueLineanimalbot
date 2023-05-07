import discord
import requests
import json
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

embedimage = "https://cdn.discordapp.com/attachments/1104556106916831343/1104805611092320276/v6zop3p2sb32fidi77.png"
embedcolor = 0x2563EB

@bot.slash_command(name='help', description='Sends all Command info!')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="BlueLine Help Menu", description="```ini\n[ ping ] -> Sends Bot Ping\n[ cat ] -> Sends Random Cat Image\n[ catgif ] -> Sends Random Cat Gif\n[ dog ] -> Sends random dog image```", color=embedcolor)
    embed.set_image(url=embedimage)
    embed.set_footer(text=f"Powered By BlueLine Animals")

    await interaction.send(embed=embed)

@bot.slash_command(name='ping', description='Whats my ping?')
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(title="BlueLine Ping Info:", color=embedcolor)
    embed.add_field(name="Bot Ping:", value=f"```ini\n[ {round(bot.latency * 1000)}ms ]```", inline=True)
    embed.add_field(name="Image Api Ping", value=f"```ini\n[ 69ms ]```", inline=True)
    embed.set_image(url=embedimage)
    embed.set_footer(text=f"Powered By BlueLine Animals")

    await interaction.send(embed=embed)

# animal commands

@bot.slash_command(name='cat', description='Sends Random Cat Image!')
async def cat(interaction: discord.Interaction):
    try:
        response = requests.get("https://cataas.com/cat?json=true")
        data = json.loads(response.text)
        image = data['url']

        embed = discord.Embed(title="Random Cat Image :zany_face:", color=embedcolor)
        embed.set_image(url=f"https://cataas.com/{image}")
        embed.set_footer(text=f"Powered By https://cataas.com/")

        await interaction.send(embed=embed)
    except:
        embed = discord.Embed(title="API ERROR", description="```ini\n[ UNKNOWN API ERROR! ]```", color=embedcolor)
        embed.set_footer(text=f"Powered By https://cataas.com/")

        await interaction.send(embed=embed)

@bot.slash_command(name='catgif', description='Sends Random Cat GIF!')
async def catgif(interaction: discord.Interaction):
    try:
        response = requests.get("https://cataas.com/cat/gif?json=true")
        data = json.loads(response.text)
        image = data['url']

        embed = discord.Embed(title="Random Cat Gif :zany_face:", color=embedcolor)
        embed.set_image(url=f"https://cataas.com/{image}")
        embed.set_footer(text=f"Powered By https://cataas.com/")

        await interaction.send(embed=embed)
    except:
        embed = discord.Embed(title="API ERROR", description="```ini\n[ UNKNOWN API ERROR! ]```", color=embedcolor)
        embed.set_footer(text=f"Powered By https://cataas.com/")

        await interaction.send(embed=embed)

@bot.slash_command(name='dog', description='Sends Random Dog Image!')
async def dog(interaction: discord.Interaction):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = json.loads(response.text)

    if data['status'] == 'success':
        embed = discord.Embed(title="Random Dog Image :zany_face:", color=embedcolor)
        embed.set_image(url=data['message'])
        embed.set_footer(text=f"Powered By https://dog.ceo/")

        await interaction.send(embed=embed)
    else:
        embed = discord.Embed(title="API ERROR", description="```ini\n[ UNKNOWN API ERROR! ]```", color=embedcolor)
        embed.set_footer(text=f"Powered By https://dog.ceo/")

        await interaction.send(embed=embed)


bot.run('')
