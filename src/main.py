import discord
from bot import Bot

# bot constructor, edit this to your needs.
bot = Bot(
    command_prefix = "!",
    activity = discord.Game("!help")
  )

bot.run("TOKEN") #  change `TOKEN` to your bot's token
# running a bot like this is not recommended (token is visible in the source) but for the sake of this template, it's gonna be like this
