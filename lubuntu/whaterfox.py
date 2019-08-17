from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import pyperclip
import time

keyboard = KeyboardController()
mouse = MouseController()

def tabPress(qtd):
	for x in range(qtd):
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		time.sleep(1)

#Servers position:
#EUA1
eua1X = 505
eua1Y = 682

#EUA2
eua2X = 510
eua2Y = 714

#ALE
aleX = 511
aleY = 747

#HOL
holX = 503
holY = 778

#RU
ruX = 510
ruY = 805

#RepTcheca
repX = 508
repY = 838



def whaterfox(url, mediaTabTimes, xServer, yServer):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (393,883) #Open Whaterfox
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (82,117) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (486,636) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (519,544) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (561,638) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (713,804) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	#mouse.position = (714,572) #Agree terms to proxy site
	#mouse.click(Button.left, 1)
	#time.sleep(11)

	mouse.position = (697,518) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1260,385) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1410,26) #Close browser
	mouse.click(Button.left, 1)



