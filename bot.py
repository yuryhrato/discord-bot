import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.listen("on_message")
async def auto_translate(message):
    if message.author.bot:
        return

    text = message.content

    try:
        traducoes = {
            "pt": GoogleTranslator(source="auto", target="pt").translate(text),
            "en": GoogleTranslator(source="auto", target="en").translate(text),
            "ru": GoogleTranslator(source="auto", target="ru").translate(text),
        }

        resposta = (
            f"🇧🇷 **PT:** {traducoes['pt']}\n"
            f"🇺🇸 **EN:** {traducoes['en']}\n"
            f"🇷🇺 **RU:** {traducoes['ru']}"
        )

        await message.channel.send(resposta)

    except Exception as e:
        print("Erro:", e)

bot.run(TOKEN)
