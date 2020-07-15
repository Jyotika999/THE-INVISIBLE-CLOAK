# This bunch of code will depict the background and will capture it so that we can replace the cloak afterwards with the captured background


import cv2

# now we will be capturing the background image using my webcamera and switching it on .
capture = cv2.VideoCapture(0) # and here your camera will be all set and ready


while capture.isOpened():
    ret, background = capture.read()  # basically , this will be reading from the webcam when the given condition of capture via the webcam is true

    # the variable ret will be true if and only if it was able to read the image
    # imshow function will display what it is capturing the above function will basically tell you what the camera is reading
    if ret==True:

        cv2.imshow("image", background)

        if cv2.waitKey(6)== ord('q'):
        	# we will saving the image that is captured as image.jpg
        	cv2.imwrite('image.jpg',background)
        	break


capture.release()
cv2.destroyAllWindows()
     


