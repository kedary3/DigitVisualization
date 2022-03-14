# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:41:08 2022

@author: Kedar
"""

#this program converts the digit string of a number into a square image of color pixels representing the digits of said number.

import numpy as np
import decimal as dm
import matplotlib.colors as mcolors
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

PREC = 400
def getFrame(PREC,x1):

    colorNames = list(mcolors.TABLEAU_COLORS.items())
    colorValues = [""]*len(colorNames)
    for i in range(len(colorNames)):
        colorValues[i] = colorNames[i][1]
    
    dm.getcontext().prec = PREC  # Change the precision
    
    
    
    
    num=dm.Decimal(2).sqrt()
    
    numList=list([num.as_tuple()[1]][0])
    
    
    squareSize = int(np.ceil(np.sqrt(len(numList))))
    
    numList += [0] * (squareSize**2 - len(numList))
    numMap = np.reshape(numList, (squareSize ,squareSize ))
    
    
    colorMap = np.ndarray((squareSize ,squareSize ),dtype=np.dtype('U100'))
    for i in range(squareSize):
        for j in range(squareSize):
            colorMap[i][j] = colorValues[numMap[i][j]]
    
        
    w, h =  1000,1000
    
      
    # creating new Image object
    im = Image.new("RGB", (w, h),color="blue")
      
    # create rectangle image
    
    x = w/squareSize
    y = h/squareSize
    draw = ImageDraw.Draw(im)
    for j in range(squareSize):
        for  i in range(squareSize):
            shape = (i*x,j*y,i*x+x,j*y+y)
            draw.rectangle(shape,fill=colorMap[j][i])
          
    
    font = ImageFont.load_default()
    # draw.text((x, y),"Sample Text",(r,g,b))
 
    draw.text((0, 0),str(x1),(255,255,255),font=font)
    return im



images = []


for i in np.arange(1,2,1):
    im = getFrame(PREC,i)
    images.append(im)

images[0].save('sqrtFunc.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=20, loop=0)





