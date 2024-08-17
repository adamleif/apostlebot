import tokens
BOT_TOKEN = tokens.bot_token
import discord
from discord.ext import commands
from responses import get_response

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=">", intents=intents)

@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")


@client.event
async def on_message(message) -> None:
    if message.author == client.user: return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: '{user_message}'")
    # await send_message(message, user_message)

def main() -> None:
    client.run(token=BOT_TOKEN)

if __name__ == "__main__":
    main()

# DEPRECATED:
# async def send_message(message, user_message: str) -> None:
#     if not user_message:
#         print("Message is empty because intents weren't enabled probably. Or something")
#         return
    
#     # okay walrus operator go off
#     if is_private := user_message[0] == "?":
#         user_message = user_message[1:]

#     try:
#         response: str = get_response(user_message)
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)