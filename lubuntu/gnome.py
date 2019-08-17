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
eua1X = 490
eua1Y = 662

#EUA2
eua2X = 485
eua2Y = 700

#ALE
aleX = 495
aleY = 735

#HOL
holX = 505
holY = 768

#RU
ruX = 489
ruY = 803

#RepTcheca
repX = 530
repY = 837

# gnome FOTO: 2TAB || VIDEO: 5TAB

def gnome(url, mediaTabTimes, xServer, yServer):
	
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (268,883) #Open Gnome Browser
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (1238,21) #Open Favorites SPECIAL STEP
	mouse.click(Button.left, 1)
	time.sleep(2)

	mouse.position = (1113,135) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (475,613) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (494,509) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (542,628) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (717,796) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (714,572) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (694,441) #Modal
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

def startRequest(url,mediaTabTimes):
  qtdTabByMediaType = 0
  if mediaTabTimes == 'foto':
    qtdTabByMediaType = 3
  if mediaTabTimes == 'video':
    qtdTabByMediaType = 6
  if qtdTabByMediaType == 0:
    return

  gnome(url,qtdTabByMediaType,eua1X,eua1Y)
  gnome(url,qtdTabByMediaType,eua2X,eua2Y)
  gnome(url,qtdTabByMediaType,aleX,aleY)
  gnome(url,qtdTabByMediaType,holX,holY)
  gnome(url,qtdTabByMediaType,ruX,ruY)
  gnome(url,qtdTabByMediaType,repX,repY)

