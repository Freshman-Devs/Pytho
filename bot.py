import discord
from discord.ext import commands
import youtube_dl


TOKEN = 'YOUR TOKEN'


client = commands.Bot(command_prefix = '~')
client.remove_command("help")

@client.event
async def on_ready():
    print('Ready!')
    activity = discord.Game(name="whatever you want", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'These are my commands. \n Some require moderator permissions. \n Commands are case sensitive. All are lowercase.',
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Derpi')
    embed.add_field(name='Commands', value='Help \n Say \n Info \n Ban \n Kick \n Issue \n Home \n Credits \n Ad <1-4> \n Clear <number> \n Invite \n MyInfo \n EmbedSay', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    await ctx.send('This bot was made by Derpi in Python 3.8, hence the name Pytho.')

@client.command()
async def embedsay(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(
        title = 'Someone says...',
        description = arg,
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Derpi | Version 2.3.0')
    await channel.send(embed=embed)
    await channel.send(ctx.author)
    await channel.send(ctx.guild.name)
    await channel.send(ctx.channel.name)
    await ctx.send(embed=embed)
    await ctx.send(ctx.author)

@client.command()
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev",)
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@client.command()
@commands.has_any_role("Admin","Moderator","Owner","Dev",)
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "No reason provided."
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")
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
    await ctx.send('No issues detected.')

@client.command()
async def home(ctx):
    await ctx.send('This is my birthplace and home.')
    await ctx.send('https://discord.gg/pbw6hPP')
    await ctx.send('Welcome home.')


@client.command()
async def credits(ctx):
    await ctx.send('Thanks to Derpi for writing and creating most of the bot.')
    await ctx.send('Thanks to Avery R for some commands like Ban and Kick.')
    await ctx.send("Thanks to Jim for the logo.")


@client.command()
async def ad1(ctx):
    await ctx.send('whatever')

@client.command()
async def ad2(ctx):
    await ctx.send('whatever')

@client.command()
async def ad3(ctx):
    await ctx.send('whatever')

@client.command()
async def ad4(ctx):
    await ctx.send('whatever')

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "Member") 
    await ctx.add_roles(role)

@client.command(pass_context=True)
@commands.has_any_role("Admin","Moderator","Owner","Administrator","Dev",)
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


client.run(TOKEN)