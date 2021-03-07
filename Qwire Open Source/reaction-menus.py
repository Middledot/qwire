import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.command()
@commands.bot_has_permissions(add_reactions=True)
async def display_menu(ctx):
    # Just edit the list of embeds for it to work
    listt = [discord.Embed(description="Page 1"), discord.Embed(description="Page 2"), discord.Embed(description="Page 3"), discord.Embed(description="Page 4")]
    current = 0
    msg = await ctx.send(embed=listt[0].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
    await msg.add_reaction('⏮️')
    await msg.add_reaction('◀️')
    await msg.add_reaction('▶️')
    await msg.add_reaction('⏭️')
    await msg.add_reaction('🔢')
    await msg.add_reaction('⏹️')
    def check(reaction, user):
        return user == ctx.author and reaction.message.id == msg.id
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            break
        else:
            if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
                await msg.remove_reaction(reaction, user)
            if str(reaction) == '▶️':
                if current != len(listt)-1:
                    await msg.edit(embed=listt[current+1].set_footer(text=f"{str(current+2)}/{str(len(listt))}"))
                    current = current + 1
            if str(reaction) == '◀️':
                if current != 0:
                    await msg.edit(embed=listt[current-1].set_footer(text=f"{str(current)}/{str(len(listt))}"))
                    current = current - 1
            if str(reaction) == '⏮️':
                current = 0
                await msg.edit(embed=listt[0].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
            if str(reaction) == '⏭️':
                current = len(listt)-1
                await msg.edit(embed=listt[len(listt)-1].set_footer(text=f"{str(current+1)}/{str(len(listt))}"))
            if str(reaction) == '🔢':
                ms = await ctx.send('What page would you like to go to?')
                def checkit(m):
                    return m.author == ctx.author and m.channel == ctx.channel and m.guild == ctx.guild
                try:
                    mess = await client.wait_for('message', timeout=60.0, check=checkit)
                except asyncio.TimeoutError:
                    break
                else:
                    try:
                        await ms.delete()
                    except:
                        pass
                    if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
                        await mess.delete()
                    try:
                        t = int(mess.content)
                    except:
                        await ctx.send('Invalid page number.')
                    else:
                        if t < 0 or t > len(listt):
                            await ctx.send('Invalid page number.')
                        else:
                            await msg.edit(embed=listt[t-1].set_footer(text=f"{str(t)}/{str(len(listt))}"))
                            current = t-1
            if str(reaction) == '⏹️':
                await msg.edit(embed=discord.Embed(description="Ended"))
                await msg.remove_reaction('⏮️', client.user)
                await msg.remove_reaction('◀️', client.user)
                await msg.remove_reaction('▶️', client.user)
                await msg.remove_reaction('⏭️', client.user)
                await msg.remove_reaction('🔢', client.user)
                await msg.remove_reaction('⏹️', client.user)
                break
@example.error
async def example_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('❌ Do not know why but I do not have permission to add reactions.')
    else:
        raise error

client.run('YOUR_TOKEN')
