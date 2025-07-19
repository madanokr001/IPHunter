import os
import sys
from Tools.iplogger import *
from Tools.iptracker import *
from Tools.PortScanner import *

hacker = "\033[38;5;118m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{hacker}
    ________  __  __            __           
   /  _/ __ \/ / / /_  ______  / /____  _____
   / // /_/ / /_/ / / / / __ \/ __/ _ \/ ___/ 
 _/ // ____/ __  / /_/ / / / / /_/  __/ /    
/___/_/   /_/ /_/\__,_/_/ /_/\__/\___/_/  
{clear}      
    [{hacker}+{clear}] version  {hacker}|{clear} 1.0
    [{hacker}+{clear}] Author   {hacker}|{clear} cybermad
    [{hacker}*{clear}] Github   {hacker}|{clear} github.com/madanokr001
    [{hacker}*{clear}] Discord  {hacker}|{clear} cybermad.cpp
          
    [{hacker}01{clear}] {hacker}|{clear} IP Tracker
    [{hacker}02{clear}] {hacker}|{clear} IP Logger
    [{hacker}03{clear}] {hacker}|{clear} Port Scanner
    [{hacker}04{clear}] {hacker}|{clear} Exit
          """)
    
def main():
    while True:
        banner()
        select = input(f"[{hacker}+{clear}] IPHunter{hacker}:{clear} ")
        
        if select == "1":
            iptracker_main()

        elif select == "2":
            iplogger_main()

        elif select == "3":
            portscanner_main()

        elif select == "4":
            sys.exit()
            print(":(")


if __name__ == "__main__":
    main()