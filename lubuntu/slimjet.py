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
eua1X = 502
eua1Y = 654

#EUA2
eua2X = 499
eua2Y = 685

#ALE
aleX = 514
aleY = 719

#HOL
holX = 805
holY = 748

#RU
ruX = 507
ruY = 778

#RepTcheca
repX = 509
repY = 808



def slimjet(url, mediaTabTimes, xServer, yServer):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (360,885) #Open Midori Browser
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (144,86) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (502,610) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (515,516) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (565,644) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (716,775) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (717,631) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (711,492) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1244,409) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1422,17) #Close browser
	mouse.click(Button.left, 1)



