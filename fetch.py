import socket, sys, os, time
#Set host and port
host = 'www.hordes.io'
port = 80

#Define socket and connect.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

#Send Message
message = 'PLACEHOlDER'
try:
    s.send(message.encode())
except as err:
    print('An error has occured\n' + err)

#Receive data
try:
    data = s.recv(2048).decode()
except as err:
    print('An error has occured\n' + err)

#Close Connection
s.close()
