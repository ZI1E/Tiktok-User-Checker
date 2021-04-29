from TikTokApi import TikTokApi
import requests
import pathlib
import colorama
import os, sys
import time
from pathlib import Path
from colorama import Fore
from colorama import Style
from colorama import Back

api = TikTokApi()
current_path = os.path.dirname(os.path.realpath(__file__))
open('Files/Available.txt', 'a')
open('Files/Usernames.txt', 'a')
names = open('Files/Usernames.txt', 'r') 
available = open('Files/Available.txt', 'w') 
mypath = Path('Files/Usernames.txt')
numberOfUsernames = 0
savedNames = 0

def check():
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+"ZIE TikTok Username Checker")

    if mypath.stat().st_size == 0:
        print(Fore.WHITE+"\nPlease put your names in Usernames.txt"+ Fore.RED + "\nClosing in 5 seconds")
        time.sleep(5)
        sys.exit()
    else:  
            pass
    with open('Files/Usernames.txt', 'r') as u: 
            
            for line in u:
                username = line.rstrip("\n")
                if len(username) < 25:
                  global numberOfUsernames
                  numberOfUsernames += 1

                  try:
                      

                      user = api.getUserObject(username)

                      print(user)
                      print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"Taken"+Fore.WHITE+"] " +Fore.WHITE +username)

                  except: 
                      global savedNames
                      savedNames+=1
                      available.write(username + "\n")
                      print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"Not Taken"+Fore.WHITE+"] " +Fore.WHITE +username)

              
tic = time.perf_counter() 
check()
toc = time.perf_counter()
available.close()         
print(Fore.CYAN+"\nChecker finished " + str(numberOfUsernames) + f" usernames in {toc - tic:0.4f} seconds")
print("Saved " + str(savedNames) + " username(s) saved!")
input("You Need Exit? , (Type : Anything For Exit) ")
Confirm = 'Yes'
if Confirm:
    print(Fore.RED +"Closing in 5 seconds")
    time.sleep(5)
    sys.exit()