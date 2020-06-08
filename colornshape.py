import scipy.misc
import imageio
from skimage import exposure
from cv2 import *
import numpy as np
#import argparse
import imutils
import serial                                                                                #imports the pyserial module
import time  

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

#img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    """if not ret:
        break"""
    k = cv2.waitKey(1)

    if k == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == 32:
        # SPACE pressed
        img_name = "hello.png"
        cv2.imwrite(img_name, frame)
        print("DONE")
		

cam.release()

cv2.destroyAllWindows()

def detect_color():
		im = imageio.imread('hello.png')    #************INPUT HERE**********************
		print(im.shape)
		x_coord=int(im.shape[0]/2)
		y_coord=int(im.shape[0]/2)
		print(x_coord)
		print(y_coord)
		color = tuple(im[x_coord][y_coord])
		#r, g, b, boo = color
		print(color)
		red=color[0]
		green=color[1]
		blue=color[2]
		if (red > green) and (red > blue):
			m = "RED"
		elif green > blue :
			m= "GREEN"
		else :
			m= "BLUE"
		print("The color of the image is : "+m)
		return m
		
def detect_shape():
		image = cv2.imread('hello.png')   #***********INPUT HERE**********************
		ratio = image.shape[0] / 300.0
		orig = image.copy()
		image = imutils.resize(image, height = 300)
		 
		# convert the image to grayscale, blur it, and find edges
		# in the image
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.bilateralFilter(gray, 11, 17, 17)
		edged = cv2.Canny(gray, 30, 200)

		# find contours in the edged image, keep only the largest
		# ones, and initialize our screen contour
		cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
		screenCnt = None
		cv2.imshow('ch',edged)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		# loop over our contours
		for c in cnts:
			# approximate the contour
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.04 * peri, True)
			
			if len(approx)==3:
				shape="Triangle"
			elif len(approx)==4:
				(x,y,w,h)=cv2.boundingRect(approx)
				ar=w/ float(h)
				shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Rectangle"
			else:
				shape = "Circle"
			# if our approximated contour has four points, then
			# we can assume that we have found our screen
			'''if len(approx) == 4:
				screenCnt = approx
				break
		'''
		print(shape)
		#cv2.drawContours((image, [screenCnt], -1), (0, 255, 0), 3)
		cv2.imshow("Game Boy Screen", image)
		cv2.waitKey(0)
		return shape

m=detect_color()
shape=detect_shape()

#python to arduino 
arduino = serial.Serial('COM3', 9600)  

if(m=="RED" and shape=="Circle"):
    
    var = input("Enter 0 to proceed")
    if(var == '0'):
        arduino.write('0'.encode())
        time.sleep(1)
        #arduino.flush()
elif(m=="GREEN" and shape=="triangle"):

    print("Enter 2 to proceed")
    var=input();
    if(var == '2'):
        arduino.write('2'.encode())
        time.sleep(1)
        #arduino.flush()
elif(m=="BLUE" and shape=="Square"):

    print("Enter 1 to proceed")
    var=input();
    if(var == '1'):
        arduino.write('1'.encode())
        #time.sleep(1)
        arduino.close()
elif(m=="RED" and shape=="Rectangle"):

    print("Enter 0 to proceed")
    var=input();
    if(var == '0'):
        arduino.write('0'.encode())
        time.sleep(1)
        #arduino.flush()
elif(m=="RED" and shape=="Square"):
    arduino.write(b'4')
elif(m=="RED" and shape=="Circle"):
    arduino.write(b'5')
elif(m=="GREEN" and shape=="Square"):
    arduino.write(b'6')
elif(m=="RED" and shape=="Triangle"):
    arduino.write(b'7')
elif(m=="GREEN" and shape=="Circle"):
    arduino.write(b'8')
elif(m=="BLUE" and shape=="Circle"):
    arduino.write(b'9')
elif(m=="BLUE" and shape=="Rectangle"):
    arduino.write(b'10')
elif(m=="BLUE" and shape=="Triangle"):
    arduino.write(b'11')

arduino.close()

    


