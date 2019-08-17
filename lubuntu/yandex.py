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
eua1X = 487
eua1Y = 689

#EUA2
eua2X = 487
eua2Y = 721

#ALE
aleX = 490
aleY = 759

#HOL
holX = 484
holY = 791

#RU
ruX = 486
ruY = 829

#RepTcheca
repX = 503
repY = 862



def yandex(url, mediaTabTimes, xServer, yServer):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (330,882) #Open Yandex
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (716,146) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (475,635) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (493,530) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (517,648) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (710,819) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (721,598) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (683,460) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1260,369) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1419,15) #Close browser
	mouse.click(Button.left, 1)



