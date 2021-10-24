import discord
from discord.ext import commands

class Fun(commands.Cog):
    
    def __init__(self, bot):
      self.bot = bot
    
    # a simple command to test the bot's reponse time
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f"pong! {self.bot.latency * 1000}")

    # a command with arguments, invoked like !say <text>
    @commands.command() 
    async def say(self, ctx, text):
      await ctx.send(text)

    # a quick intro to embeds
    @commands.command() 
    async def embed(self, ctx):
      embed = discord.Embed(title = "Title", description = "A short description")
      embed.add_field(name = "A new field", value = "some text")
      embed.add_field(name = "A new field", value = "some text")
      embed.add_field(name = "A new field", value = "some text")
      embed.add_field(name = "A new field", value = "embeds can have up to 3 fields per row")
      embed.add_field(name = "A new field", value = "you can make it 1 field per row", inline = False)
      await ctx.send(embed = embed)

def setup(bot):
  bot.add_cog(Fun(bot))