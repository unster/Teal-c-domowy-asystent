#-*- coding: utf-8 -*-
##!/usr/bin/env python
from filmweb.filmweb import Filmweb
import sys, os
import subprocess
import feedparser
import time 
reload(sys)
sys.setdefaultencoding('utf-8')

atrybuty = sys.argv
numer = atrybuty[1]
numer = int(numer)

d = feedparser.parse('https://yts.ag/rss/0/720p/all/0')
fw = Filmweb()
post = d.entries[numer]
post.title = post.title.replace("[720p]","")


#subprocess.call(["/home/pi/speech.sh", introMessage])

if len(atrybuty) == 3:
	#subprocess.call(["/home/pi/speech.sh", "Nie znalazłam miejsca docelowego"])
	link = d.entries[numer]
	link2 = link.enclosures[0]['href']
	#print link2
	os.system('wget -O "/home/pi/torrenty/' + post.title + '.torrent" ' + link2)
	#subprocess.call(["/home/pi/speech.sh", "Torrent został ściągnięty"])
	quit()

items = fw.search(post.title)
item = items[0] # grab first result
info = item.get_info() # fetch more info
print('Tytuł filmu: ' + item.name)
subprocess.call(["/home/pi/speech.sh", "Tytuł filmu: ", item.name])
print('Rok premiery: ' + str(item.year))
subprocess.call(["/home/pi/speech.sh", "Rok premiery: ", str(item.year)])
ocena = "%.1f" % item.rate
print('Ocena: ' +  str(ocena))
subprocess.call(["/home/pi/speech.sh", "Ocena: ", str(ocena)])
if not info['description_short']:
	print('Brak opisu dla tego filmu w bazie filmwebu')
	subprocess.call(["/home/pi/speech.sh", "Brak opisu dla tego filmu w bazie filmwebu"])
	quit()
print('Opis: ' + info['description_short'])
subprocess.call(["/home/pi/speech.sh", info['description_short']])