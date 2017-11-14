import subprocess
import os


import sys

print (sys.argv)

print ("Type of argv 1 ", type(sys.argv[1]))

print ("Sum is ", sys.argv[1] + sys.argv[2])
print ("Sum is ", int(sys.argv[1]) + int (sys.argv[2]))

sys.exit(0)
filename = 'ravi1'
bs = 14
count = 1
#cmd = 'dd if=/dev/urandom of=\$filename bs=\$bs count=\$count'
print ("filename is %s" % filename)
arg1="of=" + filename
arg2="if=/dev/urandom"
arg3="bs="+str(bs) + "M"
arg4="count=" + str(count) 
#command = subprocess.call(['dd', 'if=/dev/urandom', 'of=filename', 'bs=1M', 'count=19'])
command = subprocess.call(['dd', arg1, arg2, arg3, arg4])

