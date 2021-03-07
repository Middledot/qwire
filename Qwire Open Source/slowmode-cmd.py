import discord
import typing
from discord.ext import commands

client = commands.Bot(command_prefix="?")

@client.command()
@commands.bot_has_permissions(manage_channels=True)
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, channel:typing.Optional[discord.TextChannel], *, value:str=None):
    channel = channel or ctx.channel
    if value == None:
        return await ctx.send("No value has been given.")
    elif value == "off":
        if channel.slowmode_delay == 0:
            return await ctx.send('Slowmode if already turned off.')
        await channel.edit(slowmode_delay=0)
        return await ctx.send('✅ Slowmode has been turned off.')
    if value[0] == '+':
        value = value[1:]
        method = "add"
    elif value[0] == '-':
        value = value[1:]
        method = "rem"
    else:
        method = None
    times = value.split(' ')
    seconds = 0
    if len(times) == 1:
        try:
            seconds = int(times[0])
        except ValueError:
            stimes = []
            for i in times:
                if 's' in i:
                    stimes.append(i.replace('s', ''))
                    continue
                elif 'm' in i:
                    stimes.append(str(int(i.replace('m', ''))*60))
                    continue
                elif 'h' in i:
                    stimes.append(str(int(i.replace('h', ''))*60*60))
                    continue
                else:
                    stimes.append(None)
            for i in stimes:
                if i == None:
                    return await ctx.send('Value is invalid')
                seconds = seconds + int(i)
    else:
        stimes = []
        for i in times:
            if 's' in i:
                stimes.append(i.replace('s', ''))
                continue
            elif 'm' in i:
                stimes.append(str(int(i.replace('m', ''))*60))
                continue
            elif 'h' in i:
                stimes.append(str(int(i.replace('h', ''))*60*60))
                continue
            else:
                stimes.append(None)
        for i in stimes:
            if i == None:
                return await ctx.send('One or several of the time values are invalid.')
            seconds = seconds + int(i)
    if method == "add":
        if seconds > 21600:
            return await ctx.send('Time given is longer than six hours.')
        elif seconds < 0:
            return await ctx.send('Double/several negatives were given.')
        await channel.edit(slowmode_delay=channel.slowmode_delay+seconds)
    elif method == "rem":
        if seconds < 0:
            return await ctx.send('Time given is negative.')
        elif seconds > 21600:
            return await ctx.send('You cannot remove that much time from the slowmode.')
        await channel.edit(slowmode_delay=channel.slowmode_delay-seconds)
    else:
        if seconds < 0:
            return await ctx.send('Time given is negative.')
        elif seconds > 21600 and method:
            return await ctx.send('Time given is longer than six hours.')
        await channel.edit(slowmode_delay=seconds)
    await ctx.send('✅ Slowmode has been set.')

client.run("TOKEN")
