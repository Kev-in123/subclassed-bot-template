import discord
from bot import Bot

bot = Bot(
    command_prefix = "!",
    activity = discord.Game("!help")
  )

bot.run("TOKEN")