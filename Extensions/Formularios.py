import discord
import discord.utils
import datetime
import pytz
import config

from discord.ext import commands
from discord import app_commands, Interaction

tz_brazil = pytz.timezone('America/Sao_Paulo')


class Denuncia(discord.ui.Modal, title='Registro de Denúncia'):
    warframe = discord.ui.TextInput(label='Warframe', required=False, placeholder='Nome#000')
    discord_name = discord.ui.TextInput(label='Discord', required=False, placeholder='Nome#000')
    razao = discord.ui.TextInput(label='Motivo da denúncia', style=discord.TextStyle.paragraph, required=True, placeholder='Xingamentos')

    async def on_submit(self, interaction: Interaction):
        guild = interaction.guild
        author = interaction.user
        formChannel = guild.get_channel(config.formularios)

        em = discord.Embed(title='Registro de Denúncia',
                           color=config.roxo,
                           description=f'**Warframe:** {self.warframe}\n'
                           f'**Discord:** {self.discord_name}\n'
                           f'**Razão:** {self.razao}\n\n'
                           f'{author.mention} - {author.id}')

        em.set_thumbnail(url=guild.icon)
        em.set_footer(text=f'Registrado por {author}', icon_url=author.avatar)
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await formChannel.send(embed=em)
        await interaction.response.send_message(f'Registro enviado para a moderação', embed=em, ephemeral=True)

    async def on_error(self, interaction: Interaction):
        await interaction.response.send_message('Ocorreu um erro e sua denuncia foi cancelada', ephemeral=True)


class Criador(discord.ui.Modal, title='Criador de Conteúdo'):
    warframe = discord.ui.TextInput(label='Warframe', required=True, placeholder='Nome#000')
    youtube = discord.ui.TextInput(label='Youtube', required=False, placeholder='https://youtube.com/user')
    twitch = discord.ui.TextInput(label='Twitch', required=False, placeholder='https://twitch.tv/user')
    razao = discord.ui.TextInput(label='Informações Extras', style=discord.TextStyle.paragraph, required=False, placeholder='Stream de Warframe 10 horas por dia')

    async def on_submit(self, interaction: Interaction):
        guild = interaction.guild
        author = interaction.user
        formChannel = guild.get_channel(config.formularios)

        em = discord.Embed(title='Criador de Conteúdo',
                           color=config.roxo,
                           description=f'**Warframe:** {self.warframe}\n'
                           f'**Twitch:** {self.twitch}\n'
                           f'**Youtube:** {self.youtube}'
                           f'**Extras:** {self.razao}\n\n'
                           f'{author.mention} - {author.id}')

        em.set_thumbnail(url=guild.icon)
        em.set_footer(
            text=f'Registrado por {author}', icon_url=author.avatar)
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await formChannel.send(embed=em)
        await interaction.response.send_message(f'Registro enviado para a moderação', embed=em, ephemeral=True)

    async def on_error(self, interaction: Interaction):
        await interaction.response.send_message('Ocorreu um erro e seu pedido foi cancelado', ephemeral=True)

@app_commands.guild_only()
class Formularios(commands.GroupCog, name='forms'):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name='denuncia')
    async def report(self, interaction: discord.Interaction):
        '''Pode denúnciar um membro do Warframe ou Discord'''

        await interaction.response.send_modal(Denuncia())

    @app_commands.command(name='criador')
    async def criador(self, interaction: discord.Interaction):
        '''Faz um pedido pelos cargos de Streamer e/ou Youtuber'''

        await interaction.response.send_modal(Criador())


async def setup(bot):
    await bot.add_cog(Formularios(bot))
