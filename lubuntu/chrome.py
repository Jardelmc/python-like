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


#Chrome run at 90 zoom

#Servers position:
#EUA1
eua1X = 513
eua1Y = 652

#EUA2
eua2X = 495
eua2Y = 684

#ALE
aleX = 521
aleY = 715

#HOL
holX = 510
holY = 748

#RU
ruX = 526
ruY = 779

#RepTcheca
repX = 512
repY = 809



def chrome(url, mediaTabTimes, xServer, yServer):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (206,884) #Open Chrome
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (153,87) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(10)

  mouse.position = (707,195) #Accept coockie terms
	mouse.click(Button.left, 1)
	time.sleep(2)

	mouse.position = (498,609) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (515,515) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (571,643) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (710,773) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (716,629) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (691,491) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1243,509) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1422,17) #Close browser
	mouse.click(Button.left, 1)



