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
    if UID in badlistt:
        pass
    else:
      t1 = time.clock()
      msg = yield from message.send_message(c, 'PONG')
      t2 = time.clock()
      y = t2-t1
      yield from message.edit_message(msg, 'PONG `' +  y[2: 4] + 'ms`')
      
      
  if message.content.upper() == '$RESTART':
    if UID in adlist:
      os.system('start restart.py')
      sys.exit(0)
      
      
  if message.content.upper() == '$ISADMIN':
    if UID in adlist:
      yield from client.send_message(c, 'Yes, you are a bot admin.')
    else:
      if UID in badlist:
        pass
      else:
        yield from client.send_message(c, 'No, you do not have access to all bot commands. If you think this is a mistake please contact <@190313064367652864>')

  if message.content.startswith('$BLIST')
    mes = message.content
    if UID in badlist:
      pass
    else:
      if UID in adlist:
        mes.split(' ')
        if len(mes) < 1:
          yield from client.send_message(authr, str(badlist))
        else:
          if message.content.upper().startswith('$BLIST ADD'):
            badlist.append(mes[2])
          if message.content.upper().startswith('$BLIST REMOVE'):
            badlist.remove(mes[2])
          else:
            yield from client.send_message(c, 'Invalid Command')
#Replace TOKEN with the actual token.    
client.run(TOKEN)
