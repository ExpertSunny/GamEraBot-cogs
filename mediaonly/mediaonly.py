import discord
import random
from redbot.core import Config, checks, commands

class MediaOnly(commands.Cog):

    def __init__(self, bot):
        """Initialise cog."""
        self.bot = bot
        self.config = Config.get_conf(self, identifier=786246974985732136, force_registration=True)
        self.config.register_global(
            mute_length=300, amount=5, per=5, mod_bypass=True, logging=None
        )
        default_guild = {"channelid": None}
        self.config.register_guild(**default_guild)

    @commands.group(name="mediaonly", aliases=["mo"])
    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    async def _mo(self, ctx: commands.Context):
        """
        Base command for managing MediaOnly settings
        Do `[p]help mo <subcommand>` for more details
        """
        pass

    @_mo.command()
    async def setchannel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """
        Set the announcement channel for this server
        Don't pass a channel to clear this server of receiving announcements
        """
        if channel is not None:
            await self.config.guild(ctx.guild).channelid.set(channel.id)
            await ctx.send("Media channel has been set to {}".format(channel.mention))
        else:
            await self.config.guild(ctx.guild).channelid.set(None)
            await ctx.send("Media channel has been cleared")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, msg):
        for guild in self.bot.guilds:
            channel = await self.config.guild(guild).channelid()
        print(channel)
        if msg.author.bot:
            return False
        try:
            if msg.attachments == False:
                msg.delete
                await channel.send('Only Media Files are allowed in this channel', delete_after=5)
        except (discord.HTTPException, discord.Forbidden, ):
                pass
