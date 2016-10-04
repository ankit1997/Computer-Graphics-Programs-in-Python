import turtle

print("Mid point circle drawing algorithm implementation.")

xCenter = int(input("Enter Xc: "))
yCenter = int(input("Enter Yc: "))
radius = int(input("Enter radius: "))

window = turtle.Screen()
pointer = turtle.Turtle()
pointer.shape("arrow")
pointer.hideturtle()
pointer.pensize(4)

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

def midpoint_circle(xCenter, yCenter, radius):
    x = 0
    y = radius
    p = 1-radius

    circlePlotPoints(xCenter, yCenter, x, y)

    while x<y:
        x = x + 1
        if p<0:
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*(x-y) + 1
        circlePlotPoints(xCenter, yCenter, x, y)

midpoint_circle(xCenter, yCenter, radius)

try:
    window.mainloop()
except:
    pass
