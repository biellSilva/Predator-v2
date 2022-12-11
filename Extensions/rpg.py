import discord
import random
import pytz
import re

from discord import app_commands
from discord.ext import commands
from typing import Optional


tz_brazil = pytz.timezone('America/Sao_Paulo')

roxo = 0x690FC3
vermelho = 0xff0000

comandos = 1000948732235362325


@app_commands.guild_only()
class rpgCommands(commands.GroupCog, name='rpg'):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dado')
    @app_commands.describe(dados='Informe quantos dados e quantos lados. ex.: 4d6')
    async def dado(self, interaction: discord.Interaction, dados: str):

        '''Tente a sorte nos dados'''

        guild = interaction.guild
        dados = dados.lower()

        #if interaction.channel.id != comandos:
        #    comand = guild.get_channel(comandos)
        #    await interaction.response.send_message(f'Apenas em {comand.mention}', ephemeral=True)
        #    return

        em = discord.Embed(title='Dados', color=roxo, description=dados)

        await interaction.response.send_message(embed=em)
        msg = await interaction.original_response()

        if ('d' not in dados) or (len(dados) < 3):
            em.color = vermelho
            em.description = f'Error:\nEsperado: ex.: 4d6\nRecebido: {dados}'
            await msg.edit(embed=em)
            return

        x = re.split(r'[d|+|*|/|-]', dados)

        print(x)

        q_dados = int(x[0])
        q_lados = int(x[1])

        em.title = f'Dados - {dados}'

        if 0 < q_dados > 20:
            em.color = vermelho
            em.description = 'Error:\nLimite  de dados: 1 ~ 20'
            await msg.edit(embed=em)
            return

        if 2 < q_lados > 100:
            em.color = vermelho
            em.description = 'Error:\nLimite  de lados: 2 ~ 100'
            await msg.edit(embed=em)
            return

        if q_lados > 2:
            soma = soma_dados(q_dados, q_lados)

            em.color = roxo
            em.description = f'{q_dados} {"dado" if q_dados > 1 else "dados"} de {q_lados} lados:\n{soma[0]}'

            if '+' in dados:
                fim = int(soma[1]) + int(x[2])
                em.description += f'= {soma[1]} + {x[2]} = {fim}'

            elif '-' in dados:
                fim = int(soma[1]) - int(x[2])
                em.description += f'= {soma[1]} - {x[2]} = {fim}'

            elif '*' in dados:
                fim = int(soma[1]) * int(x[2])
                em.description += f'= {soma[1]} * {x[2]} = {fim}'

            elif '/' in dados:
                fim = int(soma[1]) / int(x[2])
                em.description += f'= {soma[1]} / {x[2]} = {fim}'
            
            elif 'kh' in dados:
                texto = ''
                a = 0
                lista = soma[2].sort(reverse=True)
                y = lista[{x[2]}]
                em.description += f'\nKH {y}\n'
                for kh in y:
                    texto += f'{kh} +'
                    a += int(kh)
                em.description += f'{texto:-3} = {a}'

            else:
                em.description += f'= {soma[1]}'

            await msg.edit(embed=em)


def soma_dados(dados, lados):
    soma = 0
    texto = ''
    lista = []

    for y in range(dados):
        dado = random.randint(1, lados)
        texto += f'{dado} + '
        soma += dado
        lista.append(dado)
    end_text = f'{texto[:-2]}'

    return end_text, soma, lista


async def setup(bot):
    await bot.add_cog(rpgCommands(bot))
