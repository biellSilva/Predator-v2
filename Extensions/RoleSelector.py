import discord
import asyncio
import pytz
import config

from datetime import datetime
from discord.ext import commands


tz_brazil = pytz.timezone('America/Sao_Paulo')


class AlertaView(discord.ui.View):
    @discord.ui.select(
        custom_id='Alertas_selector',
        min_values=0,
        max_values=12,
        placeholder='Selecione seus pings de alertas',
        options=[
            discord.SelectOption(
                label='Ajudante',
                value='ajudante',
                emoji='🆘',
                description='Será pingado ao precisarem de Ajudantes'),
            
            discord.SelectOption(
                label='Reator',
                value='reator',
                emoji=':reator:844951875791093760',
                description='Será pingado em alertas com Reatores'),

            discord.SelectOption(
                label='Catalisador',
                value='catalisador',
                emoji=':catalisador:844951875371401247',
                description='Será pingado em alertas com Catalisadores'),

            discord.SelectOption(
                label='Baro Ki\'Teer',
                value='baro',
                emoji=':BaroBitchPlease:716035316464615455',
                description='Será pingado com a chegada do Baro Ki\'Teer'),

            discord.SelectOption(
                label='Forma',
                value='forma',
                emoji=':Forma:821407092698906656',
                description='Será pingado em alertas com Formas'),

            discord.SelectOption(
                label='Forma Umbra',
                value='umbra',
                emoji=':FormaUmbraiss:679970463153258512',
                description='Será pingado em alertas com Formas Umbra'),

            discord.SelectOption(
                label='Lotus Cósmica',
                value='lotus',
                emoji=':LotusCosmica:835281000694284349',
                description='Será pingado na Lotus Cósmica'),

            discord.SelectOption(
                label='Grão Mestre Ping',
                value='mestre',
                description='Pingado quando um Grão Mestre for usar sua benção'),

            discord.SelectOption(
                label='Sorteios',
                value='sorteio',
                emoji='🎉',
                description='Será pingado quando houver Sorteios'),

            discord.SelectOption(
                label='Eventos Externos',
                value='evento',
                emoji='🎊',
                description='Será pingado quando houver Eventos Externos'),
            
            discord.SelectOption(
                label='Drops Externos',
                value='drops',
                emoji='🎁',
                description='Será pingado quando houver Drops Externos'),

            discord.SelectOption(
                label='Atualizações',
                value='update',
                emoji='🔔',
                description='Será pingado quando houver Atualizações do Warframe')
        ])

    async def callback(self, interaction: discord.Interaction, select: discord.ui.select):
        guild = interaction.guild
        member = interaction.user

        await interaction.response.defer(ephemeral=True, thinking=True)

        ajudante = guild.get_role(config.ajudante)
        reator = guild.get_role(config.reator)
        catalisador = guild.get_role(config.catalisador)
        baro = guild.get_role(config.baro)
        forma = guild.get_role(config.forma)
        forma_umbra = guild.get_role(config.forma_umbra)
        lotus = guild.get_role(config.lotus)
        mestre = guild.get_role(config.mestre)
        sorteio = guild.get_role(config.sorteio)
        evento = guild.get_role(config.eventoExt)
        drop = guild.get_role(config.dropExt)
        update = guild.get_role(config.update)

        add = '\n**Adicionado:**'
        mantem = '\n**Mantido:**'
        removido = '\n**Removido:**'

        if 'ajudante' in select.values:
            if ajudante not in member.roles:
                await member.add_roles(ajudante)
                add += f'\n*+ {ajudante.mention}*'
            else:
                mantem += f'\n*~ {ajudante.mention}*'
        else:
            await member.remove_roles(ajudante)
            removido += f'\n*- {ajudante.mention}*'


        if 'reator' in select.values:
            if reator not in member.roles:
                await member.add_roles(reator)
                add += f'\n*+ {reator.mention}*'
            else:
                mantem += f'\n*~ {reator.mention}*'
        else:
            await member.remove_roles(reator)
            removido += f'\n*- {reator.mention}*'


        if 'catalisador' in select.values:
            if catalisador not in member.roles:
                await member.add_roles(catalisador)
                add += f'\n*+ {catalisador.mention}*'
            else:
                mantem += f'\n*~ {catalisador.mention}*'
        else:
            await member.remove_roles(catalisador)
            removido += f'\n*- {catalisador.mention}*'


        if 'baro' in select.values:
            if baro not in member.roles:
                await member.add_roles(baro)
                add += f'\n*+ {baro.mention}*'
            else:
                mantem += f'\n*~ {baro.mention}*'
        else:
            await member.remove_roles(baro)
            removido += f'\n*- {baro.mention}*'


        if 'forma' in select.values:
            if forma not in member.roles:
                await member.add_roles(forma)
                add += f'\n*+ {forma.mention}*'
            else:
                mantem += f'\n*~ {forma.mention}*'
        else:
            await member.remove_roles(forma)
            removido += f'\n*- {forma.mention}*'


        if 'umbra' in select.values:
            if forma_umbra not in member.roles:
                await member.add_roles(forma_umbra)
                add += f'\n*+ {forma_umbra.mention}*'
            else:
                mantem += f'\n*~ {forma_umbra.mention}*'
        else:
            await member.remove_roles(forma_umbra)
            removido += f'\n*- {forma_umbra.mention}*'


        if 'lotus' in select.values:
            if lotus not in member.roles:
                await member.add_roles(lotus)
                add += f'\n*+ {lotus.mention}*'
            else:
                mantem += f'\n*~ {lotus.mention}*'
        else:
            await member.remove_roles(lotus)
            removido += f'\n*- {lotus.mention}*'

        
        if 'mestre' in select.values:
            if mestre not in member.roles:
                await member.add_roles(mestre)
                add += f'\n*+ {mestre.mention}*'
            else:
                mantem += f'\n*~ {mestre.mention}*'
        else:
            await member.remove_roles(mestre)
            removido += f'\n*- {mestre.mention}*'


        if 'sorteio' in select.values:
            if sorteio not in member.roles:
                await member.add_roles(sorteio)
                add += f'\n*+ {sorteio.mention}*'
            else:
                mantem += f'\n*~ {sorteio.mention}*'
        else:
            await member.remove_roles(sorteio)
            removido += f'\n*- {sorteio.mention}*'


        if 'evento' in select.values:
            if evento not in member.roles:
                await member.add_roles(evento)
                add += f'\n*+ {evento.mention}*'
            else:
                mantem += f'\n*~ {evento.mention}*'
        else:
            await member.remove_roles()

        if 'drops' in select.values:
            if drop not in member.roles:
                await member.add_roles(drop)
                add += f'\n*+ {drop.mention}*'
            else:
                mantem += f'\n*~ {drop.mention}*'

        if 'update' in select.values:
            if update not in member.roles:
                await member.add_roles(update)
                add += f'\n*+ {update.mention}*'
            else:
                mantem += f'\n*~ {update.mention}*'


        await interaction.edit_original_response(content=f'{"" if len(mantem)<14 else mantem} {"" if len(add)<17 else add} {"" if len(removido)<17 else removido}')
        

class SquadView(discord.ui.View):
    @discord.ui.select(
        custom_id='Squad_selector',
        min_values=0,
        max_values=18,
        placeholder='Selecione seus pings de esquadrão',
        options=[
            discord.SelectOption(
                label='Eidolon',
                value='eidolon',
                emoji=':ostron:664486884868882487',
                description='Ping para caçar Eidolon'),

            discord.SelectOption(
                label='Beneficiária',
                value='profit',
                description='Ping para caçar a Beneficiária'),

            discord.SelectOption(
                label='Deriva de Cambion',
                value='deimos',
                description='Ping para a Deriva de Cambion'),

            discord.SelectOption(
                label='Zariman',
                value='anjos',
                description='Ping para farm na Zariman'),

            discord.SelectOption(
                label='Relíquias ',
                value='relic',
                emoji=':reliquia:664486282046472202',
                description='Ping para as Relíquias '),

            discord.SelectOption(
                label='Caminho do Aço',
                value='steel',
                description='Ping para o Caminho do Aço'),

            discord.SelectOption(
                label='Index',
                value='index',
                emoji=':Creditos:596817907984498718',
                description='Ping para farm de Créditos'),

            discord.SelectOption(
                label='Recursos',
                value='recurso',
                emoji=':recurso:664484737951334401',
                description='Ping para farm de Recursos'),
            
            discord.SelectOption(
                label='Arbitragem',
                value='arbitros',
                emoji=':arbiters:664487282635571213',
                description='Ping para a Arbitragem'),

            discord.SelectOption(
                label='Experiencia',
                value='xp',
                emoji=':afinidade:664488114437357574',
                description='Ping para farm de Xp'),

            discord.SelectOption(
                label='Railjack',
                value='railjack',
                emoji=':CephalonCy:664487929724272660',
                description='Ping para a Railjack'),

            discord.SelectOption(
                label='Massacre do Santuário',
                value='santuario',
                description='Ping para o Massacre do Santuário'),

            discord.SelectOption(
                label='Kuva Liches',
                value='lich',
                emoji=':ReliquiaRequiem:687005668325982238',
                description='Ping para caçar Kuva Lich'),
            
            discord.SelectOption(
                label='Irmãs de Parvos',
                value='sisters',
                description='Ping para caçar Corpus Lich'),

            discord.SelectOption(
                label='Kuva',
                value='kuva',
                emoji=':Kuva:689906601619882020',
                description='Ping para farm de Kuva'),

            discord.SelectOption(
                label='Praga Estelar',
                value='praga',
                emoji=':Forma:821407092698906656',
                description='Ping para a Praga Estelar'),

            discord.SelectOption(
                label='Novato',
                value='novato',
                description='Ping para farm de Kuva'),

            discord.SelectOption(
                label='Caçada de Arconte',
                value='archon',
                emoji='🐍',
                description='Ping para a Caçada de Arconte')])
                
    async def callback(self, interaction: discord.Interaction, select: discord.ui.select):
        member = interaction.user
        guild = interaction.guild

        #print(member, select.labels)

        await interaction.response.defer(ephemeral=True, thinking=True)

        eidolon = guild.get_role(config.eidolon)
        profit = guild.get_role(config.profit)
        relic = guild.get_role(config.relic)
        steel = guild.get_role(config.steel)
        index = guild.get_role(config.index)
        recurso = guild.get_role(config.recurso)
        arbitros = guild.get_role(config.arbitros)
        xp = guild.get_role(config.xp)
        railjack = guild.get_role(config.railjack)
        deimos = guild.get_role(config.deimos)
        santuario = guild.get_role(config.santuario)
        lich = guild.get_role(config.kuvalich)
        sisters = guild.get_role(config.corpuslich)
        kuva = guild.get_role(config.kuva)
        anjos = guild.get_role(config.anjos)
        praga = guild.get_role(config.praga)
        novato = guild.get_role(config.novato)
        archon = guild.get_role(config.archon)

        add = '\n**Adicionado:**'
        mantem = '\n**Mantido:**'
        removido = '\n**Removido:**'

        if 'eidolon' in select.values:
            if eidolon not in member.roles:
                await member.add_roles(eidolon)
                add += f'\n*+ {eidolon.mention}*'
            else:
                mantem += f'\n*~ {eidolon.mention}*'

        if 'profit' in select.values:
            if profit not in member.roles:
                await member.add_roles(profit)
                add += f'\n*+ {profit.mention}*'
            else:
                mantem += f'\n*~ {profit.mention}*'

        if 'relic' in select.values:
            if relic not in member.roles:
                await member.add_roles(relic)
                add += f'\n*+ {relic.mention}*'
            else:
                mantem += f'\n*~ {relic.mention}*'

        if 'steel' in select.values:
            if steel not in member.roles:
                await member.add_roles(steel)
                add += f'\n*+ {steel.mention}*'
            else:
                mantem += f'\n*~ {steel.mention}*'

        if 'index' in select.values:
            if index not in member.roles:
                await member.add_roles(index)
                add += f'\n*+ {index.mention}*'
            else:
                mantem += f'\n*~ {index.mention}*'

        if 'recurso' in select.values:
            if recurso not in member.roles:
                await member.add_roles(recurso)
                add += f'\n*+ {recurso.mention}*'
            else:
                mantem += f'\n*~ {recurso.mention}*'

        if 'arbitros' in select.values:
            if arbitros not in member.roles:
                await member.add_roles(arbitros)
                add += f'\n*+ {arbitros.mention}*'
            else:
                mantem += f'\n*~ {arbitros.mention}*'

        if 'xp' in select.values:
            if xp not in member.roles:
                await member.add_roles(xp)
                add += f'\n*+ {xp.mention}*'
            else:
                mantem += f'\n*~ {xp.mention}*'

        if 'railjack' in select.values:
            if railjack not in member.roles:
                await member.add_roles(railjack)
                add += f'\n*+ {railjack.mention}*'
            else:
                mantem += f'\n*~ {railjack.mention}*'

        if 'deimos' in select.values:
            if deimos not in member.roles:
                await member.add_roles(deimos)
                add += f'\n*+ {deimos.mention}*'
            else:
                mantem += f'\n*~ {deimos.mention}*'

        if 'santuario' in select.values:
            if santuario not in member.roles:
                await member.add_roles(santuario)
                add += f'\n*+ {santuario.mention}*'
            else:
                mantem += f'\n*~ {santuario.mention}*'

        if 'lich' in select.values:
            if lich not in member.roles:
                await member.add_roles(lich)
                add += f'\n*+ {lich.mention}*'
            else:
                mantem += f'\n*~ {lich.mention}*'

        if 'sisters' in select.values:
            if sisters not in member.roles:
                await member.add_roles(sisters)
                add += f'\n*+ {sisters.mention}*'
            else:
                mantem += f'\n*~ {sisters.mention}*'

        if 'kuva' in select.values:
            if kuva not in member.roles:
                await member.add_roles(kuva)
                add += f'\n*+ {kuva.mention}*'
            else:
                mantem += f'\n*~ {kuva.mention}*'

        if 'anjos' in select.values:
            if anjos not in member.roles:
                await member.add_roles(anjos)
                add += f'\n*+ {anjos.mention}*'
            else:
                mantem += f'\n*~ {anjos.mention}*'

        if 'praga' in select.values:
            if praga not in member.roles:
                await member.add_roles(praga)
                add += f'\n*+ {praga.mention}*'
            else:
                mantem += f'\n*~ {praga.mention}*'

        if 'novato' in select.values:
            if novato not in member.roles:
                await member.add_roles(novato)
                add += f'\n*+ {novato.mention}*'
            else:
                mantem += f'\n*~ {novato.mention}*'

        if 'archon' in select.values:
            if archon not in member.roles:
                await member.add_roles(archon)
                add += f'\n*+ {archon.mention}*'
            else:
                mantem += f'\n*~ {archon.mention}*'

                            #########################################
                            #########################################
                            #########################################

        if 'eidolon' not in select.values:
            if eidolon  in member.roles:
                await member.remove_roles(eidolon)
                removido += f'\n*- {eidolon.mention}*'

        if 'profit' not in select.values:
            if profit  in member.roles:
                await member.remove_roles(profit)
                removido += f'\n*- {profit.mention}*'

        if 'relic' not in select.values:
            if relic  in member.roles:
                await member.remove_roles(relic)
                removido += f'\n*- {relic.mention}*'

        if 'steel' not in select.values:
            if steel  in member.roles:
                await member.remove_roles(steel)
                removido += f'\n*- {steel.mention}*'

        if 'index' not in select.values:
            if index  in member.roles:
                await member.remove_roles(index)
                removido += f'\n*- {index.mention}*'

        if 'recurso' not in select.values:
            if recurso  in member.roles:
                await member.remove_roles(recurso)
                removido += f'\n*- {recurso.mention}*'

        if 'arbitros' not in select.values:
            if arbitros  in member.roles:
                await member.remove_roles(arbitros)
                removido += f'\n*- {arbitros.mention}*'

        if 'xp' not in select.values:
            if xp  in member.roles:
                await member.remove_roles(xp)
                removido += f'\n*- {xp.mention}*'

        if 'railjack' not in select.values:
            if railjack  in member.roles:
                await member.remove_roles(railjack)
                removido += f'\n*- {railjack.mention}*'

        if 'deimos' not in select.values:
            if deimos  in member.roles:
                await member.remove_roles(deimos)
                removido += f'\n*- {deimos.mention}*'

        if 'santuario' not in select.values:
            if santuario  in member.roles:
                await member.remove_roles(santuario)
                removido += f'\n*- {santuario.mention}*'

        if 'lich' not in select.values:
            if lich  in member.roles:
                await member.remove_roles(lich)
                removido += f'\n*- {lich.mention}*'

        if 'sisters' not in select.values:
            if sisters  in member.roles:
                await member.remove_roles(sisters)
                removido += f'\n*- {sisters.mention}*'

        if 'kuva' not in select.values:
            if kuva  in member.roles:
                await member.remove_roles(kuva)
                removido += f'\n*- {kuva.mention}*'

        if 'anjos' not in select.values:
            if anjos  in member.roles:
                await member.remove_roles(anjos)
                removido += f'\n*- {anjos.mention}*'

        if 'praga' not in select.values:
            if praga  in member.roles:
                await member.remove_roles(praga)
                removido += f'\n*- {praga.mention}*'

        if 'novato' not in select.values:
            if novato  in member.roles:
                await member.remove_roles(novato)
                removido += f'\n*- {novato.mention}*'

        if 'archon' not in select.values:
            if archon  in member.roles:
                await member.remove_roles(archon)
                removido += f'\n*- {archon.mention}*'

        await interaction.edit_original_response(content=f'{"" if len(mantem)<14 else mantem} {"" if len(add)<17 else add} {"" if len(removido)<17 else removido}')


class DiarioView(discord.ui.View):
    @discord.ui.select(
        custom_id='diario_selector',
        min_values=0,
        max_values=6,
        placeholder='Selecione seus pings diarios',
        options=[
            discord.SelectOption(
                label='Cetus Dia',
                value='dia',
                emoji='☀️',
                description='Ping quando amanhecer em Cetus'),

            discord.SelectOption(
                label='Cetus Noite',
                value='noite',
                emoji='🌑',
                description='Ping quando anoitecer em Cetus'),

            discord.SelectOption(
                label='Deimos Vome',
                value='vome',
                emoji='🔵',
                description='Ping quando Vome reina no Necralisk'),

            discord.SelectOption(
                label='Deimos Fass',
                value='fass',
                emoji='🔴',
                description='Ping quando Fass reina no Necralisk'),

            discord.SelectOption(
                label='Fortuna Frio',
                value='frio',
                emoji='❄️',
                description='Ping quando Fortuna se torna Fria'),

            discord.SelectOption(
                label='Fortuna Morno',
                value='morno',
                emoji='🔥',
                description='Ping quando Fortuna se torna Morna'),
        ])
    
    async def callback(self, interaction: discord.Interaction, select: discord.ui.select):
        member = interaction.user
        guild = interaction.guild

        #print(member, select.labels)

        await interaction.response.defer(ephemeral=True, thinking=True)
        
        dia = guild.get_role(config.dia)
        noite = guild.get_role(config.noite)
        vome = guild.get_role(config.vome)
        fass = guild.get_role(config.fass)
        frio = guild.get_role(config.frio)
        morno = guild.get_role(config.morno)

        add = '\n**Adicionado:**'
        mantem = '\n**Mantido:**'
        removido = '\n**Removido:**'

        if 'dia' in select.values:
            if dia not in member.roles:
                await member.add_roles(dia)
                add += f'\n*+ {dia.mention}*'
            else:
                mantem += f'\n*~ {dia.mention}*'
        
        if 'noite' in select.values:
            if noite not in member.roles:
                await member.add_roles(noite)
                add += f'\n*+ {noite.mention}*'
            else:
                mantem += f'\n*~ {noite.mention}*'

        if 'vome' in select.values:
            if vome not in member.roles:
                await member.add_roles(vome)
                add += f'\n*+ {vome.mention}*'
            else:
                mantem += f'\n*~ {vome.mention}*'
        
        if 'fass' in select.values:
            if fass not in member.roles:
                await member.add_roles(fass)
                add += f'\n*+ {fass.mention}*'
            else:
                mantem += f'\n*~ {fass.mention}*'
        
        if 'frio' in select.values:
            if frio not in member.roles:
                await member.add_roles(frio)
                add += f'\n*+ {frio.mention}*'
            else:
                mantem += f'\n*~ {frio.mention}*'

        if 'morno' in select.values:
            if morno not in member.roles:
                await member.add_roles(morno)
                add += f'\n*+ {morno.mention}*'
            else:
                mantem += f'\n*~ {morno.mention}*'

        if 'dia' not in select.values:
            if dia in member.roles:
                await member.remove_roles(dia)
                removido += f'\n*- {dia.mention}*'

        if 'noite' not in select.values:
            if noite in member.roles:
                await member.remove_roles(noite)
                removido += f'\n*- {noite.mention}*'

        if 'vome' not in select.values:
            if vome in member.roles:
                await member.remove_roles(vome)
                removido += f'\n*- {vome.mention}*'

        if 'fass' not in select.values:
            if fass in member.roles:
                await member.remove_roles(fass)
                removido += f'\n*- {fass.mention}*'

        if 'frio' not in select.values:
            if frio in member.roles:
                await member.remove_roles(frio)
                removido += f'\n*- {frio.mention}*'

        if 'morno' not in select.values:
            if morno in member.roles:
                await member.remove_roles(morno)
                removido += f'\n*- {morno.mention}*'

        await interaction.edit_original_response(content=f'{"" if len(mantem)<14 else mantem} {"" if len(add)<17 else add} {"" if len(removido)<17 else removido}')


class PlataformaView(discord.ui.View):
    @discord.ui.select(
        custom_id='plataforma_selector',
        min_values=0,
        max_values=3,
        placeholder='Selecione sua plataforma',
        options=[
            discord.SelectOption(
                label='Pc',
                value='pc',
                emoji='💻',
                description='Joga pelo Pc/Notebook'),

            discord.SelectOption(
                label='Console',
                value='console',
                emoji='🎮',
                description='Joga pelo Console'),

            discord.SelectOption(
                label='Mobile',
                value='mobile',
                emoji='📱',
                description='Joga pelo Mobile')])

    async def callback(self, interaction: discord.Interaction, select: discord.ui.select):
        guild = interaction.guild
        member = interaction.user

        #print(member, select)

        await interaction.response.defer(ephemeral=True, thinking=True)

        pc = guild.get_role(config.pc)
        console = guild.get_role(config.console)
        mobile = guild.get_role(config.mobile)

        add = '\n**Adicionado:**'
        mantem = '\n**Mantido:**'
        removido = '\n**Removido:**'

        if 'pc' in select.values:
            if pc not in member.roles:
                await member.add_roles(pc)
                add += f'\n*+ {pc.mention}*'
            else:
                mantem += f'\n*~ {pc.mention}*'

        if 'console' in select.values:
            if console not in member.roles:
                await member.add_roles(console)
                add += f'\n*+ {console.mention}*'
            else:
                mantem += f'\n*~ {console.mention}*'

        if 'mobile' in select.values:
            if mobile not in member.roles:
                await member.add_roles(mobile)
                add += f'\n*+ {mobile.mention}*'
            else:
                mantem += f'\n*~ {mobile.mention}*'

        if 'pc' not in select.values:
            if pc in member.roles:
                await member.remove_roles(pc)
                removido += f'\n*- {pc.mention}*'

        if 'console' not in select.values:
            if console in member.roles:
                await member.remove_roles(console)
                removido += f'\n*- {console.mention}*'

        if 'mobile' not in select.values:
            if mobile in member.roles:
                await member.remove_roles(mobile)
                removido += f'\n*- {mobile.mention}*'

        await interaction.edit_original_response(content=f'{"" if len(mantem)<14 else mantem} {"" if len(add)<17 else add} {"" if len(removido)<17 else removido}')


class MemberView(discord.ui.View):
    @discord.ui.select(
        custom_id='member_selector',
        max_values=1,
        placeholder='Selecione 1 cargo',
        options=[
            discord.SelectOption(
                label='Os Tenno de Andromeda',
                value='tan',
                emoji=':Andromeda:615250826474291211',
                description='Membro do Andromeda'),

            discord.SelectOption(
                label='Os Tenno de Aquila',
                value='ta',
                emoji=':Aquila:615250826289741834',
                description='Membro do Aquila'),
            
            discord.SelectOption(
                label='Os Tenno de Lyra',
                value='tl',
                emoji=':Lyra:615250826260381735',
                description='Membro do Lyra'),

            discord.SelectOption(
                label='Os Tenno de Orion',
                value='to',
                emoji=':Orion:615250826872619196',
                description='Membro do Orion'),
            
            discord.SelectOption(
                label='Visitante',
                value='visit',
                emoji='👥',
                description='Visitando a Aliança'),

            discord.SelectOption(
                label='Quero Participar',
                value='parti',
                emoji='🤝',
                description='Deseja participar da Aliança')])

    async def callback(self, interaction: discord.Interaction, select: discord.ui.select):
        guild = interaction.guild
        member = interaction.user

        #print(member, select.labels)

        await interaction.response.defer(ephemeral=True, thinking=True)

        tan = guild.get_role(config.andromeda)
        ta = guild.get_role(config.aquila)
        tl = guild.get_role(config.lyra)
        to = guild.get_role(config.orion)

        visitante = guild.get_role(config.visitante)
        participar = guild.get_role(config.participar)
        membro = guild.get_role(config.membro)

        recrutador = guild.get_role(config.Recrutador)

        channelRec = guild.get_channel(config.recrutamento)

        add = '\n**Adicionado:**'
        removido = '\n**Removido:**'
        mantem = '\n**Mantido:**'

        if "tan" in select.values:
            if tan not in member.roles:
                await member.add_roles(tan)
                await member.add_roles(membro)
                add += f'\n*+ {tan.mention}*'
            else:
                mantem += f'\n~ {tan.mention}'

        if "ta" in select.values:
            if ta not in member.roles:
                await member.add_roles(ta)
                await member.add_roles(membro)
                add += f'\n*+ {ta.mention}*'
            else:
                mantem += f'\n~ {ta.mention}'

        if "tl" in select.values:
            if tl not in member.roles:
                await member.add_roles(tl)
                await member.add_roles(membro)
                add += f'\n*+ {tl.mention}*'
            else:
                mantem += f'\n~ {tl.mention}'

        if "to" in select.values:
            if to not in member.roles:
                await member.add_roles(to)
                await member.add_roles(membro)
                add += f'\n*+ {to.mention}*'
            else:
                mantem += f'\n~ {to.mention}'

        if "visit" in select.values:
            if visitante not in member.roles:
                await member.remove_roles(membro)
                await member.add_roles(visitante)
                add += f'\n*+ {visitante.mention}*'
            else:
                mantem += f'\n~ {visitante.mention}'

        if "parti" in select.values:
            if participar not in member.roles:
                await member.remove_roles(membro)
                await member.add_roles(participar)
                add += f'\n*+ {participar.mention}*'

                embedRec = discord.Embed(title="Recrutamento",
                                            color=config.roxo,
                                            description=f"Olá {member.mention}! Para um atendimento rapido nos informe seu nick no Warframe e um dos clãs abaixo para notificarmos um recrutador\n"
                                            f"<:Andromeda:615250826474291211> - {tan.mention}\n"
                                            f"<:Aquila:615250826289741834> - {ta.mention}\n"
                                            f"<:Lyra:615250826260381735> - {tl.mention}\n"
                                            f"<:Orion:615250826872619196> - {to.mention}\n\n"
                                            f"||{member} - {member.id}||")
                embedRec.timestamp = datetime.now(tz=tz_brazil)
                embedRec.set_footer(text=f"Bem vindo a {guild}")
                embedRec.set_thumbnail(url=member.avatar.url)

                await asyncio.sleep(1)
                await channelRec.send(f"{member.mention} {recrutador.mention}")
                await channelRec.send(embed=embedRec)
            else:
                mantem += f'\n~ {participar.mention}'

        
        if "tan" not in select.values:
            if tan in member.roles:
                await member.remove_roles(tan)
                removido += f'\n*- {tan.mention}*'

        if "ta" not in select.values:
            if ta in member.roles:
                await member.remove_roles(ta)
                removido += f'\n*- {ta.mention}*'

        if "tl" not in select.values:
            if tl in member.roles:
                await member.remove_roles(tl)
                removido += f'\n*- {tl.mention}*'

        if "to" not in select.values:
            if to in member.roles:
                await member.remove_roles(to)
                removido += f'\n*- {to.mention}*'

        if "visit" not in select.values:
            if visitante in member.roles:
                await member.remove_roles(visitante)
                removido += f'\n*- {visitante.mention}*'

        if "parti" not in select.values:
            if participar in member.roles:
                await member.remove_roles(participar)
                removido += f'\n*- {participar.mention}*'

        await interaction.edit_original_response(content=f'{"" if len(mantem)<14 else mantem} {"" if len(add)<17 else add} {"" if len(removido)<17 else removido}')


class CargosSelector(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.member_view = MemberView(timeout=None)
        self.plataforma_view = PlataformaView(timeout=None)
        self.diario_view = DiarioView(timeout=None)
        self.squad_view = SquadView(timeout=None)
        self.alerta_view = AlertaView(timeout=None)

    async def cog_load(self):
        self.bot.add_view(self.member_view)
        self.bot.add_view(self.plataforma_view)
        self.bot.add_view(self.diario_view)
        self.bot.add_view(self.squad_view)
        self.bot.add_view(self.alerta_view)

    @commands.command(name='view')
    @commands.is_owner()
    async def membros_view(self, ctx: commands.Context):
        ''' Inicia os seletores de cargos '''

        channel = await self.bot.fetch_channel(config.cargo_reacao)
        
        memberEmbed = discord.Embed(color=config.roxo,
                                    description='Selecione o cargo que lhe representa na aliança: '
                                       '<:Andromeda:615250826474291211> '
                                       '<:Aquila:615250826289741834> '
                                       '<:Lyra:615250826260381735> '
                                       '<:Orion:615250826872619196> 👥 🤝')

        plataformaEmbed = discord.Embed(color=config.roxo,
                                        description='Selecione as plataformas em que você joga: 💻 🎮 📱')

        diarioEmbed = discord.Embed(color=config.roxo,
                                    description='Selecione os ping de horarios que deseja: ☀️ 🌑 ❄️ 🔥')

        squadEmbed = discord.Embed(color=config.roxo,
                                   description='Selecione os ping de esquadrões que deseja: <:reliquia:664486282046472202> <:Creditos:596817907984498718> <:recurso:664484737951334401> <:Forma:821407092698906656>')

        alertaEmbed = discord.Embed(color=config.roxo,
                                   description='Selecione os ping de alertas que deseja: <:reator:844951875791093760> <:catalisador:844951875371401247> <:BaroBitchPlease:716035316464615455> <:FormaUmbraiss:679970463153258512>')

        await ctx.message.delete()
        await channel.send(embed=memberEmbed, view=MemberView())
        await channel.send(embed=plataformaEmbed, view=PlataformaView())
        await channel.send(embed=diarioEmbed, view=DiarioView())
        await channel.send(embed=squadEmbed, view=SquadView())
        await channel.send(embed=alertaEmbed, view=AlertaView())


async def setup(bot):
    await bot.add_cog(CargosSelector(bot))