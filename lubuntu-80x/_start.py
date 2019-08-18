import _getUrl
import chrome
import falkon
import firefox
import gnome
import palemoon
import slimjet
import whaterfox
import yandex
import time

urlMedia = ''
typeMedia = ''

firefoxUrlFormatted = _getUrl.firefoxURL(urlMedia)
firefox.startRequest(firefoxUrlFormatted,typeMedia)
time.sleep(60)

chromeUrlFormatted = _getUrl.chromeURL(urlMedia)
chrome.startRequest(chromeUrlFormatted,typeMedia)
time.sleep(60)

falkonUrlFormatted = _getUrl.falkonURL(urlMedia)
falkon.startRequest(falkonUrlFormatted,typeMedia)
time.sleep(60)

gnomeUrlFormatted = _getUrl.gnomeURL(urlMedia)
gnome.startRequest(gnomeUrlFormatted,typeMedia)
time.sleep(60)

palemoonUrlFormatted = _getUrl.palemoonURL(urlMedia)
palemoon.startRequest(palemoonUrlFormatted,typeMedia)
time.sleep(60)

yandexUrlFormatted = _getUrl.yandexURL(urlMedia)
yandex.startRequest(yandexUrlFormatted,typeMedia)
time.sleep(60)

slimjetUrlFormatted = _getUrl.slimjetURL(urlMedia)
slimjet.startRequest(slimjetUrlFormatted,typeMedia)
time.sleep(60)

whaterfoxUrlFormatted = _getUrl.whaterfoxURL(urlMedia)
whaterfox.startRequest(whaterfoxUrlFormatted,typeMedia)
time.sleep(60)
