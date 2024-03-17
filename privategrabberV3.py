#!/usr/bin/python
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
Cyan = '\033[36m'
white = '\033[37m'
black = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
  _____             _   _             _               
 |  __ \           | | (_)           | |              
 | |__) |___   ___ | |_ _ _ __   __ _| |__   _____  __
 |  _  // _ \ / _ \| __| | '_ \ / _` | '_ \ / _ \ \/ /
 | | \ \ (_) | (_) | |_| | | | | (_| | |_) | (_) >  < 
 |_|  \_\___/ \___/ \__|_|_| |_|\__,_|_.__/ \___/_/\_\
                                                      
                                                             
 Websites Grabber V3.0    |   Free method    | |  Coded by Rootinabox                             
                      
 [+] Telegram : @rootinabox
 [+] Channel  : https://t.me/Rootinabox_Community

   \033[32m>----------------------------------<
   [-] 1. Grab list of IPs
   [-] 2. Reverse IPs
   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

choice = raw_input('#~: \033[34mChoose\033[32m Number : ')

def rapid_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        x = requests.get('https://rapiddns.io/s/'+url+'?full=1&down=1#result/', headers=headers, timeout=30).content
        if '<th scope="row ">' in x:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                print("[Reversing Ip--> ] {} : Grabbed successfully".format(website_url))
                open('Reversed_IPs.txt', 'a').write(website_url + '\n')
        else:
            print("[Reversing Ip--> ]" + url + " : Bad IP !")
    except:
        pass


def getingiips():
	rootxcode = raw_input('#~:Frist Page : ')
	CODEE = raw_input('#~:Last Page : ')
	try:
		for page in range(int(rootxcode), int(CODEE)):
			urls = 'http://usings.ru/bots.php?bot=&page='+str(page)
			ROOTGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'IP' in ROOTGET:
				REGEX = re.findall("[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}",ROOTGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('Grabbed_IPs.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY Rootinabox --> ]' + Fore.WHITE)
	except:
		pass


def Main():
	try:
		if choice =='1':
			getingiips()
		if choice =='2':
			list = raw_input("\n\033[91mGive Me List \033[97m#~: \033[97m")
			dragonslyr = raw_input("\033[91mthread \033[97m\033[97m#~: \033[97m")
			rev1 = open(list, 'r').read().splitlines()
			pp = Pool(int(dragonslyr))
			pr = pp.map(rapid_dns, rev1)

	except:
		pass		


if __name__ == '__main__':
	Main()