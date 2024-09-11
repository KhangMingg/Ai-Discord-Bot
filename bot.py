import discord
from discord.ext import commands
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API = os.getenv('GEMINI_API')
BOT_API = os.getenv('BOT_API')


bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

client = discord.Client(intents = discord.Intents.all())

genai.configure (api_key=GEMINI_API)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel('gemini-pro',
	safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    }
	]
	)


@bot.event
async def on_ready():
	print(f"Logged in as: {bot.user.name}!")
     

@bot.command(name = "usage")
async def usage(ctx):
    msg = f'**Bot usage:**  !info  `<@username>`,   !ai  `<ask_me_anything>`,   !roles  `<@username>`'
    await ctx.send(msg)


@bot.command(name = "ai")
async def ai(ctx: commands.Context, *, prompt: str):
	response = model.generate_content(prompt)

	await ctx.reply(response.text)
	

@ai.error      
async def ai_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('**correct use:** `!gen <ask smth more than 5 characters>`')

	
@bot.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)} roles.'
    await ctx.send(msg)


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))


@roles.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


bot.run(BOT_API)