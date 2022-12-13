import asyncio
import discord
import datetime
import random
import json
import os
import pytz
import config

from time import time
from discord.ext import commands
from discord import app_commands
from typing import Optional
from discord.app_commands import Choice
from operator import getitem

os.path.join(os.getcwd(), './json')

#   timezone brasil
tz_brazil = pytz.timezone('America/Sao_Paulo')

#   24 horas = 86400
cd_mapping = commands.CooldownMapping.from_cooldown(
    1, 86400, commands.BucketType.user)


class Personalizado(discord.ui.Modal, title='Compra de Cargo Personalizado'):
    nome = discord.ui.TextInput(label='Nome', placeholder='Dumb Dev')
    cor = discord.ui.TextInput(label='Cor', placeholder='hex: #121212')
    mencionavel = discord.ui.TextInput(label='Mencionavel', required=False, placeholder='Sim/Não', default='Sim')
    icone = discord.ui.TextInput(label='Icone', required=False, placeholder='https://')

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user

        form = guild.get_channel(1021369373782454292)

        em = discord.Embed(title='Compra de Cargo Personalizado',
                           color=config.roxo,
                           description=f'**Nome:** {self.nome}\n'
                           f'**Cor:** {self.cor}\n'
                           f'**Mencionavel:** {self.mencionavel}\n'
                           f'**Icone:** {self.icone}\n')

        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado por {user}', icon_url=user.avatar)
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        users = await get_bank_data()
        users[str(user.id)]['banco'] -= 5000000
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

        await form.send(embed=em)
        await interaction.response.send_message(f'Pedido enviado para {form.mention}', embed=em, ephemeral=True)

    async def on_error(self, interaction: discord.Interaction):
        await interaction.response.send_message('Ocorreu um erro e seu registro foi cancelado', ephemeral=True)


class Economia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    banco = app_commands.Group(name='banco', description='Comandos do Banco Cósmico', guild_only=True)
    loja = app_commands.Group(name='loja', description='Comandos da Loja Cósmica', guild_only=True)

    @commands.guild_only()
    @commands.is_owner()
    @commands.command()
    async def clearbank(self, ctx):

        if ctx.author.id != 420634633793699851:
            ctx.reply('Você não tem permissão para isso')
            return

        data = json.load(open("./json/bank.json", "r"))
        del (data)

        with open('./json/bank.json', 'w') as f:
            json.dump({}, f, indent=4)

        await ctx.reply('json limpo')

    @clearbank.error
    async def clear_error(self, ctx, err):
        await ctx.reply('de alguma forma você conseguiu chegar aqui, mas ainda não é o dono')
        return

    @commands.guild_only()
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def json(self, ctx):
        await ctx.reply(file=discord.File('./json/bank.json'))

    @commands.Cog.listener()
    async def on_message(self, message):

        msg_base = str(message.content)

        if message.author.bot:
            return

        if msg_base.startswith('p!') or msg_base.startswith('m!') or msg_base.startswith('!'):
            return

        user = message.author
        await open_account(user)
        users = await get_bank_data()

        msg = int(len(str(message.content)))+5
        if msg > 50: msg = 50
        valor = random.randrange(1, msg)

        users[str(user.id)]['banco'] += valor
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

        guild = self.bot.get_guild(config.uniao)
        log = guild.get_channel(config.loja_log)

        em = discord.Embed(title='Log',
                           color=config.roxo,
                           description=f'Mensagem: {user.mention} recebeu `{valor}`')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        if user.avatar != None:
            em.set_footer(text=f'{user}', icon_url=f'{user.avatar.url}')
        else:
            em.set_footer(text=f'{user}')
        await log.send(embed=em)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        guild = self.bot.get_guild(config.uniao)
        log = guild.get_channel(config.loja_log)

        if member.bot:
            return

        if after.channel == None:
            return

        if after.afk:
            return

        while after.channel is not None and (after.self_mute == False or after.self_deaf == False or after.mute == False or after.deaf == False):
            if before is not None or (after.self_stream == True or after.self_video == True) or after.afk:
                break

            user = member
            await open_account(user)
            users = await get_bank_data()

            valor1 = random.randrange(1, 100)

            users[str(user.id)]['banco'] += valor1
            with open('./json/bank.json', 'w') as f:
                json.dump(users, f, indent=4)

            em = discord.Embed(title=f'Log',
                               color=config.roxo,
                               description=f'Voice Stream: {member.mention} recebeu `{valor1}`')
            em.timestamp = datetime.datetime.now(tz=tz_brazil)
            em.set_footer(text=f'{member}', icon_url=f'{member.avatar.url}')
            await log.send(embed=em)

            await asyncio.sleep(600)

    @banco.command(name='conta')
    @app_commands.describe(membro='Selecione um membro')
    async def conta(self, interaction: discord.Interaction, membro: Optional[discord.Member]):

        '''Envia as informações da conta no Banco Cósmico'''

        user = interaction.user
        guild = interaction.guild

        if membro != None:

            await open_account(membro)
            users = await get_bank_data()

            bal = await update_bank(membro)
            cafe = users[str(membro.id)]['cafe']

            em = discord.Embed(title=f'Banco da {guild}',
                               color=config.roxo,
                               description=f'Olá {user.display_name}!\nEstas são as informações de {membro.display_name}:\n')
            em.add_field(name='Saldo de UCredits', value=f'{bal}')
            em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
            em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
            em.timestamp = datetime.datetime.now(tz=tz_brazil)

            if cafe > 0: em.add_field(name='Cafézinhos', value=f'{cafe}')

            await interaction.response.send_message(embed=em, ephemeral=True)
            return

        await open_account(user)
        users = await get_bank_data()

        bal = await update_bank(user)
        cafe = users[str(user.id)]['cafe']

        em = discord.Embed(title=f'Banco da {guild}',
                           color=config.roxo,
                           description=f'Olá {user.display_name}! Estas são suas informações:\n')
        em.add_field(name='Saldo de UCredits', value=f'{bal}')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        if cafe > 0: em.add_field(name='Cafézinhos', value=f'{cafe}')

        await interaction.response.send_message(embed=em, ephemeral=True)

    @banco.command(name='login')
    @app_commands.checks.cooldown(1, 86400)
    async def login(self, interaction: discord.Interaction):

        '''Login diário da Loja Cósmica'''

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas em <#{config.loja_comandos}>', ephemeral=True)
            return

        guild = interaction.guild
        user = interaction.user
        log = guild.get_channel(config.loja_log)

        await open_account(user)
        users = await get_bank_data()

        diario = random.randrange(100, 500)

        users[str(user.id)]['banco'] += diario
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

        em = discord.Embed(title=f'Login Diário',
                           color=config.roxo,
                           description=f'{user.display_name}, recebeu `{diario} UCredits` pelo login diário')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await interaction.response.send_message(embed=em)

        em = discord.Embed(title=f'Login diário',
                           color=config.roxo,
                           description=f'{user.mention} recebeu {diario}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await log.send(embed=em)

    @login.error
    async def login_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.CommandOnCooldown):
            dt = int(f'{time():.0f}') + int(f'{err.retry_after:.0f}')
            await interaction.response.send_message(f'calma, espere até <t:{dt}>, <t:{dt}:R>')

    @banco.command(name='doar')
    @app_commands.describe(membro='Selecione um membro', valor='Informe a quantia, deve ser numeros inteiros')
    async def doar(self, interaction: discord.Interaction, membro: discord.Member, valor: int):

        '''Doe/pague alguem enviando UCredits '''

        user = interaction.user
        guild = interaction.guild

        log = guild.get_channel(config.loja_log)

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas em <#{config.loja_comandos}>', ephemeral=True)
            return
        
        await open_account(membro)
        users = await get_bank_data()
        bal = await update_bank(user)

        if membro == user:
            await interaction.response.send_message('<:pepehmm:759975150367014952>?', ephemeral=True)
            return

        if valor < 0:
            await interaction.response.send_message('O valor de UCredits deve ser maior que `0`', ephemeral=True)
            return

        if valor > bal:
            em = discord.Embed(title=f'Sem Saldo',
                               color=config.roxo,
                               description=f'{user.display_name}, você não possui {valor} em UCredits')
            em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
            em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
            em.add_field(name='Saldo de UCredits', value=f'{bal}')
            em.timestamp = datetime.datetime.now(tz=tz_brazil)
            await interaction.response.send_message(embed=em, ephemeral=True)
            return

        em = discord.Embed(title=f'Doação de UCredits',
                           color=config.roxo,
                           description=f'{user.display_name} enviou {valor} UCredits para {membro.mention}')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await interaction.response.send_message(embed=em)


        users[str(user.id)]['banco'] -= valor
        users[str(membro.id)]['banco'] += valor
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

    @loja.command(name='ajuda')
    async def loja_cosmica(self, interaction: discord.Interaction):

        '''Loja Cósmica'''

        user = interaction.user
        guild = interaction.guild

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas no <#{config.loja_comandos}>', ephemeral=True)
            return

        # cargos padroes
        cargo1 = guild.get_role(1000948503905849446)
        cargo2 = guild.get_role(1000948507106095174)
        cargo3 = guild.get_role(1000948505306742825)
        cargo4 = guild.get_role(1000948506279825418)
        # cargos custons
        cargo5 = guild.get_role(1000948473555857499)
        cargo6 = guild.get_role(1000948475371982859)
        cargo7 = guild.get_role(1000948479188795412)
        cargo8 = guild.get_role(1000948474503757855)
        cargo9 = guild.get_role(1000948476466692167)
        cargo10 = guild.get_role(1000948477481717790)
        cargo11 = guild.get_role(1000948471311900712)
        cargo12 = guild.get_role(1000948481407598592)
        cargo13 = guild.get_role(1000948478287020122)
        cargo14 = guild.get_role(1000948482644901979)
        cargo15 = guild.get_role(1000948472545026128)
        cargo16 = guild.get_role(1000948480052826183)
        cargo17 = guild.get_role(1000948397043372042)
        cargo18 = guild.get_role(1000948398033211514)
        cargo19 = guild.get_role(1000948399044038776)
        cargo20 = guild.get_role(1000948400059076649)
        cargo21 = guild.get_role(1000948404152717463)
        cargo22 = guild.get_role(1000948405666861127)
        cargo23 = guild.get_role(1000948406740582451)
        cargo24 = guild.get_role(1000948407717867641)
        cargo25 = guild.get_role(1000948408892280893)
        cargo26 = guild.get_role(1000948410280579083)
        cargo27 = guild.get_role(1000948395906703476)

        em = discord.Embed(title='Loja Cósmica',
                           color=config.roxo,
                           description=f'**Cargos Padrões:**\n*custo: 2.000.000 UCredits*\n\n{cargo1.mention}\n{cargo2.mention}\n{cargo3.mention}\n{cargo4.mention}\n\n'

                           f'**Cargos Personalizados:**\n*custo: 5.000.000 UCredits*\n\n{cargo5.mention}\n{cargo6.mention}\n{cargo7.mention}\n{cargo8.mention}'
                           f'\n{cargo9.mention}\n{cargo10.mention}\n{cargo11.mention}\n{cargo12.mention}\n{cargo13.mention}\n{cargo14.mention}'
                           f'\n{cargo15.mention}\n{cargo16.mention}\n{cargo17.mention}\n{cargo18.mention}\n{cargo19.mention}\n{cargo20.mention}'
                           f'\n{cargo21.mention}\n{cargo22.mention}\n{cargo23.mention}\n{cargo24.mention}\n{cargo25.mention}\n{cargo26.mention}'
                           f'\n{cargo27.mention}'

                           '\n\nPara comprar um dos cargos ou criar seu cargo personalizado `/loja compra`'
                           '\nPara criar novos cargos personalizados preencha o formulario informando tudo que deseja nele, nome, cor, etc\nCor deve ser passada em HEX (#ffffff por exemplo)')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'{guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        await interaction.response.send_message(embed=em, ephemeral=True)
           
    @loja.command(name='compra')
    @app_commands.describe(tipo='Cargo padrão ou personalizado?', cargo='Selecione o cargo padrão que deseja comprar')
    @app_commands.choices(tipo=[
        Choice(name='Padrão', value='pad'),
        Choice(name='Personalizado', value='per')
    ],
        cargo = [
            Choice(name='Traficante de Rivens', value='tra'),
            Choice(name='Tenno Master', value='ten'),
            Choice(name='Viciado em Café', value='vic'),
            Choice(name='Tony Hawk do K-Drive', value='ton'),
        ])
    async def custom(self, interaction: discord.Interaction, tipo: str, cargo: Optional[str]):

        '''Compra cargo padrão ou personalizado'''

        user = interaction.user
        guild = interaction.guild

        users = await get_bank_data()
        bal = await update_bank(user)

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'Apenas no <#{config.loja_comandos}>', ephemeral=True)
            return

        if tipo == 'pad':

            if cargo == None:
                await interaction.response.send_message(f'Você deve informar qual cargo padrão quer comprar', ephemeral=True)
                return

            valor = 2000000
            if bal < valor:
                em = discord.Embed(title=f'Sem Saldo',
                                color=config.roxo,
                                description=f'{user.display_avatar}, você não possui UCredits suficientes')
                em.add_field(name='Balanço atual', value=f'{bal}')
                em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
                em.set_footer(text=f'{guild}', icon_url=f'{guild.icon}')
                em.timestamp = datetime.datetime.now(tz=tz_brazil)
                await interaction.response.send_message(embed=em, ephemeral=True)

            else:
                if cargo == 'tra':
                    cargo_add = guild.get_role(1000948503905849446)

                if cargo == 'ten':
                    cargo_add = guild.get_role(1000948507106095174)

                if cargo == 'vic':
                    cargo_add = guild.get_role(1000948505306742825)

                if cargo == 'ton':
                    cargo_add = guild.get_role(1000948506279825418)

            await user.add_roles(cargo_add)
            
            em = discord.Embed(title='Loja Cósmica', color=config.roxo,
                               description=f'{user.display_name}, o cargo {cargo_add.mention} foi entregue conforme sua compra')
            em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
            em.set_footer(text=f'{guild}', icon_url=f'{guild.icon}')
            em.timestamp = datetime.datetime.now(tz=tz_brazil)

            users[str(user.id)]['banco'] -= valor
            with open('./json/bank.json', 'w') as f:
                json.dump(users, f, indent=4)

            await interaction.response.send_message(embed=em)

        if tipo == 'per':
            valor = 5000000
            if bal < valor:
                em = discord.Embed(title=f'Sem Saldo',
                                   color=config.roxo,
                                   description=f'{user.display_avatar}, você não possui UCredits suficientes')
                em.add_field(name='Balanço atual', value=f'{bal}')
                em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
                em.set_footer(text=f'{guild}', icon_url=f'{guild.icon}')
                em.timestamp = datetime.datetime.now(tz=tz_brazil)
                await interaction.response.send_message(embed=em)

            else:
                await interaction.response.send_modal(Personalizado())

    @app_commands.guild_only()
    @app_commands.command(name='cafe')
    async def cafe(self, interaction: discord.Interaction):

        '''Compra um cafézinho'''

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev) and (interaction.channel.id != config.comandos):
            await interaction.response.send_message(f'Apenas no <#{config.comandos}>, <#{config.comandos_staff}>, <#{config.loja_comandos}>', ephemeral=True)
            return

        guild = interaction.guild
        user = interaction.user

        sala = interaction.channel_id
        sala = guild.get_channel(sala)

        await interaction.response.send_message('```\n'
                                                        'Boa tarde senhor(a), gostaria de um café?\n'
                                                        'Temos os seguintes grãos:\n'
                                                        '1: Especial, Jacu Bird - 800 créditos\n'
                                                        '2: Especial, Bravo Tenor - 500 créditos\n'
                                                        '3: Gourmet, Orfeu Clássico - 100 créditos\n'
                                                        '4: Superior, Café Brasileiro - 50 créditos\n'
                                                        '5: Extraforte, Pilão - 10 créditos e sua dignidade\n'
                                                        'Me informe o número de qual deseja'
                                                        '```', file=discord.File('./imagens/cafe/tipos.jpg'))
        def check(message):
            return message.author == user

        async def cafezin():
            response = await self.bot.wait_for('message', check=check)
            return response.content

        tipo = await cafezin()

        if (tipo != '1') and (tipo != '2') and (tipo != '3') and (tipo != '4') and (tipo != '5'):
            async with sala.typing():
                await asyncio.sleep(0.2)
            await sala.send('Lamento mas não servimos este café aqui...')
            return

        users = await get_bank_data()
        bal = await update_bank(user)

        if tipo == '1':
            custo = 800
            if bal < custo:
                await sala.send('Cartão recusado!')
                return
            async with sala.typing():
                await asyncio.sleep(3)
                await sala.send('hmm, aprecio sua preferência pelo belíssimo Jacu Bird, irei prepará-lo imediatamente começando por moer os grãos', file=discord.File('./imagens/cafe/moendo.gif'))
                await asyncio.sleep(3)
                await sala.send('Agora é só esperar a água ferver...', file=discord.File('./imagens/cafe/agua.gif'))
                await asyncio.sleep(3)
                await sala.send('Dê uns segundinhos para florecer seu café.', file=discord.File('./imagens/cafe/florecendo.gif'))
                await asyncio.sleep(3)
                await sala.send('Certo, agora só alguns minutos e estará pronto.', file=discord.File('./imagens/cafe/coando.gif'))
                await asyncio.sleep(3)
            await sala.send('Pronto! Aproveite seu belíssimo café feito com grãos de Jacu Bird', file=discord.File('./imagens/cafe/pronto.gif'))

        if tipo == '2':
            custo = 500
            if bal < custo:
                await sala.send('Cartão negado!')
                return
            async with sala.typing():
                await asyncio.sleep(3)
                await sala.send('hmm, aprecio sua preferência por um delicioso Bravo Tenor, irei prepará-lo imediatamente começando por moer os grãos', file=discord.File('./imagens/cafe/moendo.gif'))
                await asyncio.sleep(3)
                await sala.send('Agora é só esperar a água ferver...', file=discord.File('./imagens/cafe/agua.gif'))
                await asyncio.sleep(3)
                await sala.send('Dê uns segundinhos para florecer seu café.', file=discord.File('./imagens/cafe/florecendo.gif'))
                await asyncio.sleep(3)
                await sala.send('Certo, agora só alguns minutos e estará pronto.', file=discord.File('./imagens/cafe/coando.gif'))
                await asyncio.sleep(3)
            await sala.send('Pronto! Aproveite seu café feito com grãos de Bravo Tenor', file=discord.File('./imagens/cafe/pronto.gif'))

        if tipo == '3':
            custo = 100
            if bal < custo:
                await sala.send('Este cartão está bloqueado!')
                return
            async with sala.typing():
                await asyncio.sleep(3)
                await sala.send('hmm, então você é daqueles que preferem Orfeu Clássico, I see\nMe dê um minuto já irei prepará-lo, enquanto deixarei a máquina moendo os grãos', file=discord.File('./imagens/cafe/moendo.gif'))
                await asyncio.sleep(3)
                await sala.send('Enquanto a água ganha temperatura, o que você faz aqui?', file=discord.File('./imagens/cafe/agua.gif'))
                await asyncio.sleep(3)
                await sala.send('Opa, só mais um tempinho e estará pronto.', file=discord.File('./imagens/cafe/coando.gif'))
                await asyncio.sleep(3)
            await sala.send('Pronto! Aproveite seu Orfeu Clássico', file=discord.File('./imagens/cafe/pronto.gif'))

        if tipo == '4':
            custo = 50
            if bal < custo:
                await sala.send('Você não tem nem mesmo uma notinha de 50 UCredits??')
                return
            async with sala.typing():
                await asyncio.sleep(3)
                await sala.send('hmm, eu vejo que você ainda não conheceu algo melhor que Café Brasileiro, um minuto já irei prepará-lo', file=discord.File('./imagens/cafe/agua.gif'))
                await asyncio.sleep(3)
                await sala.send('Certo, so mais uma pequena espera.', file=discord.File('./imagens/cafe/coando.gif'))
                await asyncio.sleep(3)
            await sala.send('Pronto! Aproveite seu Café Brasileiro', file=discord.File('./imagens/cafe/pronto.gif'))

        if tipo == '5':
            custo = 10
            if bal < custo:
                await sala.send('Como conseguiu ficar pobre ao ponto de não ter 10 UCredits????')
                return
            async with sala.typing():
                await asyncio.sleep(3)
                await sala.send('hm, acabou o dinheiro não foi?\nCafé Pilão, um minuto e você terá o que pediu', file=discord.File('./imagens/cafe/agua.gif'))
                await asyncio.sleep(3)
                await sala.send('Sem pressa.', file=discord.File('./imagens/cafe/coando.gif'))
                await asyncio.sleep(3)
            await sala.send('Pronto! Aproveite seu Café Pilão\nAgora VAZA!!', file=discord.File('./imagens/cafe/pronto.gif'))

        users[str(user.id)]['banco'] -= custo
        users[str(user.id)]['cafe'] += 1
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

    @banco.command(name='rank')
    async def ranking(self, interaction: discord.Interaction):

        '''Ranking dos 10 maiores acumuladores do Banco Cósmico'''

        with open('./json/bank.json', 'r', encoding="utf_8") as f:
            data = json.load(f)
        lines = sorted(data.items(), key=lambda k:getitem(k[1], 'banco'), reverse=True)

        guild = interaction.guild
        em = discord.Embed(title='Banco Cósmico', color=config.roxo,
                           description='Ranking dos 10 maiores acumuladores de UCredits')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'{guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        index = 1
        for i, v in lines:
            while index <= 10:
                x = int(str(i))
                nome = guild.get_member(x)
                banco = str(v['banco'])
                em.add_field(name=nome.display_name, value=banco)
                index += 1
                break

        await interaction.response.send_message(embed=em, ephemeral=True)


async def open_account(user):

    '''Cria a conta caso membro não possua'''

    users = await get_bank_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]['nome'] = str(user.name)
        users[str(user.id)]['banco'] = 75000
        users[str(user.id)]['cafe'] = 0

    with open('./json/bank.json', 'w') as f:
        json.dump(users, f, indent=4)
        return True


async def get_bank_data():

    '''Lê todo o arquivo json, em busca do membro'''

    with open('./json/bank.json', 'r') as f:
        users = json.load(f)
    return(users)


async def update_bank(user, change=0, mode='banco'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('./json/bank.json', 'w') as f:
        json.dump(users, f, indent=4)

    bal = users[str(user.id)][mode]
    return bal


async def setup(bot):
    await bot.add_cog(Economia(bot))
