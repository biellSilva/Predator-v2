

'''

Desabilitado e trocado para
RoleSelector.py

'''




import discord
import discord.utils
import asyncio
import pytz

from datetime import datetime
from discord.ext import commands

COR = 0x690FC3

tz_brazil = pytz.timezone('America/Sao_Paulo')


class CargosEvent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_raw_reaction_add')
    async def geral(self, payload: discord.RawReactionActionEvent):

        member     = payload.member    
        guild      = member.guild
        emoji      = payload.emoji.name

        tennoID = self.bot.main_tennoID
        
        if tennoID == payload.message_id:

            tan        = guild.get_role(1000948462512263238)
            ta         = guild.get_role(1000948461342048296)
            tl         = guild.get_role(1000948463732805632)
            to         = guild.get_role(1000948460331225219)

            visitante  = guild.get_role(1000948466958209155)
            participar = guild.get_role(1000948465800577044)
            membro     = guild.get_role(1000948464869453905)

            recrutador = guild.get_role(1000948440135639180)

            channelRec = guild.get_channel(1000948600425156648)

            if member.bot == True:
                return

            if emoji == "Andromeda":
                await member.add_roles(tan)
                await member.add_roles(membro)

            if emoji == "Aquila":
                await member.add_roles(ta)
                await member.add_roles(membro)

            if emoji == "Lyra":
                await member.add_roles(tl)
                await member.add_roles(membro)

            if emoji == "Orion":
                await member.add_roles(to)
                await member.add_roles(membro)

            if emoji == "👥":
                await member.remove_roles(membro)
                await member.add_roles(visitante)

            if emoji == "🤝":
                await member.remove_roles(membro)
                await member.add_roles(participar)
                
                embedRec = discord.Embed(title="Recrutamento",
                                       color=COR,
                                       description= f"Olá {member.mention}! Para um atendimento rapido nos informe seu nick no Warframe\n\n"
                                                    "Informe um dos clãs abaixo para notificarmos um recrutador\n"
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

            if tan in member.roles:
                await member.remove_roles(tan)              

            if ta in member.roles:
                await member.remove_roles(ta)

            if tl in member.roles:
                await member.remove_roles(tl)

            if to in member.roles:
                await member.remove_roles(to)

            if visitante in member.roles:
                await member.remove_roles(visitante)

            if participar in member.roles:
                await member.remove_roles(participar)
            
##############################################

        ignisID = self.bot.main_ignisID
        
        if ignisID == payload.message_id:

            ignis  = guild.get_role(1000948521085706330)

            if member.bot == True:
                return

            if emoji == "IgnisWraith":
                role = ignis
                await member.add_roles(role)

###############################################

        squadID = self.bot.main_squadID

        if squadID == payload.message_id:

            member = payload.member
            guild  = member.guild                    # ADICIONA
            emoji  = payload.emoji.name              # SQUAD

            eidolon    = guild.get_role(1000948539255435274)
            profit     = guild.get_role(1000948553864196096)
            relic      = guild.get_role(1000948545169408091)
            steel      = guild.get_role(1000948552178081832)
            index      = guild.get_role(1000948540031385740)
            recurso    = guild.get_role(1000948540933144648)
            arbitros   = guild.get_role(1000948541960753272)
            xp         = guild.get_role(1000948542661206077)
            railjack   = guild.get_role(1000948543919509538)
            deimos     = guild.get_role(1000948554895999066)
            santuario  = guild.get_role(1000948545991487530)
            kuvalich   = guild.get_role(1000948546893271210)
            corpuslich = guild.get_role(1000948547778261074)
            kuva       = guild.get_role(1000948548969443450)
            anjos      = guild.get_role(1000948555772596316)
            praga      = guild.get_role(1000948551372775454)
            novato     = guild.get_role(1000948550450024488)
            archon     = guild.get_role(1020906135353573506)

            if member.bot == True:
                return

            if emoji == "ostron":
                role = eidolon
                await member.add_roles(role)

            if emoji == "ProfitTaker": 
                role = profit  
                await member.add_roles(role)

            if emoji == "reliquia":
                role = relic
                await member.add_roles(role)

            if emoji == "essencia":
                role = steel
                await member.add_roles(role)

            if emoji == "Creditos":
                role = index
                await member.add_roles(role)

            if emoji == "recurso":
                role = recurso
                await member.add_roles(role)

            if emoji == "arbiters":
                role = arbitros
                await member.add_roles(role)

            if emoji == "afinidade":
                role = xp
                await member.add_roles(role)

            if emoji == "CephalonCy":
                role = railjack
                await member.add_roles(role)

            if emoji == "Entrati":
                role = deimos
                await member.add_roles(role)

            if emoji == "Simaris":
                role = santuario
                await member.add_roles(role)

            if emoji == "ReliquiaRequiem":
                role = kuvalich
                await member.add_roles(role)

            if emoji == "granum":
                role = corpuslich
                await member.add_roles(role)

            if emoji == "Kuva":
                role = kuva
                await member.add_roles(role)

            if emoji == "void":
                role = anjos
                await member.add_roles(role)

            if emoji == "Forma":
                role = praga
                await member.add_roles(role)

            if emoji == "LotusGold":
                role = novato
                await member.add_roles(role)

            if emoji == "🐍":
                role = archon
                await member.add_roles(role)

###################################################

        diarioID = self.bot.main_diarioID

        if diarioID == payload.message_id:

            member = payload.member                 # ADICIONA
            guild  = member.guild                   # PING DIARIO
            emoji  = payload.emoji.name

            dia    = guild.get_role(1000948512046985267)
            noite  = guild.get_role(1000948511438798848)
            vome   = guild.get_role(1000948528614486056)
            fass   = guild.get_role(1000948527247151167)
            frio   = guild.get_role(1000948525825282089)
            morno  = guild.get_role(1000948523837181952)

            if member.bot == True:
                return

            if emoji == "☀️":
                role = dia
                await member.add_roles(role)

            if emoji == "🌑":
                role = noite
                await member.add_roles(role)

            if emoji == "🔵":
                role = vome
                await member.add_roles(role)

            if emoji == "🔴":
                role = fass
                await member.add_roles(role)

            if emoji == "❄️":
                role = frio
                await member.add_roles(role)

            if emoji == "🔥":
                role = morno
                await member.add_roles(role)

#############################################

        pingID = self.bot.main_pingID

        if pingID == payload.message_id:

            member      = payload.member                            # ADICIONA
            guild       = member.guild                              # CARGOS
            emoji       = payload.emoji.name                        # PING

            ajudante    = guild.get_role(1000948509375209532)
            reator      = guild.get_role(1000948513355604048)
            catalisador = guild.get_role(1000948514202865796)
            baro        = guild.get_role(1000948516169990194)
            forma       = guild.get_role(1000948520263618560)
            lotus       = guild.get_role(1000948531449835560)
            mestre      = guild.get_role(1000948519231828038)
            sorteio     = guild.get_role(1000948516589416492)
            eventoExt   = guild.get_role(1000948521509335121)
            dropExt     = guild.get_role(1000948518044835870)
            update      = guild.get_role(1000948510310531183)

            if member.bot == True:
                return

            if emoji == "🆘":
                role = ajudante
                await member.add_roles(role)

            if emoji == "reator":
                role = reator
                await member.add_roles(role)

            if emoji == "catalisador":
                role = catalisador
                await member.add_roles(role)

            if emoji == "BaroBitchPlease":
                role = baro
                await member.add_roles(role)

            if emoji == "FormaUmbraiss":
                role = forma
                await member.add_roles(role)

            if emoji == "LotusCosmica":
                role = lotus
                await member.add_roles(role)

            if emoji == "graomestre":
                role = mestre
                await member.add_roles(role)

            if emoji == "🎉":
                role = sorteio
                await member.add_roles(role)

            if emoji == "🎊":
                role = eventoExt
                await member.add_roles(role)

            if emoji == "🎁":
                role = dropExt
                await member.add_roles(role)

            if emoji == "🔔":
                role = update
                await member.add_roles(role)

#######################################################################################
############################# REMOVE CARGOS ###########################################
#######################################################################################

    @commands.Cog.listener('on_raw_reaction_remove')
    async def tenno(self, payload: discord.RawReactionActionEvent):

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji = payload.emoji.name

        tennoID = self.bot.main_tennoID

        tan        = 1000948462512263238
        ta         = 1000948461342048296
        tl         = 1000948463732805632
        to         = 1000948460331225219

        visitante  = 1000948466958209155
        participar = 1000948465800577044
        membro     = 1000948464869453905

        if payload.message_id == tennoID:

            if emoji == "Andromeda":
                role = discord.utils.get(guild.roles, id=tan)
                role2 = discord.utils.get(guild.roles, id=membro)
                await member.remove_roles(role)
                await member.remove_roles(role2)

            if emoji == "Aquila":
                role = discord.utils.get(guild.roles, id=ta)
                role2 = discord.utils.get(guild.roles, id=membro)
                await member.remove_roles(role)
                await member.remove_roles(role2)

            if emoji == "Lyra":
                role = discord.utils.get(guild.roles, id=tl)
                role2 = discord.utils.get(guild.roles, id=membro)
                await member.remove_roles(role)
                await member.remove_roles(role2)

            if emoji == "Orion":
                role = discord.utils.get(guild.roles, id=to)
                role2 = discord.utils.get(guild.roles, id=membro)
                await member.remove_roles(role)
                await member.remove_roles(role2)

            if emoji == "👥":
                role = discord.utils.get(guild.roles, id=visitante)
                await member.remove_roles(role)
            
            if emoji == "🤝":
                role = discord.utils.get(guild.roles, id=participar)
                await member.remove_roles(role)

#######################################################################

    @commands.Cog.listener('on_raw_reaction_remove')
    async def ignis(self, payload: discord.RawReactionActionEvent):

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji = payload.emoji.name

        ignisID = self.bot.main_ignisID       #embed ID

        ignis = 1000948521085706330         #cargo ID

        if payload.message_id == ignisID:

            if emoji == "IgnisWraith":
                role = discord.utils.get(guild.roles, id=ignis)
                await member.remove_roles(role)

#########################################################

    @commands.Cog.listener('on_raw_reaction_remove')
    async def squad(self, payload: discord.RawReactionActionEvent):

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji = payload.emoji.name

        squadID = self.bot.main_squadID

        eidolon = 1000948539255435274
        profit = 1000948553864196096
        relic = 1000948545169408091
        steel = 1000948552178081832
        index = 1000948540031385740
        recurso = 1000948540933144648
        arbitros = 1000948541960753272
        xp = 1000948542661206077
        railjack = 1000948543919509538
        deimos = 1000948554895999066
        santuario = 1000948545991487530
        kuvalich = 1000948546893271210
        corpuslich = 1000948547778261074
        kuva = 1000948548969443450
        anjos = 1000948555772596316
        praga = 1000948551372775454
        novato = 1000948550450024488
        archon = 1020906135353573506

        if payload.message_id == squadID:

            if emoji == "ostron":
                role = discord.utils.get(guild.roles, id=eidolon)
                await member.remove_roles(role)

            if emoji == "ProfitTaker":
                role = discord.utils.get(guild.roles, id=profit)
                await member.remove_roles(role)

            if emoji == "reliquia":
                role = discord.utils.get(guild.roles, id=relic)
                await member.remove_roles(role)

            if emoji == "essencia":
                role = discord.utils.get(guild.roles, id=steel)
                await member.remove_roles(role)

            if emoji == "Creditos":
                role = discord.utils.get(guild.roles, id=index)
                await member.remove_roles(role)

            if emoji == "recurso":
                role = discord.utils.get(guild.roles, id=recurso)
                await member.remove_roles(role)

            if emoji == "arbiters":
                role = discord.utils.get(guild.roles, id=arbitros)
                await member.remove_roles(role)

            if emoji == "afinidade":
                role = discord.utils.get(guild.roles, id=xp)
                await member.remove_roles(role)

            if emoji == "CephalonCy":
                role = discord.utils.get(guild.roles, id=railjack)
                await member.remove_roles(role)

            if emoji == "Entrati":
                role = discord.utils.get(guild.roles, id=deimos)
                await member.remove_roles(role)

            if emoji == "Simaris":
                role = discord.utils.get(guild.roles, id=santuario)
                await member.remove_roles(role)

            if emoji == "ReliquiaRequiem":
                role = discord.utils.get(guild.roles, id=kuvalich)
                await member.remove_roles(role)

            if emoji == "granum":
                role = discord.utils.get(guild.roles, id=corpuslich)
                await member.remove_roles(role)

            if emoji == "Kuva":
                role = discord.utils.get(guild.roles, id=kuva)
                await member.remove_roles(role)

            if emoji == "void":
                role = discord.utils.get(guild.roles, id=anjos)
                await member.remove_roles(role)

            if emoji == "Forma":
                role = discord.utils.get(guild.roles, id=praga)
                await member.remove_roles(role)

            if emoji == "LotusGold":
                role = discord.utils.get(guild.roles, id=novato)
                await member.remove_roles(role)

            if emoji == "🐍":
                role = discord.utils.get(guild.roles, id=archon)
                await member.remove_roles(role)

######################################################

    @commands.Cog.listener('on_raw_reaction_remove')
    async def diario(self, payload: discord.RawReactionActionEvent):

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji = payload.emoji.name

        diarioID = self.bot.main_diarioID

        dia = 1000948512046985267
        noite = 1000948511438798848
        vome = 1000948528614486056
        fass = 1000948527247151167
        frio = 1000948525825282089
        morno = 1000948523837181952

        if diarioID == payload.message_id:

            if emoji == "☀️":
                role = discord.utils.get(guild.roles, id=dia)
                await member.remove_roles(role)

            if emoji == "🌑":
                role = discord.utils.get(guild.roles, id=noite)
                await member.remove_roles(role)

            if emoji == "🔵":
                role = discord.utils.get(guild.roles, id=vome)
                await member.remove_roles(role)

            if emoji == "🔴":
                role = discord.utils.get(guild.roles, id=fass)
                await member.remove_roles(role)

            if emoji == "❄️":
                role = discord.utils.get(guild.roles, id=frio)
                await member.remove_roles(role)

            if emoji == "🔥":
                role = discord.utils.get(guild.roles, id=morno)
                await member.remove_roles(role)

##################################################

    @commands.Cog.listener('on_raw_reaction_remove')
    async def alerta(self, payload: discord.RawReactionActionEvent):

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        emoji = payload.emoji.name

        pingID = self.bot.main_pingID

        ajudante = 1000948509375209532
        reator = 1000948513355604048
        catalisador = 1000948514202865796
        baro = 1000948516169990194
        forma = 1000948520263618560
        lotus = 1000948531449835560
        mestre = 1000948519231828038
        sorteio = 1000948516589416492
        eventoExt = 1000948521509335121
        dropExt = 1000948518044835870
        update = 1000948510310531183

        if pingID == payload.message_id:

            if emoji == "🆘":
                role = discord.utils.get(guild.roles, id=ajudante)
                await member.remove_roles(role)

            if emoji == "reator":
                role = discord.utils.get(guild.roles, id=reator)
                await member.remove_roles(role)

            if emoji == "catalisador":
                role = discord.utils.get(guild.roles, id=catalisador)
                await member.remove_roles(role)

            if emoji == "BaroBitchPlease":
                role = discord.utils.get(guild.roles, id=baro)
                await member.remove_roles(role)

            if emoji == "FormaUmbraiss":
                role = discord.utils.get(guild.roles, id=forma)
                await member.remove_roles(role)

            if emoji == "LotusCosmica":
                role = discord.utils.get(guild.roles, id=lotus)
                await member.remove_roles(role)

            if emoji == "graomestre":
                role = discord.utils.get(guild.roles, id=mestre)
                await member.remove_roles(role)

            if emoji == "🎉":
                role = discord.utils.get(guild.roles, id=sorteio)
                await member.remove_roles(role)

            if emoji == "🎊":
                role = discord.utils.get(guild.roles, id=eventoExt)
                await member.remove_roles(role)

            if emoji == "🎁":
                role = discord.utils.get(guild.roles, id=dropExt)
                await member.remove_roles(role)

            if emoji == "🔔":
                role = discord.utils.get(guild.roles, id=update)
                await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(CargosEvent(bot))