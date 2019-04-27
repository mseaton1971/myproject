#sish.py by Marlon Seaton
import sys
import os
import errno
 
#Produce error messages for system call failures and other errors

def ErrorMessage(msg):

  print msg
  sys.exit(0);

#This Method supports a few built-in functions if requested by the user
def Builtins(tokens):

  isbuiltin = False
  
  if(tokens[0] == "exit"):
     isbuiltin = True
     sys.exit()

  elif(tokens[0] == "cd"):
     
    if(len(tokens) == 1):
    
      try: 
        os.chdir('/home') 
        isbuiltin = True
        
      except OSError as e: 
        ErrorMessage(e.strerror)
    
    else:


    
      try:
        os.chdir(tokens[1])
        isbuiltin = True

      except OSError as e:        
        ErrorMessage(e.strerror) 
   
    return isbuiltin
  

#Method defined to execute basic common unix commands
def Execute():

  line = raw_input("sish$ ")
  
  isbuiltin = False
 
  while(True):
  
    line = raw_input("sish$ ")
    #Parse the line into tokens with white space as the delimiter
    
    tokens = line.split()

    #Check for built-ins first
    if(Builtins(tokens)):
       continue
    
    else:
    
       try:
         pid = os.fork()
       except OSError as e:
         print e.strerror   

       if pid == 0:    
         try:
           os.execvp(tokens[0],tokens)
         except OSError as e:
           print e.strerror
       
       else:
         os.waitpid(0,0)
  
 #   line = raw_input("sish$ ")

# Program execution begins here


print("\n\n\t*********MY SHELL*********")
 
Execute()  
