import cv2
import numpy as np
import imutils

def saveSegments(img):

    greyImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    X = greyImage.shape[1]
    Y = greyImage.shape[0]
    mid = (X/2, Y/2)

    corner1 = np.array([[(0,0), mid, (X,0)]], dtype=np.int32)
    corner2 = np.array([[(0,0), mid, (0,Y)]], dtype=np.int32)
    corner3 = np.array([[(0,Y), mid, (X, Y)]], dtype=np.int32)
    corner4 = np.array([[(X, Y), mid, (X,0)]], dtype=np.int32)
    corners = [corner1, corner2, corner3, corner4, corner4] 

    segments = []

    for i in range(4):
        
        mask = np.zeros(greyImage.shape, dtype=np.uint8)
        cv2.fillPoly(mask, corners[i], 255)
        segment = cv2.bitwise_and(greyImage, mask)
        segments.append(segment)

    return segments