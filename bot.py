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
adlist = ['190313064367652864', '227376221351182337']
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
    if UID in badlist:
        pass
    else:
      t1 = time.clock()
      msg = yield from client.send_message(c, 'PONG')
      t2 = time.clock()
      y = str(t2-t1)
      yield from client.edit_message(msg, 'PONG `' +  y[2: 5] + 'ms`')


  if message.content.upper() == '$RESTART':
    if UID in adlist:
      yield from client.send_message(c, 'Restarting...')
      os.system('start /min restart.py')
      sys.exit()


  if message.content.upper() == '$ISADMIN':
    if UID in adlist:
      yield from client.send_message(c, 'Yes, you are a bot admin.')
    else:
      if UID in badlist:
        pass
      else:
        yield from client.send_message(c, 'No, you do not have access to all bot commands. If you think this is a mistake please contact <@190313064367652864>')

  if message.content.upper().startswith('$BLIST'):
    if UID in adlist:
      mes = mes.split(' ')
      print(len(mes))
      if len(mes) == 1:
        yield from client.send_message(auth, badlist)
      else:
        if mes[1].upper() == 'ADD':
          badlist.append(mes[2])
          yield from client.send_message(c, '<@' + mes[2] + '> added to the blacklist.')
        if mes[1].upper() == 'REM':
          badlist.remove(mes[2])
          yield from client.send_message(c, '<@' + mes[2] + '> removed from the blacklist.')

  if message.content.upper() == '$INFO':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, 'HordesBot was created by BlazingFire007 and LegusX.')

  if message.content.upper() == '$HELP':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`HORDESBOT HELP: \nEveryone:\n$INFO - Gives info about HordesBot. \n$ISADMIN - Tells you if you have admin privelages.\n$PING - Returns with "PONG". Used to ensure HordesBot is running.')
  if message.content.upper() == '$STOP':
    if UID in adlist:
      sys.exit()
#Replace TOKEN with the actual token.
client.run("MjQzMTIwMTM3MDEwNDEzNTY4.CvqzgQ.F_LYyrZj3h10eW20poqWdsxL1Vc")
