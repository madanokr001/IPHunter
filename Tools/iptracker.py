import requests
import json

hacker = "\033[38;5;118m"
clear = "\033[0m"

def iptracker(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        date = r.json()
        print(f"{hacker}{json.dumps(date, indent=4)}{clear}")
    except:
        pass
    input("")

def iptracker_main():
    ip = input(f"[{hacker}+{clear}] ip{hacker}:{clear} ")
    iptracker(ip)