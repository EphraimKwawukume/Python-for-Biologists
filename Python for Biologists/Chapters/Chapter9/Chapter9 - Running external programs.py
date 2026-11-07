import subprocess

#Without shell=True, Python would try to launch "time /T" as a program directly. 
#But time is a built-in Command Prompt command, not a standalone program, so it likely raises FileNotFoundError.
#shell=True runs it through Command Prompt, which understands built-in commands like time.

#subprocess.call("start ms-clock:", shell=True)#launches the clock app
subprocess.call("time /T", shell=True)#shows the time on the terminal

#Saving program output
current_time = subprocess.check_output("time /T", shell=True, text=True)
#text=True tells Python to decode the command’s output from bytes into a regular string. Without it, check_output() returns bytes, which look like b'...' when displayed.

print('The current time: ' + current_time)

#User input makes our programs more flexible
#dna = "ATCGATCGTGACTAGCTACG"
#When data is mixed in with the code in this manner, it is said to be hard-coded.Giving us a problem like  if we want to change the input data, we have to open up the code and edit it

#Interactive user input
# input takes a single string argument, which is the prompt to be displayed to the user, and returns the value typed in as a string:

#MyName = input("Enter the accession name: ")
#print(MyName)

#Command line arguments
import sys
print(sys.argv)
