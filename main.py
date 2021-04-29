import discord
from discord.ext.commands import Bot
import asyncio
from discord.ext import commands
import os
import random
import praw
from discord import DMChannel
from keep_alive import keep_alive
from discord.ext import commands
import json
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)
reddit = praw.Reddit(client_id = "14mbLGXtOkTcSw",
client_secret = "G5Vp744PIvtEZz_Es0BUBHd70z0AfQ",
username = "Optimal-Flounder-928",
password = "eye am a simp",
user_agent = "killauX")

client = commands.Bot(command_prefix = "k!")
client.remove_command("help")



@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "list of all the current commands.Also use k!help(command category) for more info on command types ")

  em.add_field(name = "Moderation", value = "`kick`,`ban`,`mute`,`clear`")
  em.add_field(name = "Fun", value = "`ask`,`anime`,`kill`,`say`,`hello`,`insult`,`die`")


  await ctx.send(embed = em)

  

@help.command()
async def kick(ctx):

  em = discord.Embed(title = "Kick", description = "kicks a user from the server",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!kick <member> [reason]")

  await ctx.send(embed = em)



@help.command()
async def mute(ctx):

  em = discord.Embed(title = "Mute", description = "Mutes a server until unmuted with k!unmute",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!mute <member>")

  await ctx.send(embed = em)



@help.command()
async def ban(ctx):

  em = discord.Embed(title = "BAN", description = "Bans a user from the server, k!unban <user#tag> to unban",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!ban <member>")

  await ctx.send(embed = em)



@help.command()
async def clear(ctx):

  em = discord.Embed(title = "Clear", description = "clears a certain amount of messages from 1-100",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!clear 5")

  await ctx.send(embed = em)



@help.command()
async def ask(ctx):

  em = discord.Embed(title = "Ask", description = "ask a yes or no question for killuaX to answer",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!ask am i epic?")

  await ctx.send(embed = em)



@help.command()
async def anime(ctx):

  em = discord.Embed(title = "Anime", description = "sends anime posts",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!anime")

  await ctx.send(embed = em)



@help.command()
async def kill(ctx):

  em = discord.Embed(title = "Kill", description = "'Kills' a user",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!kill <mention>")

  await ctx.send(embed = em)



@help.command()
async def say(ctx):

  em = discord.Embed(title = "Say", description = "Says anything",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!say uwu~")

  await ctx.send(embed = em)



@help.command()
async def hello(ctx):

  em = discord.Embed(title = "Hello", description = "Killua says hello in very stupid ways bc im stupid as well :pensive:",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!hello")

  await ctx.send(embed = em)



@help.command()
async def insult(ctx):

  em = discord.Embed(title = "Insult", description = "Killua can uh insult people? in very cringey ways i guess idk",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!insult <member> or just any random word")

  await ctx.send(embed = em)



@help.command()
async def die(ctx):

  em = discord.Embed(title = "Die", description = "just *dies*",color = ctx.author.color)

  em.add_field(name = "**Syntax**", value = "k!die <member> or anything else")

  await ctx.send(embed = em)



@client.event
async def on_ready():
    print("Im from an elite gang of assasins".format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name="KilluaX", url="https://www.twitch.tv/dreamwastaken"))
    bot.load_extension('cogs.leveling')

@client.command(brief="Killua greets you", description="Killua greets you")
async def hello(ctx):
    choices=['whats up','yo whas up','hey',"owo?", "am better than u",'U wont pass the hunter exam smh','good morning','uwu~','hiii']
    await ctx.send(random.choice(choices))
@client.command(brief="Killua answers a yes or no question", description = "Killua answers a yes or no question")
async def ask(ctx):
    choices=['yes','no','yasss','sadly, no','I regret saying this but yes',"you're crazy, right? ofc not!"]
    await ctx.send(random.choice(choices))
@client.command(brief= "Killua will insult someone for free " ,   description="Killua will insult anyone for free!")
async def insult(ctx,*,args):
    choices=['so dog water','ur trash kiddo','nothing but a BiG NOOB','you = noob','ur so weak lmao', "u look like that one dude that doesnt pass the hunter exam","stop existing","do you are have stupid?","ur nothing compared to me","*insults*","you have small brain","imagine not being from an elite gang of assasins what a loser am i right?","haha LOSER BAHAAHAH"]
    await ctx.send(args + ', ' + random.choice(choices))
@client.command(brief="Shows you Info on KilluaX", description="Shows you Info on KilluaX")
async def info(ctx):
    embedVar = discord.Embed(title="KilluaX Hunter report", description="KilluaX", color=000000)
    embedVar.add_field(name="Info on KilluaX", value="The KilluaX bot is a bot made by me cuz im bored..And Im adding 1-3 features each day depending on if i feel like it", inline=False)
    embedVar.set_thumbnail(url=client.user.avatar_url)
    embedVar.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(embed=embedVar)

@client.command(brief="God will strike down the user", description="God strikes down a user")
async def die(ctx,*, args):
    choices=[f"{args} fell and hit their head!", f"{args} got caught in an accident with a large shark...",f"{args} commit suicide after failing the hunter exam",f"{args} tried to build their own nuclear bomb...", f"Two trucks crashed into each other. {ctx.author.mention} and {args} the truck drivers start fighting. One of the trucks is filled with gas. The gas in the truck is leaking and {ctx.author.mention} grabs a lighter to ignite the gas. {ctx.author.mention} pushes {args} into gas and {args} blows up", f"{args} went bungee jumping, if only they knew how to...", f"We knew {args} couldn't handle it, but we let them fly that plane anyway.",f'{args} died of too much pogging',f'{args} choked on air',f"{args} died during the hunter exam RIP {ctx.author.mention}:pensive:"]
    await ctx.send(random.choice(choices))

@client.command(brief="Killua is an elite assasin",
description="killua will kill any user after this command")
async def kill(ctx):
  choices=["*burns your house down with you inside it:fire:*","*kills*","I put poison in those chips u eatin","STABY STABY :smiling_imp:"]
  await ctx.send(random.choice(choices))

@client.command(brief="sends anime posts",description="sends posts of anime from the internet")
async def anime(ctx):
  subreddit = reddit.subreddit("anime")
  all_subs = []

  top = subreddit.top(limit = 50)

  for submission in top:
    all_subs.append(submission)

  random_sub = random.choice(all_subs)

  name = random_sub.title
  url = random_sub.url

  em = discord.Embed(title = name)

  em.set_image(url = url)
  await ctx.send(embed= em)

@client.command(brief="kick an user",description="kicks a user epicly")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'{member.mention} has been kicked')

@client.command(brief="bans a user",description="bans a user")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command(brief="unbans a user with their exact name and tag",description="example of unban: k!unban ♡𝕂𝕒𝕪𝕝𝕒♡#7198")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
          return

@client.command(brief='clears an amount of messages',description='clears an amout of messages from 1-100')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@client.command(brief="make killua say something!",description="killua will say anything after k!say")
async def say(ctx, *,message):
    await ctx.message.delete()
    await ctx.send(f"{message}" .format(message))

@client.command(brief="DO NOT USE UNLESS U RLY NEED TO")
@commands.has_permissions(administrator=True)
async def dm(ctx, user: discord.User, *, msg):
    await ctx.message.delete()
    await ctx.send("DM sent")
    await user.send(f'{msg}')

@client.command(brief="mutes a user",description="mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in {guild.name} for {reason}")

@client.command(brief="unmutes a user who is already muted",description="this command unmutes a user who has already been muted")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in {ctx.guild.name}")

keep_alive()
client.run(os.environ['TOKEN'])