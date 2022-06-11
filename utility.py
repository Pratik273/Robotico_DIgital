#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import os
import sys

file11= open("u2.txt", "r")
menu=["-l","-c","-w","-n","-a","-h"]
    
no_of_lines = 0
no_of_words = 0
no_of_characters = 0
for line11 in file11:
    line11= line11.strip("\n")
    words= line11.split()
    no_of_lines += 1
    no_of_words += len(words)
    no_of_characters += len(line11)
    
if((sys.argv[1])==menu[0]) :
    print(no_of_lines,sys.argv[2])
elif(sys.argv[1]==menu[1]):
    print(no_of_characters,sys.argv[2])
elif(sys.argv[1]==menu[2]):
    print(no_of_words,sys.argv[2])
    
elif(sys.argv[1]==menu[3]):
    print (re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+",line11),sys.argv[2])
elif(sys.argv[1]==menu[4]):
      print(re.sub(r'[^a-zA-Z]', '',line11),sys.argv[2])
elif(sys.argv[1]==menu[5]):
      print("-l: should display no. of lines present in a file",
"-c: no. of character present in a file",
 "-w: no. of words in a file",
"-n: should display only numeric numbers in input file",
"-a: should display only alphabets in input file",
"-h: help message to run your program ")


# file11.close()


# In[ ]:




