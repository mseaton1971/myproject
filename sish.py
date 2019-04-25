#sish.py by Marlon Seaton
#import sys
import os
 
#status = True

line = raw_input("sish$ ")

while(line != "exit"):
  
  #Parse the line into tokens with white space as the delimiter
    
  tokens = line.split()
 
  os.execvp(tokens[0],tokens)  
  
  line = raw_input("sish$ ")

  
