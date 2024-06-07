import math
import cv2
import numpy as np

points = []
img = cv2.imread('ProblemStatement\Image-1.jpg',3)
def draw(event, x,y, flags, params):

    if event==cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])
        cv2.circle(img, (x,y), 5, (255,0,0), -1)
        if (len(points)!=0) :
            cv2.arrowedLine(img, tuple(points[0]),(x,y), (255,0,0),3)
        cv2.imshow('image', img)
        print(points)
        if len(points)%2==0:
            degrees = angle()

            print(abs(degrees))


def angle():
    a = points[-1]
    b = points[-2]

    m = slope(b,a)
    angle = math.atan(m)
    angle = round(math.degrees(angle))
    if angle<0:
        angle =-1*angle
    cv2.putText(img, str((angle)), (b[0]-40,b[1]+40), cv2.FONT_HERSHEY_DUPLEX, 2,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('image',img)
    return angle

def slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

while True:
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw)
    if cv2.waitKey(1)&0xff==ord('q'):
        break