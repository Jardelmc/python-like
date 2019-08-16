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



def firefoxFotoEUA1(url):
	pyperclip.copy(url)
	time.sleep(2)
	mouse.position = (176,884) #Open Firefox
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (218,109) #Open Proxy Site
	mouse.click(Button.left, 1)
	time.sleep(6)

	mouse.position = (635,628) #Click to select server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (605,674) #Select EUA1 server
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (570,536) #Click right to paste url
	mouse.click(Button.right, 1)
	time.sleep(1)

	mouse.position = (625,627) #Paste URL
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (781,801) #Click to access site with proxy site
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (806,650) #Agree terms to proxy site
	mouse.click(Button.left, 1)
	time.sleep(7)

	mouse.position = (783,508) #Modal
	mouse.click(Button.left, 1)
	time.sleep(1)

	mouse.position = (1348,318) #Click null area
	mouse.click(Button.left, 1)
	time.sleep(1)

	tabPress(3) #Tab Key

	keyboard.press(Key.space)
	keyboard.release(Key.space)
	time.sleep(2)

	mouse.position = (1587,14)
	mouse.click(Button.left, 1)



