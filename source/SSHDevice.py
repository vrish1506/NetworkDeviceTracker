#! /usr/bin/python3

""" This module will establish a SSH connection to target box and fetch the file system info """

import sys
import paramiko
def connecttotargetmachine():
    """This functions connects to target machine."""
    print("Entered data is: " + str(sys.argv) + "\n")
    _host_ = sys.argv[1]
    _user_ = sys.argv[2]
    _pwd_ = sys.argv[3]
    _command_ = sys.argv[4]
    _ssh_ = paramiko.SSHClient()
    _ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    _ssh_.connect(_host_, username=_user_, password=_pwd_)
    executecommandontargetbox(_ssh_, _host_, _command_)
    return

def executecommandontargetbox(_ssh_, _host_, _command_):
    """This functions executes the command on the target machine."""
    print('Running remote command DF on %s' % _host_ + "\n")
    stdin, stdout = _ssh_.exec_command(_command_)
    print("Result of '%s' command on '%s' host" % (_command_, _host_) + "\n")
    writetojsonandfile(_ssh_, _host_, stdout)
    for line in stdout.read().splitlines():
        print('%s' % (str(line) + "\n"))
    stdin.close()
    return

def writetojsonandfile(_ssh_, _host_, stdout):
    """This function writes the console output to Json object and writes to log file"""
    _json_output = stdout.read()
    print("---------------Writing to log.txt------------\n")
    _logfile_ = open('Log.txt', 'wb')
    _logfile_.write(_json_output)
    _logfile_.close()
    parseandstoreoutputindictionary(_host_, _ssh_)
    return

def printoutputonconsole(stdout):
    """This function prints the output on console from console and Json object"""
    print("--------------Normal print------------------")
    for line in stdout.read().splitlines():
        print('%s' % (str(line) + "\n"))
    return

def parseandstoreoutputindictionary(_host_, _ssh_):
    """This function reads the log file and stores the output in dictionary using loop """
    _logfile_ = open('Log.txt', 'r')
    _lines_ = (line.strip() for line in _logfile_.readlines())
    _logfile_.close()
    _splittedlines_ = (line.split() for line in _lines_)
    _listofcolumndata_ = zip(*_splittedlines_)
    _input2_ = input("Enter the mounted file system to know the details for ? ")
    j = 0
    _length_ = len(_listofcolumndata_)+2
    print("Length of List Of Column Data %s" % _length_)
    elts_dict = {}
    while j <= _length_:
        elts = (x[j] for x in _listofcolumndata_)
        if _input2_ in elts:
            print("File system to know details of %s " % elts)
            _input3_ = input("Enter the field to know about ?")
            elts_dict = dict((j, elts[j]) for j in range(len(elts)))
            print("Dictionary %s " % elts_dict)
            print('\n')
            if _input3_ == '%':
                print(elts_dict[4])
                break
            if _input3_ == 'Available':
                print(elts_dict[3])
                break
            if _input3_ == 'Filesystem':
                print(elts_dict[0])
                break
            if _input3_ == 'blocks':
                print(elts_dict[1])
                break
            if _input3_ == 'Used':
                print(elts_dict[2])
                break
            else:
                print("No Input for field, printing complete details %s :" % elts_dict)
    j += 1
    closeconnectiontotargetmachine(_host_, _ssh_)
    return

def closeconnectiontotargetmachine(_host_, _ssh_):
    """ This function closes the connection to target machine """
    _ssh_.close()
    print('connection to %s closed' %  _host_)
    return

connecttotargetmachine()

    ############Review Comments#################
    #### Milestone 1:
    # Explore all the functionalities of paramiko, json, df, dict, list, user input, tuple, sphinx.
    #### Milestone 2:
    # Convert to proper functions. Code cleanup. Do not delete any code.
    # Just move it to the end of the file.
    # User argparse module for command line parsing.
    # Write proper documentation for the functions
    # Run pylint tool on the code. Make sure the score is above 8 atleast.
    # Try not to repeat the mistakes in further code you write.
    ####  Milestone 3:
    # Error handling.
    # Convert it into a dictionary of dictionray.
    # The user should be able to access the file system stat using two dictionary lookups.
    # Show the df output in a table using tabulate
    #### Milestone 4:
    # Display the graph.
    ###############Unused Code#################
"""
for line in stderr.read().splitlines():
    print('%s %s' % (host, str(line) + "\n"))
print("-------------PPrinting JSON Object------------\n")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json_output)
print("\n")
print("------------Tabulate Json Object-------------\n")
print tabulate(json_output, showindex="always",tablefmt="html")
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

print("List of Column Data %s :" % listOfColumnData)
for eachColumn in listOfColumnData:
print(eachColumn)
print(type(eachColumn))
length1 = len(elts_dict)
print("Length of dictionary %s" % length1)
p"""
