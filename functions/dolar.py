#-*- coding: utf-8 -*-
##!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse, subprocess

url = "http://www.kursywalutnbp.eu/widget/?currencies=USD"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "lxml")
div = soup.find("td", { "class" : "currency-rate-column" })
kurs = ''.join(map(str, div.contents))
kurs2 = kurs.split(",")
zlotowki = kurs2[0]
grosze = kurs2[1][:2]
subprocess.call(["/home/pi/speech.sh", "Jeden dolar amerykański to " + zlotowki + "złote i " + grosze + "grosze"])