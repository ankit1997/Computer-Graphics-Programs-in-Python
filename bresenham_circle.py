import turtle

print("Bresenham's circle drawing algorithm implementation.")

xCenter = int(input("Enter Xc: "))
yCenter = int(input("Enter Yc: "))
radius = int(input("Enter radius: "))

window = turtle.Screen()
pointer = turtle.Turtle()
pointer.shape("arrow")
pointer.hideturtle()
pointer.pensize(2)

def setPixel(x, y):
    x = round(x)
    y = round(y)

    print("Plotting : (%s, %s)" % (x, y))
    try:
        pointer.penup()
        pointer.setx(x)
        pointer.sety(y)
        pointer.pendown()
        pointer.goto(x, y)
        
    except:
        pass

def circlePlotPoints(xCenter, yCenter, x, y):
    setPixel(xCenter+x, yCenter+y)
    setPixel(xCenter-x, yCenter+y)
    setPixel(xCenter+x, yCenter-y)
    setPixel(xCenter-x, yCenter-y)
    setPixel(xCenter+y, yCenter+x)
    setPixel(xCenter-y, yCenter+x)
    setPixel(xCenter+y, yCenter-x)
    setPixel(xCenter-y, yCenter-x)
    print()

def bresenham_circle(xCenter, yCenter, radius):
    x = 0
    y = radius
    d = 3-2*radius

    while x<y:
        circlePlotPoints(xCenter, yCenter, x, y)
        x = x + 1
        if d<0:
            d = d + 4*x + 6
        else:
            y = y - 1
            d = d + 4*(x-y) + 10
        circlePlotPoints(xCenter, yCenter, x, y)

bresenham_circle(xCenter, yCenter, radius)

try:
    window.mainloop()
except:
    pass
