#! /usr/bin/python3
# This module will establish a SSH connection to target box and fetch the file system info 

import paramiko
import sys
import subprocess 
import os
import json 
import pprint
from tabulate import tabulate 

my_name = 'Python'

print ("Let's talk about %s." % my_name + "\n")

print("Entered data is: " + str(sys.argv) + "\n")

host = sys.argv[1]
user = sys.argv[2]
pwd  = sys.argv[3]
command = sys.argv[4]


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=pwd)

print('Running remote command DF on %s' % host + "\n")

stdin, stdout, stderr = ssh.exec_command(command)
stdin.close()

json_output = stdout.read()

print("---------------Writing to log.txt------------\n")
logfile = open('Log.txt','wb')
logfile.write(json_output)
logfile.close()

print("--------------Normal print------------------\n")
print(json_output)

#print("-------------PPrinting JSON Object------------\n")
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(json_output)
print("\n")

#print("------------Tabulate Json Object-------------\n") 
#print tabulate(json_output, showindex="always",tablefmt="html")

print ("Result of '%s' command on '%s' host" % (command, host) + "\n")
for line in stdout.read().splitlines():
    print('%s ' % ( str(line) + "\n"))

#for line in stderr.read().splitlines():
#    print('%s %s' % (host, str(line) + "\n"))

#########################################################################
f = open('Log.txt')
lines = (line.strip() for line in f.readlines())
f.close()    
splittedLines = (line.split() for line in lines)

listOfColumnData = zip(*splittedLines)
#print("List of Column Data %s :" % listOfColumnData)

#for eachColumn in listOfColumnData:
#print(eachColumn)
#print(type(eachColumn))

'''
input1 = raw_input("Enter the mounted on name to know usuage for? : ")
j = 0
k = 0
length = len(listOfColumnData) + 2
elts_dict = {}
while( j <= length ):
  elts = [x[j] for x in listOfColumnData]
  if input1 in elts:
     print("Parsed Element %s " % elts)
     #print ("Type of Parsed Element %s " % type(elts) + '\n')
     elts_dict = dict( (j, elts[j]) for j in range(len(elts))  )
     print("Dictionary %s " % elts_dict)
  j += 1
'''


input2 = raw_input("Enter the mounted file system to know the details for ? ")
input3 = raw_input("Enter the field to know about ? ")

j = 0
k = 0
length = len(listOfColumnData) + 2
elts_dict = {}
while( j <= length ):
  elts = [x[j] for x in listOfColumnData]
  if input2 in elts:
    #print("File system to know details of %s " % elts)
    elts_dict = dict( (j, elts[j]) for j in range(len(elts))  )
    #print("Dictionary %s " % elts_dict)
    print('\n')
    if input3 == '%':
       print(elts_dict[4])
       break
    if input3 == 'Available':
       print(elts_dict[3])
       break
    if input3 == 'Filesystem':
       print(elts_dict[0])
       break
    if input3 == 'blocks':
       print(elts_dict[1])
       break
    if input3 == 'Used':
       print(elts_dict[2])
       break 
    else:
       print(elts_dict) 
  j += 1

length1 = len(elts_dict)
#print("Length of dictionary %s" % length1)
 


#############preparing full dictionary######################




'''
 length = len(eachColumn)
   i = 0 
   while (i < length):
      print(eachColumn[i])
      i += 1 
else:
  print('Exit')

'''

ssh.close()

print('connection to %s closed' %  host)


# Milestone 1:

# Explore all the functionalities of paramiko, json, df, dict, list, user input, tuple, sphinx.

# Milestone 2:

# Convert to proper functions. Code cleanup. Do not delete any code. Just move it to the end of the file.
# User argparse module for command line parsing.
# Write proper documentation for the functions
# Run pylint tool on the code. Make sure the score is above 8 atleast. Try not to repeat the mistakes in further code you write.


# Milestone 3:
# Error handling.
# Convert it into a dictionary of dictionray. The user should be able to access the file system stat using two dictionary lookups.
# Show the df output in a table using tabulate

# Milestone 4:
# Display the graph.
