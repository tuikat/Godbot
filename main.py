import discord
from discord.ext import commands
import music

client = commands.Bot(command_prefix = '-', intents = discord.Intents.all())

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    print('bot is ready.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over this server'))

@client.command()
async def ping(ctx):
    await ctx.send('pong!')

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@commands.has_permissions(ban_members=True)
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')

@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@commands.has_permissions(manage_messages=True)
@client.command()
async def purge(ctx):
    await ctx.channel.purge()

@commands.has_permissions(manage_roles=True)
@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
    await user.add_roles(role)
    await ctx.send(f'Successfully given `{role.name}` to `{user.name}`.')

@commands.has_permissions(manage_roles=True)
@client.command()
async def removerole(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
    await ctx.send(f'Successfully removed `{role.name}` from `{user.name}`.')

@commands.has_permissions(manage_roles=True)
@client.command(name='deleterole', pass_context=True)
async def deleterole(ctx, role_name):
    role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role_object.delete()
    await ctx.send(f'`role deleted`')

@commands.has_permissions(manage_roles=True)
@client.command(name='createrole', pass_context=True)
async def createrole(ctx, role_name):
    guild = ctx.guild
    await guild.create_role(name=role_name)
    await ctx.send(f'`role created`')

client.run('ODc1MTU0NjgyNzkwNzAzMTA1.YRRZTw.ZaGaur7QSlhizJTNcK0iA0Buh2g')