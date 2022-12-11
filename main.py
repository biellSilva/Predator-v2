import discord
import os
import dotenv
import asyncio

from discord.ext import commands
from discord.ext.commands import Context


class Predator(commands.Bot):
    def __init__(self, intents: discord.Intents):
        super().__init__(command_prefix='p!', intents=intents)
        self.initial_extensions = []
        

    async def setup_hook(self):
        self.task = self.loop.create_task(self.ch_pr())

        for filename in os.listdir('./Extensions2'):
            if filename.endswith('.py'):
                await self.load_extension('Extensions2.' + filename[:-3])
                self.initial_extensions.append(filename[:-3])

        print(self.initial_extensions)


    async def on_ready(self):
        print('-'*15)
        print(bot.user)
        print(f'{bot.status} - {bot.latency:.0f} ms')
        print('-'*15)


    async def ch_pr(self):
        await self.wait_until_ready()
        while not self.is_closed():

            members = 0
            for guild in self.guilds:
                members += guild.member_count - 1

            await self.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=f'p!help ou /help'))

            await asyncio.sleep(600)

            await self.change_presence(activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=f'Warframe com {members} players'))

            await asyncio.sleep(600)


bot = Predator(intents=discord.Intents.all())


@bot.command()
@commands.guild_only()
@commands.is_owner()
async def synnc(ctx: Context, spec = None):
    async with ctx.typing():
        if spec != None:
            if spec == "clear":
                # p!sync clear      apaga e synca
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync()
                sync = []

            else:
                await ctx.reply('apenas `clear` é aceito')
                return

        else:
            # p!sync            synca global
            sync = await ctx.bot.tree.sync()

        await ctx.reply(f'{len(sync)} comandos sincronizados {" " if spec == None else "para este servidor."}')
        return


dotenv.load_dotenv(dotenv.find_dotenv())
token = os.getenv('token1')
bot.run(token=token)
