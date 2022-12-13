import asyncio
import discord
import datetime
import pytz
import json
import config

from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from typing import Optional
from time import time

tz_brazil = pytz.timezone('America/Sao_Paulo')


class Registro(discord.ui.Modal, title='Registro de Punição'):
    warframe = discord.ui.TextInput(label='Warframe', required=False, placeholder='Nome#000')
    discord_id = discord.ui.TextInput(label='Discord', required=False, placeholder='Nome#000')
    local = discord.ui.TextInput(label='Local', placeholder='Warframe/Discord')
    punicao = discord.ui.TextInput(label='Punição', placeholder='Mutado por 300 segundos / 5 minutos')
    razao = discord.ui.TextInput(label='Razão', style=discord.TextStyle.paragraph, placeholder='Ficar floodando o chat')

    async def on_submit(self, interaction: discord.Interaction):

        guild = interaction.guild
        user = interaction.user

        dev_embed = guild.get_channel(config.embed_test_dev)
        reg = guild.get_channel(config.registro_de_punicao)
        em = discord.Embed(title='Registro de Punição',
                           color=config.roxo,
                           description=f'**Warframe:** {self.warframe}\n'
                           f'**Discord:** {self.discord_id}\n'
                           f'**Local:** {self.local}\n'
                           f'**Punição:** {self.punicao}\n'
                           f'**Razão:** {self.razao}\n')

        em.set_thumbnail(url=guild.icon)
        em.set_footer(text=f'Registrado por {user}', icon_url=user.avatar)
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        await interaction.response.send_message(f'Registro enviado', embed=em, ephemeral=True)
        await reg.send(embed=em)


class adminCommand(commands.GroupCog, name='staff'):

    def __init__(self, bot: commands.bot):
        self.bot = bot

    @app_commands.command(name='registro')
    @app_commands.checks.has_role(config.Staff)
    async def registro(self, interaction: discord.Interaction):

        ''' Cria um registro de punição '''

        guild = interaction.guild
        mod = guild.get_role(config.Moderador)
        gerente = guild.get_role(config.Gerente)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)

        if (mod not in interaction.user.roles) and (gerente not in interaction.user.roles) and (lorde not in interaction.user.roles) and (lider not in interaction.user.roles):
            await interaction.response.send_message(f'Você não possui o cargo {mod.mention}', ephemeral=True)

        else:
            await interaction.response.send_modal(Registro(timeout=None))

    @registro.error
    async def registro_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.MissingRole):
            staff = interaction.guild.get_role(config.Staff)
            await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)

    @app_commands.command(name='promoção')
    @app_commands.describe(member='Selecione um membro', role='Selecione um cargo', gerente_cargos='Cargo obrigatório caso membro se torne gerente')
    @app_commands.choices(role=[
        Choice(name='Lorde', value='lor'),
        Choice(name='Gerente', value='ger'),
        Choice(name='Moderador', value='mod'),
        Choice(name='Recrutador', value='rec'),
        Choice(name='Decorador', value='dec')
    ],
        gerente_cargos=[
        Choice(name='Gerente de Moderação', value='mod'),
        Choice(name='Gerente de Recrutamento', value='rec'),
        Choice(name='Gerente de Decorador', value='dec'),
        Choice(name='Gerente de Sorteios', value='sort'),
        Choice(name='Gerente de Marketing', value='mark'),
        Choice(name='Gerente de Eventos', value='event'),
        Choice(name='Gerente de Builds', value='build'),
        Choice(name='Gerente de Desenvolvimento', value='dev')
    ])
    @app_commands.checks.has_role(config.Staff)
    async def promote(self, interaction: discord.Interaction, member: discord.Member, role: str, gerente_cargos: Optional[str]):

        ''' Adiciona ou promove um membro a Staff '''

        guild = interaction.guild
        user = interaction.user

        alteraçoesStaff = guild.get_channel(config.alteraçoes_na_staff)
        embedTest = guild.get_channel(config.test_dev_embed)

        gerente = guild.get_role(config.Gerente)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)

        recrutador = guild.get_role(config.Recrutador)
        mod = guild.get_role(config.Moderador)
        dec = guild.get_role(config.Decorador)
        staff = guild.get_role(config.Staff)

        ger_mod = guild.get_role(config.Gerente_Moderação)
        ger_rec = guild.get_role(config.Gerente_Recrutamento)
        ger_dec = guild.get_role(config.Gerente_Decoração)
        ger_sort = guild.get_role(config.Gerente_Sorteios)
        ger_mark = guild.get_role(config.Gerente_Marketing)
        ger_event = guild.get_role(config.Gerente_Eventos)
        ger_build = guild.get_role(config.Gerente_Builds)
        ger_dev = guild.get_role(config.Gerente_Desenvolvimento)

        tan = guild.get_role(config.andromeda)
        ta = guild.get_role(config.aquila)
        tl = guild.get_role(config.lyra)
        to = guild.get_role(config.orion)

        recTan = guild.get_role(config.Recrutador_Andromeda)
        recTa = guild.get_role(config.Recrutador_Aquila)
        recTl = guild.get_role(config.Recrutador_Lyra)
        recTo = guild.get_role(config.Recrutador_Orion)

        modTan = guild.get_role(config.Moderador_Andromeda)
        modTa = guild.get_role(config.Moderador_Aquila)
        modTl = guild.get_role(config.Moderador_Lyra)
        modTo = guild.get_role(config.Moderador_Orion)

        if (gerente not in interaction.user.roles) and (lorde not in interaction.user.roles) and (lider not in interaction.user.roles):
            await interaction.response.send_message(
                f'{user.display_name}, este comando é determinado a {gerente.mention}, {lorde.mention} e {lider.mention}', ephemeral=True)

        else:
            if 'lor' in role.lower():
                if lider not in interaction.user.roles:
                    await interaction.response.send_message(
                        f'{user.display_name}, este comando é determinado a {lider.mention}', ephemeral=True)

                else:
                    cargo = lorde

            if 'ger' in role.lower():
                if (lorde not in interaction.user.roles) and (lider not in interaction.user.roles):
                    await interaction.response.send_message(
                        f'{user.display_name}, este comando é determinado a {lorde.mention} e {lider.mention}', ephemeral=True)
                    return

                else:
                    cargo = gerente

                    if 'mod' in gerente_cargos.lower():
                        await member.add_roles(ger_mod)

                    if 'rec' in gerente_cargos.lower():
                        await member.add_roles(ger_rec)

                    if 'dec' in gerente_cargos.lower():
                        await member.add_roles(ger_dec)

                    if 'dev' in gerente_cargos.lower():
                        await member.add_roles(ger_dev)

                    if 'sort' in gerente_cargos.lower():
                        await member.add_roles(ger_sort)

                    if 'mark' in gerente_cargos.lower():
                        await member.add_roles(ger_mark)

                    if 'event' in gerente_cargos.lower():
                        await member.add_roles(ger_event)

                    if 'build' in gerente_cargos.lower():
                        await member.add_roles(ger_build)

            if 'rec' in role.lower():
                cargo = recrutador

                if tan in member.roles:
                    await member.add_roles(recTan)

                if ta in member.roles:
                    await member.add_roles(recTa)

                if tl in member.roles:
                    await member.add_roles(recTl)

                if to in member.roles:
                    await member.add_roles(recTo)

            if 'mod' in role.lower():
                cargo = mod

                if tan in member.roles:
                    await member.add_roles(modTan)

                if ta in member.roles:
                    await member.add_roles(modTa)

                if tl in member.roles:
                    await member.add_roles(modTl)

                if to in member.roles:
                    await member.add_roles(modTo)

            if 'dec' in role.lower():
                cargo = dec

            promo = discord.Embed(title=f"Promovido",
                                  color=config.roxo,
                                  description=f"{member.mention} foi adicionado a {cargo.mention}")
            promo.set_footer(
                text=f'Promovido por {user}', icon_url=f'{user.avatar}')
            promo.timestamp = datetime.datetime.now(tz=tz_brazil)

            await member.add_roles(cargo)
            await member.add_roles(staff)
            await interaction.response.send_message(f'{member.mention} foi adicionado a {cargo.mention}\n'
                                                    f'Log enviado a {alteraçoesStaff.mention}', ephemeral=True)
            await alteraçoesStaff.send(embed=promo)

    @promote.error
    async def promote_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.MissingRole):
            staff = interaction.guild.get_role(config.Staff)
            await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)

    @app_commands.command(name='remoção')
    @app_commands.describe(member='Selecione um membro', role='Selecione um cargo', gerente_cargos='Cargo obrigatório caso membro seja um gerente')
    @app_commands.choices(role=[
        Choice(name='Lorde', value='lor'),
        Choice(name='Gerente', value='ger'),
        Choice(name='Moderador', value='mod'),
        Choice(name='Recrutador', value='rec'),
        Choice(name='Decorador', value='dec')
    ],
        gerente_cargos=[
        Choice(name='Gerente de Moderação', value='mod'),
        Choice(name='Gerente de Recrutamento', value='rec'),
        Choice(name='Gerente de Decorador', value='dec'),
        Choice(name='Gerente de Sorteios', value='sort'),
        Choice(name='Gerente de Marketing', value='mark'),
        Choice(name='Gerente de Eventos', value='event'),
        Choice(name='Gerente de Builds', value='build'),
        Choice(name='Gerente de Desenvolvimento', value='dev')
    ])
    @app_commands.checks.has_role(config.Staff)
    async def demote(self, interaction: discord.Interaction, member: discord.Member, role: str, gerente_cargos: Optional[str]):

        ''' Remove um membro da Staff '''

        guild = interaction.guild
        user = interaction.user

        alteraçoesStaff = guild.get_channel(config.alteraçoes_na_staff)
        embedTest = guild.get_channel(config.embed_test_dev)

        gerente = guild.get_role(config.Gerente)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)

        ger_mod = guild.get_role(config.Gerente_Moderação)
        ger_rec = guild.get_role(config.Gerente_Recrutamento)
        ger_dec = guild.get_role(config.Gerente_Decoração)
        ger_sort = guild.get_role(config.Gerente_Sorteios)
        ger_mark = guild.get_role(config.Gerente_Marketing)
        ger_event = guild.get_role(config.Gerente_Eventos)
        ger_build = guild.get_role(config.Gerente_Builds)
        ger_dev = guild.get_role(config.Gerente_Desenvolvimento)

        recrutador = guild.get_role(config.Recrutador)
        mod = guild.get_role(config.Moderador)
        dec = guild.get_role(config.Decorador)
        staff = guild.get_role(config.Staff)

        tan = guild.get_role(config.andromeda)
        ta = guild.get_role(config.aquila)
        tl = guild.get_role(config.lyra)
        to = guild.get_role(config.orion)

        recTan = guild.get_role(config.Recrutador_Andromeda)
        recTa = guild.get_role(config.Recrutador_Aquila)
        recTl = guild.get_role(config.Recrutador_Lyra)
        recTo = guild.get_role(config.Recrutador_Orion)

        modTan = guild.get_role(config.Moderador_Andromeda)
        modTa = guild.get_role(config.Moderador_Aquila)
        modTl = guild.get_role(config.Moderador_Lyra)
        modTo = guild.get_role(config.Moderador_Orion)

        if (gerente and lorde and lider) not in interaction.user.roles:
            await interaction.response.send_message(
                f'{user.display_name}, este comando é determinado a {gerente.mention}, {lorde.mention} e {lider.mention}', ephemeral=True)

        else:
            if 'lor' in role.lower():
                if lider not in interaction.user.roles:
                    await interaction.response.send_message(
                        f'{user.display_name}, este comando é determinado a {lider.mention}', ephemeral=True)

                else:
                    cargo = lorde

            if 'ger' in role.lower():
                if (lorde and lider) not in interaction.user.roles:
                    await interaction.response.send_message(
                        f'{interaction.user.display_name}, este comando é determinado a {lorde.mention} e {lider.mention}', ephemeral=True)

                else:
                    cargo = gerente

                    if 'mod' in gerente_cargos.lower():
                        await member.remove_roles(ger_mod)

                    if 'rec' in gerente_cargos.lower():
                        await member.remove_roles(ger_rec)

                    if 'dec' in gerente_cargos.lower():
                        await member.remove_roles(ger_dec)

                    if 'dev' in gerente_cargos.lower():
                        await member.remove_roles(ger_dev)

                    if 'sort' in gerente_cargos.lower():
                        await member.remove_roles(ger_sort)

                    if 'mark' in gerente_cargos.lower():
                        await member.remove_roles(ger_mark)

                    if 'event' in gerente_cargos.lower():
                        await member.remove_roles(ger_event)

                    if 'build' in gerente_cargos.lower():
                        await member.remove_roles(ger_build)

            if 'rec' in role.lower():
                cargo = recrutador

                if tan in member.roles:
                    await member.remove_roles(recTan)

                if ta in member.roles:
                    await member.remove_roles(recTa)

                if tl in member.roles:
                    await member.remove_roles(recTl)

                if to in member.roles:
                    await member.remove_roles(recTo)

            if 'mod' in role.lower():
                cargo = mod

                if tan in member.roles:
                    await member.remove_roles(modTan)

                if ta in member.roles:
                    await member.remove_roles(modTa)

                if tl in member.roles:
                    await member.remove_roles(modTl)

                if to in member.roles:
                    await member.remove_roles(modTo)

            if 'dec' in role.lower():
                cargo = dec

            promo = discord.Embed(title=f'Demote',
                                  color=config.roxo,
                                  description=f'{member.mention} foi removido de {cargo.mention}')
            promo.set_footer(
                text=f'Removido por {interaction.user}', icon_url=f'{interaction.user.avatar}')
            promo.timestamp = datetime.datetime.now(tz=tz_brazil)

            await member.remove_roles(cargo)
            await member.remove_roles(staff)

            await interaction.response.send_message(f'{member.mention} foi removido de {cargo.mention}\n'
                                                    f'Log enviado a {alteraçoesStaff.mention}', ephemeral=True)
            await alteraçoesStaff.send(embed=promo)

    @demote.error
    async def demote_error(self, interaction: discord.Interaction, err: app_commands.errors.MissingRole):
        staf = interaction.guild.get_role(config.Staff)
        await interaction.response.send_message(f'Você não é um {staf.mention}', ephemeral=True)

    @app_commands.command(name='recrutar')
    @app_commands.describe(member='Selecione um membro', role='Selecione um dos 4 clãs')
    @app_commands.choices(role=[
        Choice(name='Os Tenno de Andromeda', value='Andromda'),
        Choice(name='Os Tenno de Aquila', value='Aquila'),
        Choice(name='Os Tenno de Lyra', value='Lyra'),
        Choice(name='Os Tenno de Orion', value='Orion')
    ])
    @app_commands.checks.has_role(config.Staff)
    async def recrutar(self, interaction: discord.Interaction, member: discord.Member, role: str):

        ''' Recruta um membro '''

        timer = 15

        guild = interaction.guild

        membro = guild.get_role(config.membro)
        participar = guild.get_role(config.participar)

        tan = guild.get_role(config.andromeda)
        ta = guild.get_role(config.aquila)
        tl = guild.get_role(config.lyra)
        to = guild.get_role(config.orion)

        if 'andromeda' == role.lower():
            cargo = tan

        if 'aquila' == role.lower():
            cargo = ta

        if 'lyra' == role.lower():
            cargo = tl

        if 'orion' == role.lower():
            cargo = to

        recrutar = discord.Embed(title='Recrutar',
                                 color=config.roxo,
                                 description=f'{member.mention} foi adicionado a {cargo.mention}\n'
                                 f'{participar.mention} será removido em <t:{int(f"{time():.0f}") + timer}:R>\n\n')

        recrutar.set_thumbnail(url=interaction.guild.icon)
        recrutar.set_footer(text=f'Recrutado por {interaction.user}', icon_url=f'{interaction.user.avatar}')
        recrutar.timestamp = datetime.datetime.now(tz=tz_brazil)

        await member.add_roles(membro)
        await member.add_roles(cargo)
        await interaction.response.send_message(embed=recrutar)
        await asyncio.sleep(timer)
        await member.remove_roles(participar)

    @recrutar.error
    async def recrutar_error(self, interaction: discord.Interaction, err: app_commands.errors.MissingRole):
        staff = interaction.guild.get_role(config.Staff)
        await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)

    @app_commands.command(name='adicionar')
    @app_commands.checks.has_role(config.Staff)
    @app_commands.describe(membro='Selecione um membro', valor='Informe a quantia, deve ser numeros inteiros')
    async def adicionar(self, interaction: discord.Interaction, membro: discord.Member, valor: int):

        '''Líderes e Lordes podem enviar UCredits a membro'''

        user = interaction.user
        guild = interaction.guild

        mecanico = guild.get_role(config.mecanico)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)

        await open_account(membro)
        users = await get_bank_data()

        if (lorde not in user.roles) and (lider not in user.roles) and (mecanico not in user.roles):
            await interaction.response.send_message(f'{user.display_name}, este comando é determinado a {lorde.mention} e {lider.mention}')
            return

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas no <#{config.comandos_staff}>', ephemeral=True)
            return

        if valor < 0:
            await interaction.response.send_message('O valor de UCredits deve ser maior que `0`', ephemeral=True)
            return

        em = discord.Embed(title=f'Admin UCredits',
                           color=config.roxo,
                           description=f'{user.display_name} enviou `{valor}` UCredits para {membro.mention}')
        em.set_thumbnail(
            url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(
            text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await interaction.response.send_message(embed=em)

        users[str(membro.id)]['banco'] += valor
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

    @adicionar.error
    async def adicionar_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.MissingRole):
            staff = interaction.guild.get_role(config.Staff)
            await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)

    @app_commands.command(name='remover')
    @app_commands.checks.has_role(config.Staff)
    @app_commands.describe(membro='Selecione um membro', valor='Informe a quantia, deve ser numeros inteiros')
    async def remover(self, interaction: discord.Interaction, membro: discord.Member, valor: int):

        '''Líderes e Lordes podem remover UCredits de membro'''

        user = interaction.user
        guild = interaction.guild

        mecanico = guild.get_role(config.mecanico)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)

        await open_account(membro)
        users = await get_bank_data()

        if (lorde not in user.roles) and (lider not in user.roles) and (mecanico not in user.roles):
            await interaction.response.send_message(f'{user.display_name}, este comando é determinado a {lorde.mention} e {lider.mention}')
            return

        if (interaction.channel.id != config.loja_comandos) and (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas no <#{config.comandos_staff}>', ephemeral=True)
            return

        if valor < 0:
            await interaction.response.send_message('O valor de UCredits deve ser maior que `0`', ephemeral=True)
            return

        em = discord.Embed(title=f'Admin UCredits',
                           color=config.roxo,
                           description=f'{user.display_name} retirou `{valor}` UCredits de {membro.mention}')
        em.set_thumbnail(
            url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)
        await interaction.response.send_message(embed=em)

        users[str(membro.id)]['banco'] -= valor
        with open('./json/bank.json', 'w') as f:
            json.dump(users, f, indent=4)

    @remover.error
    async def remover_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.MissingRole):
            staff = interaction.guild.get_role(config.Staff)
            await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)

    @app_commands.command(name='cargo')
    @app_commands.checks.has_role(config.Staff)
    @app_commands.describe(membro='Selecione um membro', cargo_add='Informe o cargo que deve ser adicionado', cargo_rem='Informe o cargo que deve ser removido')
    async def cargo(self, interaction: discord.Interaction, membro: discord.Member, cargo_add: discord.Role, cargo_rem: Optional[discord.Role]):

        '''Lordes e Líderes podem adicionar cargo personalizado a membro'''

        guild = interaction.guild
        user = interaction.user

        mecanico = guild.get_role(config.mecanico)
        lorde = guild.get_role(config.Lorde)
        lider = guild.get_role(config.Lider)
        nome = str(cargo_add.name)
        cor = str(cargo_add.color)
        criado = str(cargo_add.created_at)

        if (lorde not in user.roles) and (lider not in user.roles) and (mecanico not in user.roles):
            await interaction.response.send_message(f'{user.display_name}, este comando é determinado a {lorde.mention} e {lider.mention}', ephemeral=True)
            return

        if (interaction.channel.id != config.comandos_staff) and (interaction.channel.id != config.teste_dev):
            await interaction.response.send_message(f'apenas no <#{config.comandos_staff}>', ephemeral=True)
            return

        if user.top_role.position < cargo_add.position:
            await interaction.response.send_message(f'O cargo {cargo_add.mention} está acima do seu cargo {user.top_role.mention}', ephemeral=True)
            return

        em = discord.Embed(title=f'Criação de cargo personalizado',
                           color=config.roxo,
                           description=f'Olá {membro.mention}!\nSeu cargo personalizado em **{guild}** foi criado e adicionado a você.\n\n'
                                       f'Nome: {nome} \nCor: {cor}\nCriado em: {criado}')

        em.set_thumbnail(
            url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        em1 = discord.Embed(title=f'Criação de cargo personalizado',
                            color=config.roxo,
                            description=f'{user.mention}, {membro.mention} foi notificado e adicionado a {cargo_add.mention}.\n\n'
                            f'Nome: {nome}\nCor: {cor}\nCriado em: {criado}')

        em1.set_thumbnail(
            url='https://cdn.discordapp.com/emojis/629264485273698325.webp')
        em1.set_footer(text=f'Registrado em {guild}', icon_url=f'{guild.icon}')
        em.timestamp = datetime.datetime.now(tz=tz_brazil)

        await membro.add_roles(cargo_add)
        if cargo_rem != None:
            await membro.remove_roles(cargo_rem)
        await interaction.response.send_message(embed=em1)
        await membro.send(embed=em)

    @cargo.error
    async def cargo_error(self, interaction: discord.Interaction, err):
        if isinstance(err, app_commands.MissingRole):
            staff = interaction.guild.get_role(config.Staff)
            await interaction.response.send_message(f'Você não é um {staff.mention}', ephemeral=True)


async def open_account(user):

    '''Cria a conta caso membro não possua'''

    users = await get_bank_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)] = {}
        users[str(user.id)]['nome'] = str(user.name)
        users[str(user.id)]['banco'] = 0
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
    await bot.add_cog(adminCommand(bot))
