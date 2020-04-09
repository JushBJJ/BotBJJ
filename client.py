import discord
import colorama
import time

client=discord.Client()
token="haha yes"

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")

@client.event
async def on_message(message):
    msg=str(message.content)
    author=str(message.author)
    channel=message.channel

    if author==client.user:
        return
    
    if author=="Jush#8735":
        if msg==">stop":
            complete_stop=True

            await channel.send("Stopping...")
            await client.close()
    
    if msg.startswith(">"):
        for i in message.author.roles:
            if 616024832475398193 == i.id:
                msg=msg[msg.find(">")+1:]
                await admin(msg, channel)
            
    #print(message.author.roles)

async def cmd_say(msg, channel):
    await channel.send(msg)

async def admin(msg, channel):
    admin_commands={"say":cmd_say}

    if msg.split(" ")[0] in admin_commands.keys():
        await admin_commands[msg.split(" ")[0]](msg, channel)

def main():
    client.run(token)

if __name__=="__main__":
    main()