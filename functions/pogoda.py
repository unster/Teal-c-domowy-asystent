#!/usr/bin/python -*- coding: utf-8 -*-

import urllib, re
import sys
import os
www = urllib.urlopen('http://www.meteoprog.pl/pl/weather/' + sys.argv[1] )
www_tekst = www.read()
wyrazenie = '<meta property="og:description" content="(.+?)" />'
pogoda = re.findall(wyrazenie, www_tekst)
print pogoda[0]
stream = os.popen('/home/pi/speech.sh Aktualna ' + pogoda[0])