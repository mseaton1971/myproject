#sish.py by Marlon Seaton
import sys
import os
import errno
 
#Produce error messages for system call failures and other errors

def ErrorMessage(msg):

  print msg
  isbuiltin = True
  sys.exit(0)

#This Method supports a few built-in functions if requested by the user
def Builtins(tokens):
  
  isbuiltin = False

  if(tokens[0] == "exit"):
     sys.exit()

  elif(tokens[0] == "cd"):
     
    if(len(tokens) == 1):
    
      try: 
	os.chdir('/home') 
        isbuiltin = True

      except OSError in e: 
        ErrorMessage(e.strerror)
    
    else:
    
      try:
        os.chdir(tokens[1])
	isbuiltin = True
         
      except OSError in e:        
        ErrorMessage(e.strerror)

  return isbuiltin 


#Method defined to execute basic common unix commands
def Execute():

  while(True):
  
    #Parse the line into tokens with white space as the delimiter

    isbuiltin = False

    line = raw_input("sish$ ")

    # Check for redirection commands
    Redirection(line)

    tokens = line.split()

    if(Builtins(tokens)):
       continue
    else:

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

#Method used to implement Redirection
def Redirection(line):
 
   infile = False
   outfile = False
   appendfile = False

   #parse the string line using "<, >, or <<" as the delimiter

   if(line.find("<") != -1):
         tokens = line.split("<")
   elif(line.find(">") != -1):
         tokens = line.split(">")
   elif(line.find(">>") != -1):
         tokens = line.split(">>")
   else:
      return
   
   for i in range(len(tokens)):
      tokens[i] == tokens[i].strip()

   try:
     pid = os.fork()
   except OSError as e:
     ErrorMessage(e.strerror)  
   
   if pid == 0:

      for i in range(len(tokens)):

        if(tokens[i] == ">"):
            outfile = True
	 
        if(tokens[i] == "<"):
	    infile = True

	if(tokens[i] == ">>"):
	    appendfile = True

        #Redirect output to a file
        if(outfile):
		
	    os.close(sys.stdout.fileno())
            
            try:
	      fdout = os.open(outfile, os.O_WRONLY | os.O_CREAT | os.O_TRUNC,0644)
	    except OSError as e:
	       ErrorMessage(e.strerror)
    
	    try:
	      newfdout = os.dup2(fdout,sys.stdout.fileno())
	    except OSError as e:
	       ErrorMessage(e.strerror)

	    os.close(fdout)

	elif(infile):
	
	   os.close(sys.stdin.fileno());
	   
	   try:
	     fdin = os.open(infile, os.O_RDONLY)
	   except OSError as e:
	      ErrorMessage(e.strerror)
           
	   try:
	     newfdin = os.dup2(fdin,sys.stdin.fileno())
	   except OSError as e:
	      ErrorMessage(e.strerror)

	   os.close(fdin)
	
	elif(appendfile):
	
	   os.close(sys.stdout.fileno())
	   
	   try:
	     os.open(appendfile, os.O_WRONLY | os.O_CREAT | os.O_APPEND,0644)
	   except OSError as e:
	      ErrorMessage(e.strerror)
	else:
	  
	   try:
	     os.execvp(tokens[0], tokens)
	   except OSError as e:
              ErrorMessage(e.strerror)
	
# Program execution begins here

print("\n\n\t*********MY SHELL*********")
 
Execute()  
