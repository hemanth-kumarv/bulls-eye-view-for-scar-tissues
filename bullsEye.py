import cv2
import numpy as np
import imutils
import sys
import trim
import get4
import get6
import pixel
import drawFinal
import stack

images = []
imgnotrim = []

dirName = str(sys.argv[1])

for i in range(8, -1, -1):
    img1 = cv2.imread(dirName+'/lge_'+str(i)+'.png')
    img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(dirName+'/mask_lge_'+str(i)+'.png')
    img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    intersect = cv2.bitwise_and(img1, img2)
    imgnotrim.append(intersect)
    trimImg = trim.trimImage(intersect)
    images.append(trimImg)
    
segments = []
averages = []
segment17 = 0

for i in range(0,9):
    if i < 6:
        segment = get6.saveSegments(images[i])
        segments.append(segment)
        if i == 2 or i == 5:
            for j in range(0, 6):
                segs = [((segments[i])[j]), ((segments[i-1])[j]), ((segments[i-2])[j])]
                average = pixel.getPixels(segs)
                averages.append(average)

    else:
        segment = get4.saveSegments(images[i])
        segments.append(segment)
        if i == 8:
            for j in range(0, 4):
                segs = [((segments[i])[j]), ((segments[i-1])[j]), ((segments[i-2])[j])]
                average = pixel.getPixels(segs)
                segment17 += average
                averages.append(average)
            
averages.append(segment17/4)
output = drawFinal.bullsEye(averages)

for i in range(17):
    level = averages[i]*6/256
    print(str(i+1)+". Pixel value: "+str(int(averages[i]))+" and Level: "+str(level))
stack = stack.stackup(imgnotrim)
cv2.namedWindow('Bulls Eye', cv2.WINDOW_NORMAL)
cv2.namedWindow('Stacked Output', cv2.WINDOW_NORMAL)
cv2.imshow('Bulls Eye', output)
cv2.imshow('Stacked Output',stack)
cv2.waitKey(0)
cv2.imwrite(dirName+'/Bulls_Eye.png', output)
cv2.imwrite(dirName+'/Stacked_Output.png', stack)
