#! /Users/jandro/anaconda/bin/python

from PIL import Image
import numpy as np
import json
import sys

def getRedFrom(hex):
    return int(hex[:2],16)
    
def getBlueFrom(hex):
    return int(hex[2:4],16)
    
def getGreenFrom(hex):
    return int(hex[4:6],16)


def convertJSONToArray(jsonObject, array, size):
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            hexValue = jsonObject[str(i)+"-"+str(j)]
            array[i][j][0] = getRedFrom(hexValue)
            array[i][j][1] = getBlueFrom(hexValue)
            array[i][j][2] = getGreenFrom(hexValue)
            

def convertJSONToImage(jsonFile, imageFile, size, pixelSize):
    inFile = open(jsonFile, 'r')
    js = inFile.read()
    jsonObject = json.loads(js)
    
    im = np.zeros((size[0], size[1], 3), dtype="uint8")
    convertJSONToArray(jsonObject["image"], im, size)
    
    image = Image.fromarray(im)
    image = image.resize((size[0]*pixelSize, size[1]*pixelSize))
    image.save(imageFile)
    
#convertJSONToImage("/Users/jandro/Desktop/temp/inJSON/temp.json", "/Users/jandro/Desktop/temp/outImage/temp.jpg", (100,100), 5)

convertJSONToImage(sys.argv[1], sys.argv[2], (int(sys.argv[3]), int(sys.argv[4])), int(sys.argv[5]));