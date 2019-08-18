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
eua1X = 498
eua1Y = 673

#EUA2
eua2X = 494
eua2Y = 706

#ALE
aleX = 499
aleY = 737

#HOL
holX = 507
holY = 768

#RU
ruX = 499
ruY = 802

#RepTcheca
repX = 502
repY = 833

# falkon FOTO: 1TAB || VIDEO: 5TAB

def falkon(url, mediaTabTimes, xServer, yServer):
    
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (236,884) #Open Falkon
	mouse.click(Button.left, 1)
	time.sleep(7)

  	mouse.position = (719,195) #Accept coockie terms
	mouse.click(Button.left, 2)
	time.sleep(2)
	
	mouse.position = (497,629) #Click to select server
	mouse.click(Button.left, 2)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 2)
	time.sleep(3)

	mouse.position = (509,529) #Click right to paste url
	mouse.click(Button.right, 2)
	time.sleep(3)

	mouse.position = (558,665) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (706,801) #Click to access site with proxy site
	mouse.click(Button.left, 2)
	time.sleep(11)

	mouse.position = (722,590) #Agree terms to proxy site
	mouse.click(Button.left, 2)
	time.sleep(11)

	mouse.position = (703,486) #Modal
	mouse.click(Button.left, 2)
	time.sleep(3)

	mouse.position = (1246,345) #Click null area
	mouse.click(Button.left, 2)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1427,15) #Close browser
	mouse.click(Button.left, 1)


def startRequest(url,mediaTabTimes):
  qtdTabByMediaType = 0
  if mediaTabTimes == 'foto':
    qtdTabByMediaType = 1
  if mediaTabTimes == 'video':
    qtdTabByMediaType = 5
  if qtdTabByMediaType == 0:
    return

  falkon(url,qtdTabByMediaType,eua1X,eua1Y)
  falkon(url,qtdTabByMediaType,eua2X,eua2Y)
  falkon(url,qtdTabByMediaType,aleX,aleY)
  falkon(url,qtdTabByMediaType,holX,holY)
  falkon(url,qtdTabByMediaType,ruX,ruY)
  falkon(url,qtdTabByMediaType,repX,repY)
