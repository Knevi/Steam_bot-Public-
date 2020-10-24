import discord
import os
from discord import Activity, ActivityType
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event 

async def on_ready():
	print("Bot_conect") #Displaying text that means the bot is running
	await client.change_presence(status=discord.Status.idle,activity=Activity(name="Steam game",type=ActivityType.watching)) #Bot status

@client.command() #Load cogs
async def load(ctx, extension):
	if ctx.author.id == 469923140084957194:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("You are not a developer")


@client.command() #unload cogs
async def unload(ctx, extension): 
	if ctx.author.id == 469923140084957194:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs is unloaded...")
	else:
		await ctx.send("You are not a developer")

@client.command() #reload cogs
async def reload(ctx, extension): 
	if ctx.author.id == 469923140084957194:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}") 
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("You are not a developer")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

# Connect

token = open( "token.txt", "r" ).readline()

client.run( token )