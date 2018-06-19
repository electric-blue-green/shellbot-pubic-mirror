__authors__ = 'electric-blue-green'
__license__ = 'MIT'
__status__ = 'Prototype'
import discord
from discord.ext import commands
import sqlite3
import os
import subprocess

def gettoken():
    tokenfile = open("token.txt", "r")
    tokenstring = tokenfile.read()
    tokentoken = tokenstring.split("\n")
    token = str(tokentoken[0])
    return token
token = gettoken()

description = "use $help"
bot = commands.Bot(command_prefix=["$"], description=description)
#afkarray=[]


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def eval(ctx):
    if int(ctx.author.id) == 173498062260404225:
        content = str(ctx.message.content)
        commandt = content.split("$eval")
        response=(eval(commandt[1]))
        if response != "":
            embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                                  description=response)
        else:
            embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                                  description="Returned without response")
        statusmessage=("python eval")
        embed.set_author(name=statusmessage,
                         icon_url="https://github.com/electric-blue-green/content/blob/master/shellbot.png?raw=true")
        embed.set_footer(text="a bot by ash#0001")
        await ctx.channel.send(embed=embed)

@bot.command()
async def shell(ctx):
    if int(ctx.author.id) == 173498062260404225:
        content=str(ctx.message.content)
        command=content.split("$shell")
        status, output = subprocess.getstatusoutput(command[1])
        if output != "":
            embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                                  description=output)
        else:
            embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                                  description="Returned without response")
        statusmessage=("status: " + str(status))
        embed.set_author(name=statusmessage,
                         icon_url="https://github.com/electric-blue-green/content/blob/master/shellbot.png?raw=true")
        embed.set_footer(text="a bot by ash#0001")
        await ctx.channel.send(embed=embed)

@bot.command()
async def pullafk(ctx):
    if int(ctx.author.id) == 173498062260404225:
        content=str(ctx.message.content)
        command=content.split("$shell")
        subprocess.Popen("cd && cd afk && git pull && cd && cd afk && python3 bot.py", shell=True)
        embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                              description="Started dotslashafk")
        embed.set_author(name="restarting dotslashafk",
                         icon_url="https://github.com/electric-blue-green/content/blob/master/shellbot.png?raw=true")
        embed.set_footer(text="a bot by ash#0001")
        await ctx.channel.send(embed=embed)

@bot.command()
async def startafk(ctx):
    if int(ctx.author.id) == 173498062260404225:
        content=str(ctx.message.content)
        command=content.split("$shell")
        subprocess.Popen("cd && cd afk && python3 bot.py", shell=True)
        embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                              description="Started dotslashafk")
        embed.set_author(name="restarting dotslashafk",
                         icon_url="https://github.com/electric-blue-green/content/blob/master/shellbot.png?raw=true")
        embed.set_footer(text="a bot by ash#0001")
        await ctx.channel.send(embed=embed)

@bot.command()
async def killafk(ctx):
    if int(ctx.author.id) == 173498062260404225:
        content = str(ctx.message.content)
        command = content.split("$shell")
        subprocess.Popen.kill()
        embed = discord.Embed(colour=discord.Colour(0x4eb2fa),
                              description="Killed dotslashafk")
        embed.set_author(name="killing dotslashafk",
                         icon_url="https://github.com/electric-blue-green/content/blob/master/shellbot.png?raw=true")
        embed.set_footer(text="a bot by ash#0001")
        await ctx.channel.send(embed=embed)


@bot.command()
async def hello(ctx):
    await ctx.channel.send("oh hi")

@bot.command()
async def py(self, ctx, *, body: str):
    """Evaluates a code"""

    env = {
        'bot': self.bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': self._last_result
    }

    env.update(globals())
    if int(author.id) == 173498062260404225:
        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    else:
        await ctx.send("no thanks")


bot.run(token)
