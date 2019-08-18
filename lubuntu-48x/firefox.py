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

#Firefox run at 90 zoom

#Servers position:
#EUA1
eua1X = 605
eua1Y = 674

#EUA2
eua2X = 601
eua2Y = 704

#ALE
aleX = 598
aleY = 736

#HOL
holX = 589
holY = 767

#RU
ruX = 638
ruY = 797

#RepTcheca
repX = 601
repY = 830

# firefox FOTO: 3TAB || VIDEO: 5TAB

def firefox(url, mediaTabTimes, xServer, yServer):
  
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (176,884) #Open Firefox
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (218,109) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(10)

  	mouse.position = (715,215) #Accept coockie terms
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (635,628) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(2)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (570,536) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (625,627) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (781,801) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (806,650) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (783,508) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1348,318) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1587,14) #Close
	mouse.click(Button.left, 1)



def startRequest(url,mediaTabTimes):
  qtdTabByMediaType = 0
  if mediaTabTimes == 'foto':
    qtdTabByMediaType = 3
  if mediaTabTimes == 'video':
    qtdTabByMediaType = 5
  if qtdTabByMediaType == 0:
    return

  firefox(url,qtdTabByMediaType,eua1X,eua1Y)
  firefox(url,qtdTabByMediaType,eua2X,eua2Y)
  firefox(url,qtdTabByMediaType,aleX,aleY)
  firefox(url,qtdTabByMediaType,holX,holY)
  firefox(url,qtdTabByMediaType,ruX,ruY)
  firefox(url,qtdTabByMediaType,repX,repY)
