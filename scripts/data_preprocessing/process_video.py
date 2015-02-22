import numpy as np
import cv2

video = cv2.VideoCapture('../../data/input_videos/pool.mp4')

success, image = video.read()

count = 0
while success:
	success, image = video.read()
	cv2.imwrite("frame%d.jpg" % count, image)
	if cv2.waitKey(10) == 27:
		break
	count += 1


