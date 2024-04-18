import discord
from discord.ext import commands, tasks
import subprocess

channel = 1230221396118868008
channel2 = 1230467965523066962
log_channel_id = 1230468506588418150
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

def run_local_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@bot.command()
async def ssh(ctx, *, command):
    if ctx.channel.id != channel and ctx.channel.id != channel2:
        return
    if ctx.channel.id == channel or ctx.channel.id == channel2:
        output = run_local_command(command)
        await ctx.send(f'```{output}```')

@bot.event
async def on_ready():
    print("Bot is ready!")

if __name__ == "__main__":
    token = input("Enter your bot token: ")
    bot.run(token)
