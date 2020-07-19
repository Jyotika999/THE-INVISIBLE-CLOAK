import cv2 # OpenCV library
import numpy  # numpy library
import keyboard
import time # this library will provide camera some time , before the code gets executed


cap = cv2.VideoCapture(0) # for live vedio capture , an object gets created to capture the input

time.sleep(3) # provided 3 units of time for the camera to get setup and avoid the initial blurness of the camera and for the final setup of the vediocapture

#inorder to capture the best image of the background
for i in range(30):

	ret, back = cap.read() # reading the input here , to capture the backgorund , we have given 30 iterations and get the best image of the background , .read() will return two values , one is the image that is captured and second is the value returned true or false
	if ret==False:
		continue

# till the capture object is opened or running , the following loop will get executed
while(cap.isOpened()):

	ret,image= cap.read() # capturing the image separtely here to perform operation on it

	if ret==False:  # when the webcam is turned off
		break

	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)  # by default pur webcam captures BGR , here we are converting the image from BGR default value to HSV that is HUE SATURATION VALUE
	# HERE WE ARE PARTICULARLY CONVERTING BGR TO HSV AND NOT TO OTHER RGB FORMAT,etc because HSV format only the hue part is dependent upon color
	# in opencv we have only 8 bits to store the color values , i.e. 2^8  values possible


	lower_red = numpy.array([0,120,70]) # HSV VALUES STORED IN ARRAYS
	upper_red = numpy.array([0,255,255])# HSV VALUES 

	mask1 = cv2.inRange(hsv, lower_red, upper_red)# separating the cloak part 

	lower_red = numpy.array([170, 120, 70])
	upper_red = numpy.array([180, 255, 255]) # red color also lays in range 170-180 range
	mask2 = cv2.inRange(hsv, lower_red, upper_red) # mask 2 will also separate the cloak 

	mask1 = mask1 + mask2 # taking an OR ,for any red shade in mask1 or mask2 will get stored now in mask1

	mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8),iterations=2)
	mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,numpy.ones((3,3),numpy.uint8),iterations=1)
	
	mask2 = cv2.bitwise_not(mask1) # this will include all that part of the image that was except the cloak part

	# for segmentation of the color
	res1 = cv2.bitwise_and(back, back, mask=mask1) #bitwise and operation to superimpose the background image 
	

	#used to superimpose the cloak part ,that is basically acting as a subtitute for the cloak part
	res2 = cv2.bitwise_and(image, image, mask= mask2)

	#linearly adding two images

	final_output = cv2.addWeighted(res1,1,res2,1,0) # paramerters of the forms alpha, x, beta, y, gammma such that (alpha * x + beta * y + gamma =0)
	 

	cv2.imshow("THE MAGICAL CLOAK", final_output)
	k  = cv2.waitKey(1)
	if k==ord('q'):
		break
	if keyboard.is_pressed('q'):
		break
cap.release()
cv2.destroyAllWindows()