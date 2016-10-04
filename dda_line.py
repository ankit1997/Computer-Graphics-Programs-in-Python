import turtle

print("DDA line drawing algorithm implementation.")

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

def dda_line(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1

    x = x1
    y = y1
    
    steps = 0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xIncr = dx/(float)(steps)
    yIncr = dy/(float)(steps)

    setPixel(x, y)
    for i in range(0, steps):
        x += xIncr
        y += yIncr
        setPixel(x, y)

dda_line(x1, y1, x2, y2)

try:
    window.mainloop()
except:
    pass
