""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')



cap = cv2.VideoCapture(0)
cap.open()



while(True):
# Capture frame-by-frame
	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))

	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		##Draw a happy face with two eyes & a mouth
		cv2.circle(frame, (w/3+x, h/3+y), w/20, (255, 255, 255), (5/3)*(w/14)) #draws white circle for eye
		cv2.circle(frame, (2*w/3+x, h/3+y), w/20, (255, 255, 255), (5/3)*(w/14)) #draws second white circle for second eye
		cv2.circle(frame, (w/3+x, h/3+y), w/45, (0,0,0), (5/3)*(w/18)) #draws black circle for inside first eye
		cv2.circle(frame, (2*w/3+x, h/3+y), w/45, (0,0,0), (5/3)*(w/18)) #draws second black circle for inside second eye 
		#Make happy face using arc from ecllipse ")"
		cv2.ellipse(frame, (w/2+x, 2*h/3+y), (w/3, w/7), 0, 10, 170, (0,0,0), (4/3)*(w/30)) #draws black arc for mouth of happy face

# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
#While not true!
cap.release()
cv2.destroyAllWindows()
	