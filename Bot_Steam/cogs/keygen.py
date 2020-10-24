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
	async def keygen (self, ctx ):
		for x in range( 1 ): # Loop to repeat the generation of random keys
			password = ''
		for i in range( 15 ):
			chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
			key = random.choice(chars)
			password =password+(key)
			if len(password)== 5 or len(password)== 11: # Where will the dash be placed
				password=password+"-"
		print( password )
		author = ctx.message.author
		await ctx.send( f" { author.mention } Your key has been generated: " f" { password }"    )

def setup(client):
	client.add_cog(User(client))