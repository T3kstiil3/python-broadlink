#!/usr/bin/python

import broadlink
import time
import sys

str_ip = "192.168.0.36"
str_mac = "34 ea 34 e3 a5 68"

try:
    fileName = sys.argv[1]
except IndexError:
    fileName = 'null'

if fileName == 'null':
   print "Error - no file name parameter suffixed"
   sys.exit()
else:

   device = broadlink.rm(host=(str_ip,80), mac=bytearray.fromhex(str_mac))

print "Connecting to Broadlink device...."
device.auth()
time.sleep(1)
print "Connected...."
time.sleep(1)
device.host

file = open(fileName, 'r')

myhex = file.read()

device.send_data(myhex.decode('hex'))
print "Code Sent...."
