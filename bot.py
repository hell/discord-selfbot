import os

import discord
from discord.ext import commands
import yaml


settings = yaml.safe_load(open("settings.yml", "r").read())

bot = commands.Bot(command_prefix='.', 
                   self_bot=True,
                   case_sensitive=False)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
bot.run(settings['token'], bot=False)
