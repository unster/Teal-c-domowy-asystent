#!/usr/bin/python -*- coding: utf-8 -*-

import commands, subprocess
status, events = commands.getstatusoutput("/usr/local/bin/gcalcli --military --nocolor --nostarted agenda | sed -e 's/Mon/Poniedziałek/g; s/Tue/Wtorek/g; s/Wed/Środa/g;s/Thu/Czwartek/g; s/Fri/Piątek/g; s/Sat/Sobota/g; s/Sun/Niedziela/g'")

events2 = events.splitlines()

if events.find("No Events Found...") == -1:
	for line in events2:
		if len(line.strip()) != 0 :
			output2 = line.split()
			output2[1] = ' '
			output2[2] = ' '
			output3 = ' '.join(output2)
			print output3
			subprocess.call(["/home/pi/speech.sh", output3])
else:
	subprocess.call(["/home/pi/speech.sh", "W ciągu następnych pięciu dni nie masz żadnych wydarzeń zapisanych w kalendarzu"])



