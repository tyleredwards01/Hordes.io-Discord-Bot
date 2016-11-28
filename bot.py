import discord, asyncio, os, sys, time, json, requests
client = discord.Client()

#Message to new members
memberJoin = '''
Hello and welcome to the Hordes.io Discord Server!
First and foremost, we would like to thank you for joining!

In this server we have some general community rules that we believe aren't too demanding:
**1) Don't insult others, in any way, shape or form.**
**2) Please keep chat to it's respected channel.**
**3) If you wish to play music in the music channel, please refrain from playing music with the intent of annoying others.**
**4) Please use bot commands in off-topic only.**
**5) Do not post links to any malicious sites, or any shortened links, i.e. goo.gl or bit.ly**
**6) Spamming in ANY channel is not allowed.**
**7) NSFW content is prohibited in voice chat or text chat, as we do have children among us.**
**8) Please do not advertise. We realize that your YouTube or Twitch may be really great, but it is not allowed here.**
If you fail to follow these rules, a staff member may either give you a warning, or if it is severe enough, can ban you. After being warned, any other rules broken will result in a permanent ban.

If you have any questions, please check out the information channel's FAQ section, or private message one of the staff for assistance.
				
Sincerely, 
		The Hordes.io Team
'''

#Executes when bot starts up.
@client.event
@asyncio.coroutine
def on_ready():
  print('Connected!')
  print('Username: ' + client.user.name)
  print('User ID: ' + client.user.id)

#Adminlist (Use the USER IDS)
adlist = ['190313064367652864', '227376221351182337', '104680633518821376', '117993898537779207', '126288853576318976']
#List of users who cannot use the bot (Use the USER IDS)
badlist = []
txt = open('badlist.txt', 'r')
badlist = txt.read().split(', ')
#Server hourly activity total reading.
activity = open('serveractivity.txt', 'r')
activity_enu = enumerate(activity)
clock_list = []
for i, line in activity_enu:
    clocks_read = 0
    while clocks_read < 24:
        clocks_read = clocks_read + 1
        if i == clocks_read:
            clock_list.append(line)
activity.close()

@client.event
@asyncio.coroutine
def on_message():
  msgTime = time.strftime("%H")
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
  clocks = [clock0, clock1, clock2, clock3, clock4, clock5, clock6, clock7, clock8, clock9, clock10, clock11, clock12, clock13, clock14, clock15, clock16, clock17, clock18, clock19, clock19, clock20, clock21, clock22, clock23]
  activity = open('serveractivity.txt', 'w')
  clocks_written = 1
  activity.write(clock0)
  while clocks_written < 24:
    activity.append(clocks[clocks_written])
    clocks_written = clocks_written + 1
  activity.close()
  
@client.event
@asyncio.coroutine
def on_member_join(member):
	yield from client.send_message(member, memberJoin)
	
@client.event
@asyncio.coroutine
def on_message(message):
  UID = message.author.id
  auth = message.author
  mes = message.content
  c = message.channel
  #Ping command, I plan on replacing this using discord timestamps eventually.
  
  if 'goo.gl/' in mes or 'bit.ly/' in mes:
  	yield from client.delete_message(mes)
  	if auth in warned:
  		yield from client.send_message(auth, "You have been banned due to posting a second shortened link.")
  		client.ban(auth, delete_message_days=1)
  	else:
  		yield from client.send_message(auth, "Your message was detected to contain a shortened link. This is your warning. Do not post another shortened link, as they are not allowed.")
  		warned.append(auth)
  if message.content.upper() == '$PING':
    if UID in badlist:
        pass
    else:
      t1 = time.clock()
      msg = yield from client.send_message(c, '`PONG`')
      t2 = time.clock()
      y = str(t2-t1)
      yield from client.edit_message(msg, '`PONG`' +  y[2: 4] + 'ms`')
      y = str(t2-t1)
      yield from client.edit_message(msg, 'PONG `' +  y[2: 5] + 'ms`')


  if message.content.upper() == '$RESTART':
    if UID in adlist:
      os.system('start /min restart.py')
      sys.exit(0)


  if message.content.upper() == '$ISADMIN':
    if UID in adlist:
      yield from client.send_message(c, '`Yes, you are a bot admin.`')
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
      yield from client.send_message(c, '`HordesBot was created by BlazingFire007 and LegusX. Currernt version: 0.0.1`')

  if message.content.upper() == '$HELP':
    if UID in badlist:
      pass
    else:
      yield from client.send_message(c, '`HORDESBOT HELP: \nEveryone:\n$INFO - Gives info about HordesBot. \n$ISADMIN - Tells you if you have admin privelages.\n$PING - Returns with "PONG". Used to ensure HordesBot is running.\n$VERSION - Gives current HordesBot version.\n$PLAYERS - Displays players currently online on Hordes.io.\nADMIN PRIVELAGES:\n$BLIST ADD/REM - Add/remove people from bot blacklist.\n$RESTART - Restarts the bot.\n$STOP - Stops HordesBot`')

  if message.content.upper() == '$PLAYERS':
    if UID in badlist:
      pass
    else:
      r = requests.get('http://www.hordes.io:9999/api/status')
      data = r.json()
      pyData = json.dumps(data)
      dataStr = json.loads(pyData)
      players = (dataStr['players'])
      yield from client.send_message(c, "`players:`" + str(players))

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
client.run('TOKEN')