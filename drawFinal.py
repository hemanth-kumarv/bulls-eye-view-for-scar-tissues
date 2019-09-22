from PIL import Image, ImageDraw
import numpy as np

def bullsEye(values):

    canvas = Image.new('L', (500,500), color=256)
    draw = ImageDraw.Draw(canvas)
    draw.arc([100, 100, 400, 400], 0, 60, fill=int(values[4]), width=40)
    draw.arc([100, 100, 400, 400], 60, 120, fill=int(values[3]), width=40)
    draw.arc([100, 100, 400, 400], 120, 180, fill=int(values[2]), width=40)
    draw.arc([100, 100, 400, 400], 180, 240, fill=int(values[1]), width=40)
    draw.arc([100, 100, 400, 400], 240, 300, fill=int(values[0]), width=40)
    draw.arc([100, 100, 400, 400], 300, 0, fill=int(values[5]), width=40)

    draw.arc([145, 145, 355, 355], 0, 60, fill=int(values[10]), width=40)
    draw.arc([145, 145, 355, 355], 60, 120, fill=int(values[9]), width=40)
    draw.arc([145, 145, 355, 355], 120, 180, fill=int(values[8]), width=40)
    draw.arc([145, 145, 355, 355], 180, 240, fill=int(values[7]), width=40)
    draw.arc([145, 145, 355, 355], 240, 300, fill=int(values[6]), width=40)
    draw.arc([145, 145, 355, 355], 300, 0, fill=int(values[11]), width=40)

    draw.arc([190, 190, 310, 310], 45, 135, fill=int(values[14]), width=40)
    draw.arc([190, 190, 310, 310], 135, 225, fill=int(values[13]), width=40)
    draw.arc([190, 190, 310, 310], 225, 315, fill=int(values[12]), width=40)
    draw.arc([190, 190, 310, 310], 315, 45, fill=int(values[15]), width=40)

    draw.arc([235, 235, 265, 265], 1, 0, fill=int(values[16]), width=40)

    points = [(225, 120), (125, 180), (125, 315), (230, 375), (325, 340), (345, 170), (225, 165), (155, 210), (155, 280), (220, 330), (310, 280), (315, 215), (240, 210), (195, 250), (235, 285), (275, 250), (236, 247)]
    
    for i in range(17):
        level = values[i]*6/256
        print(str(i+1)+". Pixel value: "+str(int(values[i]))+" and Level: "+str(level))
        draw.text(points[i], str(round(level,3)))

    del draw
    output = np.array(canvas)
    return output