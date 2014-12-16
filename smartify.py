#!/usr/bin/env python3

import os,sys
from PIL import Image
import colorsys
from collections import Counter

imgFile = Image.open("HSVstrip.png")
imgXsize,imgYsize = imgFile.size
colourWeight = []

def whatHue(hue):
	if hue > 345.0 and hue <= 360.0: #reddish
		colourWeight.append(1)
	elif hue > 0.0 and hue <= 20.0: #reddish
		colourWeight.append(1)
	elif hue > 160.0 and hue <= 250.0: #blueish
		colourWeight.append(2)
	elif hue > 80.0 and hue <= 160.0: #greenish
		colourWeight.append(3)
	elif hue > 40.0 and hue <= 80.0: #yellowish
		colourWeight.append(4)
	elif hue > 20.0 and hue <= 40.0: #orangebrownish
		colourWeight.append(5)
	elif hue > 250.0 and hue <= 345.0: #pinkish
		colourWeight.append(6)
	else:								#not defined
		colourWeight.append(0)
	return

for x in range(int(0.9 * imgXsize), imgXsize):
	for y in range(int(0.9 * imgYsize), imgYsize):
		r,g,b,a = imgFile.getpixel((x,y)) 
		h,s,v = colorsys.rgb_to_hsv(r, g, b)
		hue = h*360
		#print(x,y)
		whatHue(hue)

most_common,num_most_common = Counter(colourWeight).most_common(1)[0]
print(most_common,num_most_common)
