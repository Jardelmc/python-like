import chrome
import falkon
import firefox
import gnome
import palemoon
import slimjet
import whaterfox
import yandex

url = ''
typeMedia = ''

firefox.startRequest(url,typeMedia)
chrome.startRequest(url,typeMedia)
falkon.startRequest(url,typeMedia)
gnome.startRequest(url,typeMedia)
palemoon.startRequest(url,typeMedia)
yandex.startRequest(url,typeMedia)
slimjet.startRequest(url,typeMedia)
whaterfox.startRequest(url,typeMedia)