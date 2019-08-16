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
eua1X = 526
eua1Y = 676

#EUA2
eua2X = 488
eua2Y = 706

#ALE
aleX = 492
aleY = 470

#HOL
holX = 497
holY = 748

#RU
ruX = 504
ruY = 805

#RepTcheca
repX = 512
repY = 809



def falkon(url, mediaTabTimes, xServer, yServer):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (236,884) #Open Falkon
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (358,473) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (497,629) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (509,529) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (558,665) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (706,801) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (722,590) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (703,486) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1246,345) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1427,15) #Close browser
	mouse.click(Button.left, 1)



