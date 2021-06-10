import socket
import os
import time
import subprocess

REMOTE_SERVER = "portal.acttv.in"
def is_connected():
  
  try:
    print("Checking....")
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    os.startfile("J:Home8d.mp3")
    print("Connected to Network")
  except:
     time.sleep(60)
     print("Internet Connection Unavailable")
     is_connected()

is_connected()
