import discord
from discord.ext.commands import Bot
import asyncio
from selenium import webdriver
import time
import random

client = Bot("!")

berufe = ["Professor der Medizin", "Dr der Medizin", "Biologe", "Elektroniker", "Arzt", "Informatiker", "Mathematiker", "Virologe", "Historiker", "Musiker", "Influencer", "Bürokaufmann", "Verkäufer", "Müllmann", "ein Hurensohn", "Elektriker", "Tischler", "Corona-Surviver", "Bestatter", "Totengräber", "Obdachloser", "Harzer"]

@client.event
async def on_ready():
    print("Wir sind eingeloggt!")
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Mr Krabs overdoses on Ketamine"), status=discord.Status.online)
        await asyncio.sleep(1)

@client.command(name = "helpme")
async def helpme(ctx):
    await ctx.send("Hallo ich bin das FBI\nBisher habe ich nur zwei Commands: \"!kick\" und \"!ban\"\nBald wird mein Creator Dr.Schröter hoffentlich ein paar neue Commands entwickeln.")


@client.command(name = "kick", pass_context = True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.send("User " + member.display_name + " has been kicked!")
    print("User " + member.display_name + " has been kicked!")

@client.command(name = "ban", pass_context = True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.send("User " + member.display_name + " has been banned!")
    print("User " + member.display_name + " has been banned!")

@client.command(name = "beruf")
async def Beruf(ctx):
    await ctx.send(ctx.message.author.name + " wird warscheinlich " + random.choice(berufe))

@client.command(name="Raid", pass_context=True)
async def raid(ctx):
    channel = ctx.message.author.voice.channel
    voicechannel = await channel.conncet()
    voicechannel.play(discord.FFmpegPCMAudio("FBI.mp3"))

    print("Bot ist Channel " + str(channel) + " gejoined")

    while voicechannel.is_playing():
        time.sleep(5)
    
    await voicechannel.disconnect()
    await ctx.send("Raid complete")

    print("Bot hat den Voicechannel verlassen")
    
    



client.run('Nzg5NDM3NzA1MTY3Njk5OTY4.X9yDJw.yJRRnSrjYOldzPhkYlUqgrlWwCQ')