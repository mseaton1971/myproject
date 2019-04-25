#sish.py by Marlon Seaton
import sys
import os
 
#*Produce error messages for system call failures and other errors

def ErrorMessage(msg):

  print msg
  sys.exit(0);


line = raw_input("sish$ ")

while(line != "exit"):
  
  #Parse the line into tokens with white space as the delimiter
    
  tokens = line.split()
 
  if(os.fork() < 0):
    ErrorMessage("Forked failed");
  
  elif os.fork() == 0:
    os.execvp(tokens[0],tokens)

  else:
    print "in parent"
  
  line = raw_input("sish$ ")

  
