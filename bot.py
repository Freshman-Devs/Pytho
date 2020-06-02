import discord
from discord.ext import commands
import random

TOKEN = 'Your token'


client = commands.Bot(command_prefix = '~')
client.remove_command("help")

@client.event
async def on_ready():
    print('Ready!')
    print('Version 2.6.0')
    print('Im watching you...')
    activity = discord.Game(name=random.randint(1,101), type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'These are my commands. \n Some require moderator permissions. \n Commands are case sensitive. All are lowercase.',
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Derpi')
    embed.add_field(name='Commands', value='Help \n Say - mod command \n Info \n Ban - mod command \n Kick - mod command \n Issue \n Credits \n Clear <number> - mod command \n Invite \n MyInfo \n Hi \n EmbedSay \n AboutBot \n RandomGen \n SetStatus - mod command \n calc \n Mute - mod command \n Changelog \n CreateChannel - mod command', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    await ctx.send('This bot was made by Derpi in Python 3.8, hence the name Pytho.')

@client.command()
async def embedsay(ctx, *, arg,):
    await ctx.message.delete()
    embed = discord.Embed(
        title = "M E S S A G E",
        description = arg,
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Derpi | Version 2.6.0')
    await ctx.send(ctx.author.mention + ' says...',)
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev","Mod","Mods","Team",)
async def say(ctx, *, arg,):
    await ctx.message.delete()
    await ctx.send(arg)

@client.command()
@commands.is_owner()
async def ownersay(ctx, *, arg,):
    await ctx.message.delete()
    await ctx.send(arg)

@client.command(pass_context=True)
@commands.has_any_role("Admin","Moderator","Owner","Dev","Mods","Mod","Team",)
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "No reason provided."
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")
    await ctx.ban(member)
    print(f'{member} has been banned from {ctx.guild.name} for {reason}')

@client.command(pass_context = True)
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev",)
async def kick(ctx, userName: discord.User):
    await ctx.guild.kick(userName)
    await ctx.member.send('You have been kicked from {ctx.guild.name}. Contact a moderator in {ctx.guild.name} for more info.')

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    await ctx.send("Shutdown.")


@client.command()
async def issue(ctx):
    await ctx.send('Broken commands \n - Kick  \n - Ban \n - Mute')



@client.command()
async def credits(ctx):
    await ctx.send('Thanks to Derpi for writing and creating most of the bot.')
    await ctx.send('Thanks to Avery R for some commands like Ban and Kick.')
    await ctx.send("Thanks to Jim for the logo.")


@client.command(pass_context=True)
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev","Mods","Mod","Team",)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send('Message(s) deleted.')

@client.command()
async def invite(ctx):
    await ctx.send('Want to add me to your server? Heres my link! \n https://discordapp.com/api/oauth2/authorize?client_id=691087901198516295&permissions=8&scope=bot')

@client.command()
async def myinfo(ctx):
        embed = discord.Embed(
        title = 'Your Info',
        description = 'I currently have nothing on you.',
        colour = discord.Colour.blue()

    )
        embed.set_footer(text='Created by Derpi')
        await ctx.author.send(embed=embed)
        await ctx.send('I sent the info to your DMs! Make sure you have them open.')

@client.command()
async def hi(ctx):
    await ctx.send("Hi!")


@client.command()
async def aboutbot(ctx):
    await ctx.send("Pytho is a product of Freshman Devs. \n Pytho is developed in discord.py \n Developed by <@595397105103667236>")

@client.command()
@commands.is_owner()
async def setstatus(ctx, *, arg,):
    await ctx.message.delete()
    activity = discord.Game(name=arg, type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send("Done!")
    await ctx.send("Status: playing " + arg)

@client.command()
async def randomgen(ctx):
    await ctx.send(random.randint(0,101))

@client.command()
@commands.is_owner()
async def code(ctx, *, arg):
    await eval(arg)

@client.command()
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev","Mods","Bot Manager", "Mod","Team",)
async def mute(ctx, member : discord.Member, *, reason = None):
    muterole = discord.utils.get(ctx.guild.roles, name = "Muted")
    await member.add_roles(member, muterole)
    await ctx.send('Member was successfully muted.')
    await ctx.member.send('You were muted in {ctx.guild.name}. Reason:')
    await ctx.member.send(reason)


@client.command()
async def changelog(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title = "Changelog",
        description = "v2.70 \n - Removed anti invite link. \n Added ~createchannel. (~createchannel <name>)",
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Derpi | Version 2.61')
    await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev","Mods","Bot Manager", "Mod","Team",)
async def createchannel(ctx, *, arg):
    guild = ctx.message.guild    
    await ctx.message.delete()
    await guild.create_text_channel(arg)



client.run(TOKEN)