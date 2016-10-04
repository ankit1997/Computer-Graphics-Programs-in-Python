import turtle

print("Bresenham's line drawing algorithm implementation.")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

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

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    p = 2*dy - dx

    twoDyDx = 2*(dy-dx)
    twoDy = 2*dy

    x=0
    y=0
    xEnd=0

    if x1>x2:
        x = x2
        y = y2
        xEnd = x1
    else:
        x = x1
        y = y1
        xEnd = x2

    setPixel(x, y)

    while x<xEnd:
        x = x + 1
        if p<0:
            p = p + twoDy
        else:
            y = y + 1
            p = p + twoDyDx
        setPixel(x, y)

bresenham_line(x1, y1, x2, y2)

try:
    window.mainloop()
except:
    pass
