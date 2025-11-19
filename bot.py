import discord
from discord.ext import commands
from googletrans import Translator
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.listen("on_message")
async def auto_translate(message):
    if message.author.bot:
        return

    text = message.content

    try:
        # Detect language
        detected = translator.detect(text).lang

        # Translate to PT / EN / RU
        translations = {
            "pt": translator.translate(text, dest="pt").text,
            "en": translator.translate(text, dest="en").text,
            "ru": translator.translate(text, dest="ru").text
        }

        response = (
            f"🇧🇷 **PT:** {translations['pt']}
"
            f"🇺🇸 **EN:** {translations['en']}
"
            f"🇷🇺 **RU:** {translations['ru']}"
        )

        await message.channel.send(response)

    except Exception as e:
        print("Erro:", e)

bot.run(TOKEN)
