import socket
import threading
import os

hacker = "\033[38;5;118m"
clear = "\033[0m"

def scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "N/A"
                print(f"""
{hacker}
    ________  __  __            __           
   /  _/ __ \/ / / /_  ______  / /____  _____
   / // /_/ / /_/ / / / / __ \/ __/ _ \/ ___/ 
 _/ // ____/ __  / /_/ / / / / /_/  __/ /    
/___/_/   /_/ /_/\__,_/_/ /_/\__/\___/_/  
{clear}
[{hacker}+{clear}] TARGET{hacker}:{clear} {target}
[{hacker}+{clear}] PORT{hacker}:{clear} {port}
[{hacker}+{clear}] SERVICE{hacker}:{clear} {service}
[{hacker}+{clear}] STATUS{hacker}:{clear} Open
          """)
        s.close()
        input("")
    except:
        pass

def thread(target):
    threads = []
    for port in range(1, 65536):
        thread = threading.Thread(target=scan, args=(target, port))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

def portscanner_main():
    target = input(f"[{hacker}+{clear}] ip{hacker}:{clear} ")
    thread(target)
