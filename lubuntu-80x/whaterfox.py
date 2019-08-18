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

# whaterfox FOTO: 3TAB || VIDEO: 5TAB

def like(url):
	mouse.position = (1281,378) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	keyboard.press(Key.f6) #Firefox command to access link navigation
	keyboard.release(Key.f6)
	time.sleep(1)

	keyboard.type(url) #Type url proxy site

	keyboard.press(Key.enter) #Enter to access proxy site
	keyboard.release(Key.enter)
	time.sleep(5)

	mouse.position = (713,508) #Modal
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
    qtdTabByMediaType = 5
  if qtdTabByMediaType == 0:
    return

	count = 1
	for x in range(9):
		arrayURL = getURL.splice('.kproxy')		
		urlToLike = 'server{}.kproxy{}'.format(count, arrayURL[1])
		count = count + 1

  	like(url,qtdTabByMediaType)

	mouse.position = (1426,14) #Close browser after loop
	mouse.click(Button.left, 1)
