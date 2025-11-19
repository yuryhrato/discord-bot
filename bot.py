import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

CANAL_TRADUCAO = 1440515390072557618  # coloque aqui o ID do canal que deve traduzir

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

    # se estiver fora do canal escolhido, ignora
    if message.channel.id != CANAL_TRADUCAO:
        return

    texto = message.content

    try:
        traducoes = {
            "pt": GoogleTranslator(source="auto", target="pt").translate(texto),
            "en": GoogleTranslator(source="auto", target="en").translate(texto),
            "ru": GoogleTranslator(source="auto", target="ru").translate(texto)
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
