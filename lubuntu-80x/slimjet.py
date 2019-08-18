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

# slimjet FOTO: 3TAB || VIDEO: 6TAB

def like(url):
	mouse.position = (1281,378) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	keyboard.press(Key.f6) #Slimjet command to access link navigation
	keyboard.release(Key.f6)
	time.sleep(1)

	keyboard.type(url) #Type url proxy site

	keyboard.press(Key.enter) #Enter to access proxy site
	keyboard.release(Key.enter)
	time.sleep(5)

	mouse.position = (717,489) #Modal
	mouse.click(Button.left, 1)
	time.sleep(3)

	mouse.position = (1281,378) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(mediaTabTimes) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(3)


def startRequest(url,mediaTabTimes):
  qtdTabByMediaType = 0
  if mediaTabTimes == 'foto':
    qtdTabByMediaType = 3
  if mediaTabTimes == 'video':
    qtdTabByMediaType = 6
  if qtdTabByMediaType == 0:
    return

	count = 1
	for x in range(9):
		arrayURL = getURL.splice('.kproxy')		
		urlToLike = 'server{}.kproxy{}'.format(count, arrayURL[1])
		count = count + 1

  	like(url,qtdTabByMediaType)

	mouse.position = (1421,18) #Close browser after loop
	mouse.click(Button.left, 1)
