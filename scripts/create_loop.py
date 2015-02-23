import numpy as np
import cv2
import math
import colorsys
from get_frames import *

DATASET = "POOL"

frames = get_all_frames(DATASET)
num_frames = get_number_of_frames(DATASET)

num_rows = frames[0].shape[0]
num_cols = frames[0].shape[1]

pixel_across_time = np.zeros((3, 2*num_frames))
for row in xrange(num_rows):
  for col in xrange(num_cols):
    for frame_index in xrange(num_frames):
      # a =  float(frame_index)/(row+1)
      # b = int((math.sin(a * (2*math.pi)) * 127.0) + 127)
      # g = int((math.sin(a * (2*math.pi)) * 127.0) + 127)
      # r = int((math.sin(a * (2*math.pi)) * 127.0) + 127)
      b = frames[frame_index][row, col, 0]
      g = frames[frame_index][row, col, 1]
      r = frames[frame_index][row, col, 2]
      pixel_across_time[0, frame_index] = b
      pixel_across_time[1, frame_index] = g
      pixel_across_time[2, frame_index] = r
      pixel_across_time[0, num_frames+frame_index] = b
      pixel_across_time[1, num_frames+frame_index] = g
      pixel_across_time[2, num_frames+frame_index] = r
     
    pixel_across_time = np.array(pixel_across_time) 
    min_s = 100000
    min_p = 100000
    min_norm = 100000.0
    for s in xrange(num_frames):
      for p in xrange(num_frames/2): 
        if (p < 5): continue
        window = pixel_across_time[:, s:s+p]
        test_window = pixel_across_time[:, s+p:s+p+p]
        sq_diff = np.square(window - test_window)
        norm = np.sqrt(sq_diff[0, :] + sq_diff[1, :] + sq_diff[2, :])
        norm = np.sum(norm)
        norm /= p
        if norm < min_norm:
          min_norm = norm
          min_s = s
          min_p = p
    
    print row, col, min_s, min_p

      

  
