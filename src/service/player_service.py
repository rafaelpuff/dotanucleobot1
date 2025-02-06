import discord
from discord.ext import commands
from src.repository.command.player_repository import PlayerPersistence
from src.utils.checks import is_allowed_channel

def get_role_name(position: str) -> str:
    roles = {
        "1": "HC",
        "2": "MID",
        "3": "OFF",
        "4": "SUP4",
        "5": "SUP5"
    }
    return roles.get(position, position)

class PlayerService(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.player_persistence = PlayerPersistence()

    @commands.command(name="ajuda")
    @is_allowed_channel()
    async def help(self, ctx):
        """Mostra a lista de comandos disponíveis"""
        embed = discord.Embed(
            title="Comandos Disponíveis",
            color=0x00ff00,
            description="Lista de todos os comandos que você pode usar:"
        )

        commands_info = {
            "!registrar [role] [nick]": "Registra você como jogador. Role deve ser 1-5. Nick é opcional.",
            "!info [@ menção]": "Mostra suas informações ou de outro jogador mencionado.",
            "!lista": "Mostra a lista de todos os jogadores ordenada por MMR.",
            "!atualizar_nome [nome]": "Atualiza seu nickname.",
            "!atualizar_role [role]": "Atualiza sua role (1-5).",
            "!ajuda": "Mostra esta mensagem de ajuda."
        }

        for cmd, desc in commands_info.items():
            embed.add_field(
                name=cmd,
                value=desc,
                inline=False
            )

        await ctx.send(embed=embed)

    @commands.command(name="atualizar_nome")
    @is_allowed_channel()
    async def update_name(self, ctx, *, new_name: str):
        """Atualiza o nome do jogador
        
        Argumentos:
        new_name -- Novo nome do jogador
        """
        try:
            player = self.player_persistence.find_by_discord_id(ctx.author.id)
            if not player:
                await ctx.send("Você precisa se registrar primeiro usando !registrar")
                return
            
            old_name = player.name
            self.player_persistence.update_player(ctx.author.id, name=new_name)
            
            await ctx.send(f"Nome atualizado com sucesso de **{old_name}** para **{new_name}**!")
        except Exception as e:
            print(f"Erro ao atualizar nome: {str(e)}")
            await ctx.send("Erro ao atualizar nome. Por favor, tente novamente mais tarde.")

    @commands.command(name="atualizar_role")
    @is_allowed_channel()
    async def update_role(self, ctx, new_role: str):
        """Atualiza a role do jogador
        
        Argumentos:
        new_role -- Nova role (1-5)
        """
        if new_role not in ["1", "2", "3", "4", "5"]:
            await ctx.send("Role inválida! Use um número de 1 a 5.")
            return

        try:
            player = self.player_persistence.find_by_discord_id(ctx.author.id)
            if not player:
                await ctx.send("Você precisa se registrar primeiro usando !registrar")
                return
            
            old_role = get_role_name(player.position)
            self.player_persistence.update_player(ctx.author.id, position=new_role)
            
            await ctx.send(f"Role atualizada com sucesso de **{old_role}** para **{get_role_name(new_role)}**!")
        except Exception as e:
            print(f"Erro ao atualizar role: {str(e)}")
            await ctx.send("Erro ao atualizar role. Por favor, tente novamente mais tarde.")

    @commands.command(name="lista")
    @is_allowed_channel()
    async def list_players(self, ctx):
        """Lista todos os jogadores registrados, ordenados por MMR"""
        try:
            # Busca todos os jogadores e ordena por MMR decrescente
            players = self.player_persistence.get_all_players()
            if not players:
                await ctx.send("Nenhum jogador registrado ainda!")
                return

            # Ordena os jogadores por MMR decrescente
            sorted_players = sorted(players, key=lambda x: x.mmr, reverse=True)

            # Formata a lista de jogadores em uma linha cada
            player_lines = []
            for i, player in enumerate(sorted_players, 1):
                role_name = get_role_name(player.position)
                member = ctx.guild.get_member(player.discord_id)
                name = member.name if member else player.name
                player_lines.append(f"{i}. ```{player.mmr}``` **{name}** ```{role_name}```")

            # Envia uma mensagem para cada jogador
            for line in player_lines:
                await ctx.send(line)

        except Exception as e:
            print(f"Erro ao listar jogadores: {str(e)}")
            await ctx.send("Erro ao listar jogadores. Por favor, tente novamente mais tarde.")

    @commands.command(name="registrar")
    @is_allowed_channel()
    async def register(self, ctx, position: str, *, nickname: str = None):
        """Registra um novo jogador usando informações do Discord
        
        Argumentos:
        position -- Role (1-5)
        nickname -- Nick personalizado (opcional)
        """
        if position not in ["1", "2", "3", "4", "5"]:
            await ctx.send("Role inválida! Use um número de 1 a 5.")
            return

        # Verifica se o jogador já existe
        existing_player = self.player_persistence.find_by_discord_id(ctx.author.id)
        if existing_player:
            await ctx.send(f"{ctx.author.mention}, você já está registrado na role {get_role_name(existing_player.position)}!")
            return

        try:
            # Usa o nickname fornecido ou o nome do Discord como fallback
            player_name = nickname if nickname else ctx.author.name
            
            player = self.player_persistence.add_player(
                discord_id=ctx.author.id,
                name=player_name,
                position=position
            )
            await ctx.send(f"Jogador {ctx.author.mention} registrado com sucesso na role {get_role_name(position)} com o nick: {player_name}!")
        except Exception as e:
            print(f"Erro ao registrar jogador: {str(e)}")
            await ctx.send("Erro ao registrar jogador. Por favor, tente novamente mais tarde.")

    @commands.command(name="info")
    @is_allowed_channel()
    async def info(self, ctx, member: discord.Member = None):
        """Mostra informações do jogador
        
        Argumentos:
        member -- Membro do Discord (opcional, mostra info do autor se não especificado)
        """
        target = member if member else ctx.author
        
        try:
            player = self.player_persistence.find_by_discord_id(target.id)
            if player:
                embed = discord.Embed(
                    color=0x00ff00,
                    description="\u200b"  # Caractere invisível para manter o espaçamento
                )
                
                # Configura o autor com a foto e nome
                embed.set_author(
                    name=player.name,
                    icon_url=target.display_avatar.url
                )
                
                # Campos com valores em caixas
                role_name = get_role_name(player.position)
                embed.add_field(
                    name="Role",
                    value=f"```{role_name}```",
                    inline=True
                )
                embed.add_field(
                    name="MMR",
                    value=f"```{player.mmr}```",
                    inline=True
                )
                embed.add_field(
                    name="Vitórias",
                    value=f"```{player.wins}```",
                    inline=True
                )
                embed.add_field(
                    name="Derrotas",
                    value=f"```{player.losses}```",
                    inline=True
                )
                embed.add_field(
                    name="Abandonos",
                    value=f"```{player.abandons}```",
                    inline=True
                )
                
                # Adiciona o Discord ID como footer
                embed.set_footer(text=f"Discord ID: {target.id}")
                
                await ctx.send(embed=embed)
            else:
                target_name = target.name
                await ctx.send(f"{target_name} não está registrado!")
        except Exception as e:
            print(f"Erro ao buscar informações do jogador: {str(e)}")
            await ctx.send("Erro ao buscar informações do jogador. Por favor, tente novamente mais tarde.")
