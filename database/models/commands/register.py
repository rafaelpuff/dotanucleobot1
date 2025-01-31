import discord
from discord.ext import commands
from database.db_connection import get_db_connection

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="registrar")
    async def register(self, ctx):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM players WHERE discord_id = %s", (ctx.author.id,))
        if cursor.fetchone():
            await ctx.send(f"{ctx.author.mention}, você já está registrado!")
            return
        
        await ctx.send(f"{ctx.author.mention}, escolha sua posição favorita (Pos1, Pos2, Pos3, Pos4, Pos5):")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30)
            position = msg.content.upper()

            if position not in ["POS1", "POS2", "POS3", "POS4", "POS5"]:
                await ctx.send(f"{ctx.author.mention}, posição inválida.")
                return

            cursor.execute("INSERT INTO players (discord_id, name, position) VALUES (%s, %s, %s)",
                           (ctx.author.id, ctx.author.name, position))
            conn.commit()

            await ctx.send(f"{ctx.author.mention}, registrado com sucesso!")

        except Exception as e:
            await ctx.send(f"Erro: {str(e)}")

        finally:
            cursor.close()
            conn.close()
