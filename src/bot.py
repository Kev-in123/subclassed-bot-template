import os
from discord.ext import commands

# subclassing commands.Bot
class Bot(commands.Bot):

  # constructor class for the bot
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  # running the bot and loading the cogs
  def run(self, token):
    
    for cog in os.listdir("cogs"):
      if cog.endswith(".py"):
        self.load_extension(f"cogs.{cog[:-3]}")

    super().run(token)
    
