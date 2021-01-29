import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.command()
# the following checks if the bot can add reactions, throws an error if cannot
@commands.bot_has_permissions(add_reactions=True)
async def example(ctx):
    # In the following list, set all the "pages" of which your bot will cycle through
    listt = [discord.Embed(description="Example 1"), discord.Embed(description="Example 2"), discord.Embed(description="Example 3")]
    current = 0
    # Sends the initial message
    msg = await ctx.send(embed=listt[0].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
    # Adds all the reactions
    await msg.add_reaction('⏮️')
    await msg.add_reaction('◀️')
    await msg.add_reaction('▶️')
    await msg.add_reaction('⏭️')
    await msg.add_reaction('⏹️')
    def check(reaction, user):
        return user == ctx.author and reaction.message.id == msg.id
    # This forever loop is only broken when the user doesn't respond within 60 seconds or they pressed the ⏹️ option
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            break
        else:
            # This checks if the bot can remove the users reaction to make maneuvering faster for the user
            if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
                await msg.remove_reaction(reaction, user)

            # next
            if str(reaction) == '▶️':
                if current != len(listt)-1:
                    await msg.edit(embed=listt[current+1].set_footer(text=f"{str(current+2)}/{str(len(listt))}"))
                    current = current + 1
            # previous
            if str(reaction) == '◀️':
                if current != 0:
                    await msg.edit(embed=listt[current-1].set_footer(text=f"{str(current)}/{str(len(listt))}"))
                    current = current - 1
            # beginning
            if str(reaction) == '⏮️':
                current = 0
                await msg.edit(embed=listt[0].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
            # last
            if str(reaction) == '⏭️':
                current = len(listt)-1
                await msg.edit(embed=listt[len(listt)-1].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
            # stop
            if str(reaction) == '⏹️':
                await msg.edit(embed=discord.Embed(description="Ended"))
                await msg.remove_reaction('⏮️', client.user)
                await msg.remove_reaction('◀️', client.user)
                await msg.remove_reaction('▶️', client.user)
                await msg.remove_reaction('⏭️', client.user)
                await msg.remove_reaction('⏹️', client.user)
                break
@example.error
async def exmaple_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Cannot initialize pages, missing permissions to add reactions.')

client.run(YOUR_TOKEN)