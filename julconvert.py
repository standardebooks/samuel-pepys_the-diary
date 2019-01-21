#!/usr/bin/env python3

from jdcal import jcal2jd, jd2gcal
import os
import re

def gregorian_to_julian(match):
	dateSplit = match.group(0).split('-')
	julDate = jcal2jd(dateSplit[0],dateSplit[1],dateSplit[2])
	julCal = jd2gcal(*julDate)
	julCalString = f"{str(julCal[0])}-{str(julCal[1]).zfill(2)}-{str(julCal[2]).zfill(2)}"
	print(match.group(0), julCalString)
	return julCalString

for root, _, filenames in os.walk(os.getcwd()):
	for filename in sorted(filenames):
		if ".git/" in os.path.join(root, filename):
			continue

		if filename.endswith(".xhtml"):
			with open(os.path.join(root, filename), "r+", encoding="utf-8") as file:
				xhtml = file.read()
				processed_xhtml = xhtml
				pattern = re.compile(r'\d\d\d\d-\d\d-\d\d')

				processed_xhtml = re.sub(pattern, gregorian_to_julian, processed_xhtml)

				file.seek(0)
				file.write(processed_xhtml)
				file.truncate()
