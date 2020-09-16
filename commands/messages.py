from discord.ext import commands

class MessageStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear', pass_context=True)
    async def clear(self, ctx, username=None):
        await ctx.message.delete()
        channel = None
        if not username:
            channel = ctx.channel
        else:
            for private_channel in self.bot.private_channels:
                if str(username) in str(private_channel):
                    channel = private_channel
        
        if not channel:
            return
        
        print(f"Clearing messages with {channel}")
        async for message in channel.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    @commands.command(name='attachments', pass_context=True)
    async def attachments(self, ctx, username=None):
        await ctx.message.delete()
        channel = None
        if not username:
            channel = ctx.channel
        else:
            for private_channel in self.bot.private_channels:
                if str(username) in str(private_channel):
                    channel = private_channel
        
        if not channel:
            return
        
        print(f"Deleting attachments with {channel}")
        async for message in channel.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                if message.attachments:
                    await message.delete()
            except:
                pass            

    @commands.command(name='edit', pass_context=True)
    async def edit(self, ctx, text: str, username=None,
    description='Edits every single message in a certain channel'):
        await ctx.message.delete()
        channel = None
        if not username:
            channel = ctx.channel
        else:
            for private_channel in self.bot.private_channels:
                if str(username) in str(private_channel):
                    channel = private_channel
        
        if not channel:
            return
        
        print(f"Editing messages with {channel}")
        async for message in channel.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.edit(content=text)
            except:
                pass    

    @commands.command(name='clearfriends')
    async def clearfriends(self, ctx,
    description='Clears messages with all of your friends'):
        await ctx.message.delete()
        for friend in self.bot.user.friends:        
            async for message in friend.history(limit=None).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
                try:
                    await message.delete()
                except:
                    pass   

def setup(bot):
    bot.add_cog(MessageStuff(bot))