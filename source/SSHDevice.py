# This module will establish a SSH connection to target box and fetch the file system info 

import paramiko
import sys
import subprocess 
import os
import json 

my_name = 'Python'

print ("Let's talk about %s." % my_name + "\n")

print("Entered data is: " + str(sys.argv) + "\n")

host = sys.argv[1]
user = sys.argv[2]
pwd = sys.argv[3]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=pwd)


print('Running remote command DF on %s' % host + "\n")

stdin, stdout, stderr = ssh.exec_command('df')
stdin.close()

json_output = stdout.read()

print("---------------Writing to log.txt------------\n")
_logfile = open('Log.txt','wb')
_logfile.write(json_output)
_logfile.close()



print("-------------Printing JSON Object------------\n")
print(json_output)


#for line in stdout.read().splitlines():
# print('%s %s' % (host, str(line) + "\n"))

for line in stderr.read().splitlines():
    print('%s %s' % (host, str(line) + "\n"))

ssh.close()

print('connection to %s closed' %  host)


