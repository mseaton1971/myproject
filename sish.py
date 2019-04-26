#sish.py by Marlon Seaton
import sys
import os
import errno
 
#Method defined to produce error messages for system call failures and other errors

def ErrorMessage(msg):

  print msg
  sys.exit(0);

#Method defined to execute basic common unix commands
def Execute():

  line = raw_input("sish$ ")

  while(line != "exit"):
  
    #Parse the line into tokens with white space as the delimiter
    
    tokens = line.split()
  
    try:
      pid = os.fork()
 
    except OSError as e:
      ErrorMessage(e.strerror)  

    if pid == 0:
    
      try:      
        os.execvp(tokens[0],tokens)
     
      except OSError as e:
	ErrorMessage(e.strerror)
  
    else:
      os.waitpid(0,0)
  
    line = raw_input("sish$ ")

# Program execution begins here
Execute()
