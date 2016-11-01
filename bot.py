import discord, asyncio, os, sys, time, json
client = discord.Client()

#Executes when bot starts up.

@client.event
@asyncio.coroutine
def on_ready():
  print('Connected!')
  print('Username: ' + client.user.name)
  print('User ID: ' + client.user.id)
  
#Adminlist (Use the USER IDS)
adlist = []
#List of users who cannot use the bot (Use the USER IDS)
badlist = []

@client.event
@asyncio.coroutine
def on_message(message):
  UID = message.author.id
  auth = message.author
  mes = message.content
  c = message.channel
  #Ping command, I plan on replacing this using discord timestamps eventually.
  if message.content.upper() == '$PING':
    t1 = time.clock()
    msg = yield from message.send_message(c, 'PONG')
    t2 = time.clock()
    y = t2-t1
    yield from message.edit_message(msg, 'PONG `' +  y[2: 4] + 'ms`')
    
#Replace TOKEN with the actual token.    
client.run(TOKEN)
