import discord
from discord.ext import commands

# Configura el token de tu bot
TOKEN = 'yourtoken' 

# Configura el ID del canal de texto donde quieres aplicar la restricción
CANAL_ID = 0  # Reemplaza esto con el ID de tu canal de texto

# Inicializa el bot y establece el prefijo de los comandos
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Diccionario para rastrear los usuarios que ya han enviado un mensaje en el canal
usuarios_mensajes_enviados = {}

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == CANAL_ID:
        author_id = message.author.id
        if author_id not in usuarios_mensajes_enviados:
            usuarios_mensajes_enviados[author_id] = True
        else:
            await message.delete()
            await message.author.send("Solo se permite enviar un mensaje en este canal.")
    await bot.process_commands(message)

bot.run(TOKEN)

