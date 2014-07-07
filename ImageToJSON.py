#! /Users/jandro/anaconda/bin/python

import numpy as np
import sys
from PIL import Image


"""Convert a color in 0-255 integer range to a string
of length 2 where digits are the integer converted to hex."""
def convertColorToHex(color):
    number = str(hex(color))
    start = number.find('x')+1
    end = number.find('L')
    if (end > start): number = number[start:end]
    else: number = number[start:]
    if len(number) < 2: number = "0"+number
    return number

"""Converts individual pixel to string prepped for JSON."""
def prepPixelForJSON(pixel):
    asJson = "\""+pixel[0]+"\":\""
    asJson += (str(pixel[1])+str(pixel[2])+str(pixel[3])+"\"")
    return asJson
 
"""Converts a Numpy Array representation of an image into a list where
   each element holds key/value pair in a string formatted to be inserted
   into a json object.  The key is a position in array, the value is a 
   string representation of color."""    
def prepImageForJSON(image):
    in2D = []
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            pixel = [str(i)+"-"+str(j)]
            for k in range(0, len(image[0][0])):
                color = convertColorToHex(image[i][j][k])
                pixel.append(color)
            in2D.append(prepPixelForJSON(pixel))
    return in2D          


"""Converts Numpy Array representation of image to a json format.
   Input  : image as Numpy Array, expects 3D rgb for the array.
   Output : json string representing color by array position
            with keys of form "i-j" where i is the row, j
            is the column in grid representation of image."""
#
#todo: currently converting to javascript file containing json object.
#       must convert to full on json when server side set up.
#            
def imageToJSON(image, size, pixelSize):
    converting = prepImageForJSON(image)
    json =  "{\"size\": ["+str(size[0])+","+str(size[1])+"],"
    json += "\"pixelSize\":"+str(pixelSize)+","
    json += "\"image\":{"
    for i in range(0, len(converting)-1):
        json += (converting[i]+",\n")
    
    json += (converting[len(converting)-1]+"}}")
    return json

def convertImageToJSON(imageFile, jsonFile, newSize, pixelSize):
    #Read in and resize
    imPIL = Image.open(imageFile)
    imPIL = imPIL.resize(newSize)
    imNP = np.array(imPIL)
    
    #Convert
    json = imageToJSON(imNP, newSize, pixelSize)
    
    #Print out
    file = open(jsonFile, 'w')
    file.write(json)
    file.close()
 
 
#Drive program. 
#print "\n\n\n\n\n\n\n\n\n"
print "In ImageToJSON: ", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

convertImageToJSON(sys.argv[1],sys.argv[2], (int(sys.argv[3]),int(sys.argv[4])), int(sys.argv[5]))
