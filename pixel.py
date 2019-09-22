import numpy as np
import cv2

def getPixels(images):

    count = 0
    sum = 0
    total = 0

    for img in images:
        for i in range(img.shape[1]):
            for j in range(img.shape[0]):
                if(img[j][i]>0):
                    count += 1
                    sum += img[j][i]
        avg = sum/count
        total += avg

    total /= 3
    return total

