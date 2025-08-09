import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
  
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mHướng Dev - Kiếm Tiền Online\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97mi.urs.bin.python.TrinhHuong 
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/+77MuosyD-yk4MGY1🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mTool Auto TikTok")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.2 \033[1;97m: \033[1;34mTool Auto Instagram")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.3 \033[1;97m: \033[1;34mTool Auto Twitter")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.4 \033[1;97m: \033[1;34mTool Auto Thread")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.5 \033[1;97m: \033[1;34mTool Auto Linkedin")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.6 \033[1;97m: \033[1;34mTool Auto Snapchat V1")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.7 \033[1;97m: \033[1;34mTool Auto Snapchat V2")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mTool TTC Pro5")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mTool TTC Pro5v1")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.3 \033[1;97m: \033[1;34mTool TTC Instagram")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mTool TDS Pro5")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mTool TDS TikTok")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.3 \033[1;97m: \033[1;34mTool TDS Instagram")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Spam Vip \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4 \033[1;97m: \033[1;34mTool Spam sms")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m00 \033[1;97m: \033[1;34mTHOÁT TOOL")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1.1':
		# Thành Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AutoTikTokv1.py').text)
	elif chon == '1.2':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AutoIG.py').text)
	elif chon == '1.3':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AutoX.py').text)
	elif chon == '1.4':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AutoTheads.py').text)
	elif chon == '1.5':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AutoLinkedin.py').text)
	elif chon == '1.6':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AUTOsnap.py').text)
	elif chon == '1.7':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/AUTOSNAPCHAT.py').text)
	elif chon == '1.8':
		exec(requests.get('').text)
	elif chon == '1.9':
		exec(requests.get('').text)
        
		# TTC
	elif chon == '2.1':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/PHTOOL/refs/heads/main/TTCPRO5.py').text)
	elif chon == '2.2':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/TTCPRO5v1.py').text)
	elif chon == '2.3':
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/TTCIG.py').text)
	elif chon == '2.4':
		exec(requests.get('').text)
	elif chon == '2.5':
		exec(requests.get('').text)
		# TDS
	elif chon == '3.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/TDSPRO5v1.py').text)
	elif chon == '3.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/TDSTIKTOK.py').text)
	elif chon == '3.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/TDSIG.py').text)
	elif chon == '4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/SPAMSMSV1.py').text)
	elif chon == '00':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/pqhcoder/TOOLGOP/refs/heads/main/THOATTOOL.py').text)
    















































































































		sys.exit("")
