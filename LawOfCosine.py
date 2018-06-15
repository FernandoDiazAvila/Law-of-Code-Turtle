import math
from turtle import *

##Law of Cosine
def mytriangle():
    firstSide= int(input("Anumber"))
    secondSide= int(input("someNumber"))
    firstAngle= int(input("numbers"))

    thirdSide = (pow(firstSide,2)+(pow(secondSide,2))- ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle)))))
    thirdSide1 = pow(thirdSide,0.5)

    secondAngle = math.acos(((pow(secondSide,2)) - (pow(firstSide,2)) - (pow(thirdSide1,2))) / ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1 = math.degrees(secondAngle)
    thirdAngle = 180 - (firstAngle) - (secondAngle1)




    ## TURTLE DRAWING ##
    drawing = Turtle()
    drawing.goto(0,0)
    drawing.down()
    drawing.forward(firstSide)
    drawing.left(180 - thirdAngle)
    drawing.forward(secondSide)
    drawing.left(180 - firstAngle)
    drawing.forward(thirdSide1)
if __name__ =="__main__":
    mytriangle()


    print("First Angle: ")
    print(firstAngle)
    print("Second Angle: ")
    print(secondAngle1)
    print("Third Angle: ")
    print(thirdAngle)
