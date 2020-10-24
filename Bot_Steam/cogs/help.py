import discord
import random 
from discord.ext import commands


class User(commands.Cog):

	def _int_(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Keygen has loaded...") #Displaying text that means the command is working

	@commands.command()
	async def Steam_Help(self, ctx, aliases = ['Shelp', 'Steam_Help', 'Help_Steam', 'help_steam', 'steam_help'] ):
		embed = discord.Embed(title="Steam_bot", description="Вот список доступных команд:", color=0xeee657)
		embed.add_field(name="🎨Meme🎨", value='!game_mem⠀', inline=False)
		embed.add_field(name="🎳Game🎳", value='''
												!nice_game
												!keygen
												''', inline=False)
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(User(client))