import discord
import random
from redbot.core import commands

class ES_Misc(commands.Cog):
    """Bonk users."""
    def __init__(self, bot):
        """Initialise cog."""
        self.bot = bot

    @commands.command()
    async def bonk(self, ctx, target: discord.Member):
        try:
            embed = discord.Embed(colour = 0xf1c40f)
            embed.add_field(name = f"BONK!!!",value = f"{ctx.author.mention} bonked **{target.mention}**! Go to horni jail!",inline = True)
            embed.set_image(url = "https://media1.tenor.com/images/6814aaf968f9cd8b914514475157eb68/tenor.gif")
            await ctx.send(embed = embed)
        except Exception as e:
            raise e
    
    @commands.command()
    async def kill(self, ctx, target: discord.Member):
        try:
            embed = discord.Embed(colour = 0xf1c40f)
            embed.add_field(name = f"RUN!!!",value = f"{ctx.author.mention} threatened **{target.mention}**!!",inline = True)
            embed.set_image(url = "https://media1.tenor.com/images/53c66d170bd4393786ccca514d9e2998/tenor.gif")
            await ctx.send(embed = embed)
        except Exception as e:
            raise e

    @commands.command()
    async def fbi(self, ctx, target: discord.Member):
        try:
            embed = discord.Embed(colour = 0xf1c40f)
            embed.add_field(name = f"FBI OPEN UP!!!",value = f"{ctx.author.mention} called the cops and got **{target.mention}** arrested!!",inline = True)
            embed.set_image(url = "https://media1.tenor.com/images/f3dede91db5fd6cd46e80f543ef1b7bf/tenor.gif")
            await ctx.send(embed = embed)
        except Exception as e:
            raise e

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, msg):
        if not isinstance(msg.channel, discord.TextChannel):
            # this is a DM or group DM, discard early
            return
        if msg.type != discord.MessageType.default:
            # this is a system message, discard early
            return

        if msg.author.id == self.bot.user.id:
            # this is ours, discard early
            return

        if msg.author.bot:
            # this is a bot, discard early
            return

        if msg.content == 'Ping!':
            await msg.channel.send(f'Pong! Latency: {round(self.bot.latency*1000)}ms')

        if msg.content == 'oof':
            try:
                response_list = ["oof", "mega oof", "oof indeed", "oof lol", "oof xD"]
                lucky_num = random.randint(0,len(response_list) - 1)
                await msg.channel.send(response_list[lucky_num])
            except (discord.HTTPException, discord.Forbidden, ):
                pass
        if msg.content == 'F' or msg.content == 'f':
            try:
                await msg.channel.send(msg.author.name+" has paid their respects.")
            except (discord.HTTPException, discord.Forbidden, ):
                pass
