import cv2
import numpy as np 


def stackup(images):
    mask = np.zeros(images[1].shape, dtype=np.uint8)
    mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    for i in range(0,9):
        if i==0:
            mask = images[0]
        else:
            mask = cv2.bitwise_or(mask,images[i])

    return mask
