import discord
import random
from redbot.core import checks, commands

class MediaOnly(commands.Cog):

    def __init__(self, bot):
        """Initialise cog."""
        self.bot = bot

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
    async def on_message_without_command(self, ctx, msg):
        for guild in self.bot.guilds:
            channel = await self.config.guild(guild).channelid()
        if msg.author.bot:
            return False
        try:
            if msg.attachments.size == 0:
                msg.delete
                await ctx.send('Only Media Files are allowed in this channel', delete_after=5)
        except (discord.HTTPException, discord.Forbidden, ):
                pass
