import discord
from discord.ext import commands
import json
from src.service.player_service import PlayerService
from src.config.load_config import load_configuration

config = load_configuration()

intents = discord.Intents.default()
intents.message_content = True  # Privileged intent
intents.members = True         # Privileged intent

bot = commands.Bot(
    command_prefix=config["prefix"],
    intents=intents,
    allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True)
)

@bot.event
async def setup_hook():
    await bot.add_cog(PlayerService(bot))

@bot.event
async def on_ready():
    permissions = discord.Permissions(2147552256)
    print(f"{bot.user} está online!")
    print(f"Link de convite: {discord.utils.oauth_url(bot.user.id, permissions=permissions)}")

bot.run(config["token"])