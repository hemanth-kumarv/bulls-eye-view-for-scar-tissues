import cv2
import numpy as np

def trim(frame): # function to remove excess black bg in the image

    # crop top
    if not np.sum(frame[0, :]):
        if not np.sum(frame[6, :]):
            return trim(frame[5:, :])
        else:
            return trim(frame[1:, :])

    # crop bottom
    if not np.sum(frame[-1, :]):
        if not np.sum(frame[-7, :]):
            return trim(frame[:-6, :])
        else:
            return trim(frame[:-2, :])

    # crop left
    if not np.sum(frame[:, 0]):
        if not np.sum(frame[:, 6]):
            return trim(frame[:, 5:])
        else:
            return trim(frame[:, 1:])

    # crop right
    if not np.sum(frame[:, -1]):
        if not np.sum(frame[:, -7]):
            return trim(frame[:, :-6])
        else:
            return trim(frame[:, :-2])
        
    return frame

def trimImage(img):
    
    trimmedImg =  trim(img)

    if trimmedImg.shape[0] > trimmedImg.shape[1]:
        trimmedImg = cv2.resize(trimmedImg, (trimmedImg.shape[0], trimmedImg.shape[0]))

    else:
        trimmedImg = cv2.resize(trimmedImg, (trimmedImg.shape[1], trimmedImg.shape[1]))
    return trimmedImg