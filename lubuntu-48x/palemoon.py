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
eua1X = 592
eua1Y = 649

#EUA2
eua2X = 591
eua2Y = 678

#ALE
aleX = 596
aleY = 709

#HOL
holX = 606
holY = 739

#RU
ruX = 598
ruY = 768

#RepTcheca
repX = 600
repY = 800

# palemoon FOTO: 3TAB || VIDEO: 5TAB

def palemoon(url, mediaTabTimes, xServer, yServer):

	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (299,884) #Open Palemoon
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (210,100) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(12)

	mouse.position = (581,602) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (xServer,yServer) #Select server
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (593,517) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(3)

	mouse.position = (641,598) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (710,767) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (717,601) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(11)

	mouse.position = (710,530) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1237,395) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)

	mouse.position = (1422,17) #Close browser
	mouse.click(Button.left, 1)


def startRequest(url,mediaTabTimes):
  qtdTabByMediaType = 0
  if mediaTabTimes == 'foto':
    qtdTabByMediaType = 3
  if mediaTabTimes == 'video':
    qtdTabByMediaType = 5
  if qtdTabByMediaType == 0:
    return

  palemoon(url,qtdTabByMediaType,eua1X,eua1Y)
  palemoon(url,qtdTabByMediaType,eua2X,eua2Y)
  palemoon(url,qtdTabByMediaType,aleX,aleY)
  palemoon(url,qtdTabByMediaType,holX,holY)
  palemoon(url,qtdTabByMediaType,ruX,ruY)
  palemoon(url,qtdTabByMediaType,repX,repY)
