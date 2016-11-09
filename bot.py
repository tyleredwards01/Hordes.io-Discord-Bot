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
def serverActivity(msgTime):
  if msgTime == 0:
    clock0 = clock0 + 1
  elif msgTime == 1:
    clock1 = clock1 + 1
  elif msgTime == 2:
    clock2 = clock2 +1
  elif msgTime == 3:
    clock3 = clock3 + 1
  elif msgTime == 4:
    clock4 = clock4 + 1
  elif msgTime == 5:
    clock5 = clock5 + 1
  elif msgTime == 6:
    clock6 = clock6 + 1
  elif msgTime == 7:
    clock7 = clock7 + 1
  elif msgTime == 8:
    clock8 = clock8 + 1
  elif msgTime == 9:
    clock9 = clock9 + 1
  elif msgTime == 10:
    clock10 = clock10 + 1
  elif msgTime == 11:
    clock11 = clock11 + 1
  elif msgTime == 12:
    clock12 = clock12 + 1
  elif msgTime == 13:
    clock13 = clock13 + 1
  elif msgTime == 14:
    clock14 = clock14 + 1
  elif msgTime == 15:
    clock15 = clock15 + 1
  elif msgTime == 16:
    clock16 = clock16 + 1
  elif msgTime == 17:
    clock17 = clock17 + 1
  elif msgTime == 18:
    clock18 = clock18 + 1
  elif msgTime == 19:
    clock19 = clock19 + 1
  elif msgTime == 20:
    clock20 = clock20 + 1
  elif msgTime == 21:
    clock21 = clock21 + 1
  elif msgTime == 22:
    clock22 = clock22 + 1
  elif msgTime == 23:
    clock23 = clock23 + 1
    
def on_message(message):
  UID = message.author.id
  auth = message.author
  mes = message.content
  c = message.channel
  #Ping command, I plan on replacing this using discord timestamps eventually.
  msgTime = time.strftime("%H")
  serverActivity(msgTime)

  if message.content.upper() == '$PING':
    if UID in badlist:
        pass
    else:
      t1 = time.clock()
      msg = yield from client.send_message(c, '`PONG`')
      t2 = time.clock()
#<<<<<<< HEAD
      y = str(t2-t1)
      yield from client.edit_message(msg, '`PONG`' +  y[2: 4] + 'ms`')
#=======
      y = str(t2-t1)
      yield from client.edit_message(msg, 'PONG `' +  y[2: 5] + 'ms`')
#>>>>>>> ffeeee1a51d633b6473dcc18d9ba3ffa49c1f209


  if message.content.upper() == '$RESTART':
    if UID in adlist:
      os.system('start /min restart.py')
      sys.exit(0)


  if message.content.upper() == '$ISADMIN':
    if UID in adlist:
#<<<<<<< HEAD
      yield from client.send_message(c, '`Yes, you are a bot admin.`')
<<<<<<< HEAD
#=======
#>>>>>>> ffeeee1a51d633b6473dcc18d9ba3ffa49c1f209
=======
=======
>>>>>>> ffeeee1a51d633b6473dcc18d9ba3ffa49c1f209
>>>>>>> b65a7c0fb824b43c8f85349ba1eb1d719a07e958
    else:
      if UID in badlist:
        pass
      else:
        yield from client.send_message(c, '`No, you do not have access to all bot commands. If you think this is a mistake please contact <@190313064367652864>`')

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
      yield from client.send_message(c, '`HordesBot was created by BlazingFire007 and LegusX.`')

  if message.content.upper() == '$HELP':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`HORDESBOT HELP: \nEveryone:\n$INFO - Gives info about HordesBot. \n$ISADMIN - Tells you if you have admin privelages.\n$PING - Returns with "PONG". Used to ensure HordesBot is running.\nADMIN PRIVELAGES:\n$RESTART - Restarts the bot.\n$STOP - Stops HordesBot`')

  if message.content.upper() == '$LEADERBOARD':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`Sorry, but this command has not yet been fully implemented.`')

  if message.content.upper() == '$VERSION':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`HordesBot version 0.1`')

  if message.content.startswith('$ANNOY_'):
    if UID in badlist:
      pass
    else:
      annoying = False
      annoyed = 0
      while annoying == False:
        yield from client.send_message(auth, message.content.strip('$ANNOY_')+'!!')
        annoyed = annoyed+1
        if annoyed > 10:
          annoying = True
#Replace TOKEN with the actual token.
client.run('MjQzMTIwMTM3MDEwNDEzNTY4.CwIghQ.zZb1swqmPslGo66QFn3-D0opXBM')
