import discord
import leetcode


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN: 'MTA4OTIxMjc1NjU0NjMwNjE3OQ.GRPSkH.adAHg-WxTFUC2DUKOZ0e3sq6XXmrJjCjwdHhwk'
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f'{client.user} us no running!')
        
    @client.event
    async def on_message():
        if message.author == client.user:
            return 
        
        
        
    client.run(TOKEN)