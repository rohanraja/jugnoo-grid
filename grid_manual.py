from helpers import *
import cv2
import imutils
import json


testImage = "test_images/grid2.jpg"

img = readImg(testImage)
img = imutils.resize(img, width=900)

cv2.imshow('image',img)

GRID = {}

kidx = 0

keys = ["x", "y", "origin"]

def nextKey():
    global kidx
    kidx = kidx + 1

pos = 0
curSet = []


def addToDict(x, y):
    global pos, curSet

    k = keys[kidx]
    if k not in GRID:
        GRID[k] = []

    if k == "origin":
        GRID[k] = [x,y]
        return

    curSet.append([x,y])

    if pos%2 == 1:
        GRID[k].append(curSet)
        curSet = []

    pos = pos + 1


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       # draw circle here (etc...)
       print('x = %d, y = %d'%(x, y))
       cv2.circle(img,(x,y), 5, (0,0,255), -1)
       cv2.imshow('image',img)
       addToDict(x,y)

cv2.setMouseCallback('image', onMouse)



def save():
    with open('grid.json', 'w') as fp:
        json.dump(GRID, fp)

