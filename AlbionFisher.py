import pyautogui as pg
import cv2
import numpy as np
from PIL import Image, ImageGrab
import time
#To get it work you need to have an image stored in the folder with this Python file 

# Enter the coordinates of the box, where your float will stay (poplavok = float btw)
x1,y1 = 265,350
x2,y2 = 408,495

x,y = 523,445 #This is where you want to throw your float 

meanvalue = 4.8  #You need to know the optimal mean value to actually make it work


x = int()
while True:
	arrayEND = False

	time.sleep(3.5)
	pg.moveTo(x , y, duration = 0.5) 
	pg.mouseDown()
	time.sleep(1)
	pg.mouseUp()
	time.sleep(1.5)
	print('zakinul')
	time.sleep(0.5)

	while arrayEND == False:

		poplavokplace = ImageGrab.grab((x1,y1,x2,y2)) #Takes a screenshot of the box where the float is 
		poplavokplace.save('iii2.png', 'BMP')
		poplavok_place_image_original = cv2.imread('iii2.png')
		poplavok_place_array = np.array(poplavok_place_image_original)
		poplavok_canny = cv2.Canny(poplavok_place_array,90, 200)
		cv2.imwrite('canny.png', poplavok_canny)
		poplavok_place_array_mean = np.mean(poplavok_canny)
		time.sleep(0.3)
		print('mean = '+ str(poplavok_place_array_mean))
		if poplavok_place_array_mean == 0:
			print('mean == 0, ending the program')
			break
			
		if poplavok_place_array_mean >= float(meanvalue) and poplavok_place_array_mean != 0:
			time.sleep(0.1)
			pg.click(clicks = 2)
			arrayEND = True
			print('array has been ended sucessfully (break)')
			break

	while arrayEND == True:
		time.sleep(0.3)
		catch = False
		window = ImageGrab.grab((837,532,1078,567)) #This is where the minigame will appear (FullHD)

		locate = pg.locate('obrezka.png',window, confidence = 0.5)
		if locate == None:
			break
		if locate != None:
			x = locate[0]
			print('x = '+ str(x) + ' catch = True')
			catch = True

		while catch == True:
			window = ImageGrab.grab((837,532,1078,567))
			ggmme = pg.locate('obrezka.png',window, confidence = 0.5)
			if ggmme != None:
				x = ggmme[0]
				print('x = '+ str(x) + '  has been found')
				if 65 < int(x) < 170:
					pg.mouseDown()
					time.sleep(1.1)
					pg.mouseUp()
					time.sleep(0.1)
				if int(x) < 64:
					pg.mouseDown()
					time.sleep(2.5)	
					pg.mouseUp()
			else:
				catch = False
				print('NONE')
				arrayEND = False
				print('minigame has been ended')
				time.sleep(1)
			


pass

# Copyright (c) 2020 Unbewohnte

