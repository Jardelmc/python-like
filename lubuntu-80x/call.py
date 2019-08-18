import chrome
import falkon
import firefox
import gnome
import palemoon
import slimjet
import whaterfox
import yandex
import time

def initRequest(url,typeMedia):

  firefox.startRequest(url,typeMedia)
  time.sleep(151)
  chrome.startRequest(url,typeMedia)
  time.sleep(152)
  falkon.startRequest(url,typeMedia)
  time.sleep(153)
  gnome.startRequest(url,typeMedia)
  time.sleep(154)
  palemoon.startRequest(url,typeMedia)
  time.sleep(155)
  yandex.startRequest(url,typeMedia)
  time.sleep(156)
  slimjet.startRequest(url,typeMedia)
  time.sleep(157)
  whaterfox.startRequest(url,typeMedia)
