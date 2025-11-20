import discord
from discord.ext import commands
from deep_translator import GoogleTranslator
import os
from dotenv import load_dotenv

# Carregar .env
load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None or TOKEN == "":
    raise ValueError("❌ ERRO: TOKEN não foi encontrado no .env")


# ID do canal onde o bot vai traduzir automaticamente
CANAL_TRADUCAO = 1440515390072557618  # substitua se precisar

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


@bot.event
async def on_message(message):
    # Ignorar mensagens do próprio bot
    if message.author.bot:
        return

    # Traduz apenas no canal configurado
    if message.channel.id == CANAL_TRADUCAO:
        texto = message.content

        try:
            traducao_pt = GoogleTranslator(source="auto", target="pt").translate(texto)
            traducao_en = GoogleTranslator(source="auto", target="en").translate(texto)
            traducao_ru = GoogleTranslator(source="auto", target="ru").translate(texto)

            resposta = (
                f"🇧🇷 **PT:** {traducao_pt}\n"
                f"🇺🇸 **EN:** {traducao_en}\n"
                f"🇷🇺 **RU:** {traducao_ru}"
            )

            await message.channel.send(resposta)

        except Exception as e:
            print("Erro na tradução:", e)

    # Necessário para comandos funcionarem
    await bot.process_commands(message)


# Iniciar o bot
bot.run(TOKEN)
