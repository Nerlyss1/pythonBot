import discord
from discord.ext import commands
from commandhisto import CommandHistory
from tree import Conversation

intents = discord.Intents.all()
history = CommandHistory()
conversation = Conversation()

client = commands.Bot(command_prefix="!", intents=intents)

@client.command(name="history")
async def display_history(ctx):
    all_commands = history.get_all_commands()
    for command in all_commands:
        await ctx.send(command)

@client.command(name="clear_history")
async def clear_history(ctx):
    history.clear()
    await ctx.send("L'historique des commandes a été effacé.")

@client.command(name="reset_conversation")
async def reset_conversation(ctx):
    conversation.reset()
    await ctx.send("La conversation a été réinitialisée.")

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1091337387294068788) # Remplacer 1234567890 par l'ID du canal général
    await general_channel.send("Bienvenue sur le serveur, {} !".format(member.mention))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "help":
        await message.channel.send("Bienvenue dans la conversation. Je vais essayer de déterminer votre besoin.")
        conversation.reset()
    elif message.content.lower().startswith("speak about"):
        topic = message.content[11:].strip()
        response = conversation.speak_about(topic)
        await message.channel.send(response)
    else:
        response = conversation.respond(message.content)
        if conversation.current_node.yes_node is None and conversation.current_node.no_node is None:
            await message.channel.send(conversation.current_node.question)
        else:
            await message.channel.send(response)

    history.add_command(message.content)
    await client.process_commands(message)
    

    
client.run("Code_bot")
