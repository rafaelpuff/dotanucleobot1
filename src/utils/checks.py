from discord.ext import commands

ALLOWED_CHANNEL_ID = 1336515580857024572

def is_allowed_channel():
    async def predicate(ctx):
        return ctx.channel.id == ALLOWED_CHANNEL_ID
    return commands.check(predicate)
