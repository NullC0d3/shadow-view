#!/usr/bin/env python3
import time
import sys
import platform
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

ver = platform.python_version()

if (ver <= '3'):
	print("\033[91m Shadows Traffic isn't compatible with python2 use python 3.x\033[00m")
	sys.exit(1)

import random
import time
import os

try:
	from stem import Signal
	from stem.control import Controller
	import requests

except ImportError:

	print("\033[91m Install stem and requests with pip\033[00m")

	sys.exit(1)

print("""\033[91m

 ######    #####   ########   #######  ##        #######   ######   ######  
##    ##  ##   ##  ##     ## ##     ## ##       ##     ## ##    ## ##    ## 
##       ##     ## ##     ##        ## ##              ## ##       ##       
##       ##     ## ##     ##  #######  ##        #######   ######   ######  
##       ##     ## ##     ##        ## ##              ##       ##       ## 
##    ##  ##   ##  ##     ## ##     ## ##       ##     ## ##    ## ##    ## 
 ######    #####   ########   #######  ########  #######   ######   ######\033[00m

				\033[93mv.1.2
				By C0d3l3ss\033[00m
""")

#tor_password = input("\033[92m Enter your tor password: \033[00m")


### 	U CAN USE THIS SCRIPT FOR 2 WEBSITE TO GET TRAFFICE FOR BOTH OF THEM   	###
### 	THIS SCIRPTS WORK GOOD FOR ANY WEBSITE OR BLOGS 	###
address ='https://youtu.be/FnvCc23dw1g'
views = int(10000)   #### enter  target views you want


Timer = 120

# signal Tor for new identity

def renew_connection():

	with Controller.from_port(address="127.0.0.1", port = 9051) as controller:

		controller.authenticate(password="")   #password can be found in torrc file(HashedControlPassword)

		controller.signal(Signal.NEWNYM)

		controller.signal(Signal.HUP)

		time.sleep(5)


def tor_session():

#setup proxies

	session = requests.session()

	session.proxies = {}

	session.proxies['http'] = 'socks5://localhost:9050'

	session.proxies['https'] = 'socks5://localhost:9050'

	return session


def visit():

#file which contains user-agent lists

	with open('agents.txt','r') as file:

		lines = open('agents.txt').read().splitlines()

	for num in range(views):

		header_value = random.choice(lines)

		header = {}

		header['User-Agent'] = header_value

		session = tor_session()

		session.get(address, headers=header)	#visiting the URL given by the user
		

		firefox_options = Options()
		firefox_options.add_argument(header_value)

		# Override Firfox profile with multi vendor options
		user_agent = header_value
		profile = webdriver.FirefoxProfile() 
		profile.set_preference("general.useragent.override", user_agent)
		browser = webdriver.Firefox(profile,options = firefox_options,executable_path= '/bin/geckodriver')
		#open firefox mobile view and minimized
		browser.set_window_size(360,640)
		browser.minimize_window()
		#open first link then open new tab to open 2nd link
		browser.get(address)

        for i in range(views):
            time.sleep(Timer)
            

        

		print("\033[92m-\033[00m" * 150)

		print("\033[92m Page Visited with following ip with user-agent..\033[00m")

		print(session.get('http://httpbin.org/ip').text)	#display current ip

		print(session.get('http://httpbin.org/user-agent', headers=header).text)	#display current user-agent

		#close firefox then renew seesions
		browser.quit()
		renew_connection()

		if num == (views - 1):
			print("\033[92m-\033[00m " * 150)
			print("\033[01m\033[93m Shadows Traffic Successfully Visited & Viewed Target Website ",views, "times\033[00m")
			sys.exit(0)


visit()


