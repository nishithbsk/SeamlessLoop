import numpy as np
import cv2
import os
import re

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    # Obtained from Stack Overflow. Alphanumeric sorting.
	return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]  

def get_all_frames(dataset):
	path = "../data/frames/" + dataset.lower()
	all_frames_path = os.listdir(path)
	all_frames_path.sort(key=natural_sort_key)
	all_frames_path = np.array(all_frames_path)
	
	all_frames = []
	for frame_path in all_frames_path:
		frame_path_absolute = path + "/" + frame_path
		frame = cv2.imread(frame_path_absolute)
		all_frames.append(frame)
	
	return np.array(all_frames)

def get_number_of_frames(dataset):
	path = "../data/frames/" + dataset.lower()
	all_frames_path = os.listdir(path)
	return len(all_frames_path)










