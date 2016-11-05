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
adlist = ['190313064367652864', '227376221351182337', '104680633518821376', '117993898537779207']
#List of users who cannot use the bot (Use the USER IDS)
badlist = []
txt = open('badlist.txt', 'r')
badlist = txt.read().split(', ')

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
      os.system('start /min restart.py')
      sys.exit(0)


  if message.content.upper() == '$ISADMIN':
    if UID in adlist:
      yield from client.send_message(c, "Yes, you're a bot admin.")
    else:
      if UID in badlist:
        pass
      else:
        yield from client.send_message(c, 'No, you do not have access to all bot commands. If you think this is a mistake please contact <@190313064367652864>')

  if message.content.upper().startswith('$BLIST'):
    if UID in adlist:
      mes = mes.split(' ')
      if len(mes) == 1:
        yield from client.send_message(auth, badlist)
      else:
        if mes[1].upper() == 'ADD':
          badlist.append(mes[2])
          txt = open('badlist.txt', 'a')
          txt.write(str(mes[2]) + ', ')
          txt.close()
          yield from client.send_message(c, 'Added <@' + mes[2] + '> to the blacklist.')
        if mes[1].upper() == 'REM':
          badlist.remove(mes[2])
          delthis = [str(mes[2]) + ', ']
          lst = []
          txt = open('badlist.txt', 'r')
          for line in txt:
            for word in delthis:
              if word in line:
                line = line.replace(word, '')
            lst.append(line)
          txt.close()
          txt = open('badlist.txt', 'w')
          for line in lst:
            txt.write(line)
          txt.close()
          yield from client.send_message(c, 'Removed <@' + mes[2] + '> from the blacklist.')

  if message.content.upper() == '$INFO':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, 'HordesBot was created by BlazingFire007 and LegusX.')

  if message.content.upper() == '$HELP':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`HORDESBOT HELP: \nEveryone:\n$INFO - Gives info about HordesBot. \n$ISADMIN - Tells you if you have admin privelages.\n$PING - Returns with "PONG". Used to ensure HordesBot is running.\nADMIN PRIVELAGES:\n$RESTART - Restarts the bot.\n$STOP - Stops HordesBot`')
  
  if message.content.upper() == '$LEADERBOARD':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, 'Sorry, but this command has not yet been fully implemented.')
      
  if message.content.upper() == '$VERSION':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, 'HordesBot version 0.1')
      
#Replace TOKEN with the actual token.
client.run(token)
