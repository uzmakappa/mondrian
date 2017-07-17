import random
from turtle import *

def drawSquare (w):
    """Using turtle graphics, draw a square centered at the origin.
    
    Params:
        w (int): 1/2 side length of square
    """
    
    up ()
    goto (-w, -w)
    down ()
    for i in range(4):
        forward (2*w)
        left (90)
    
#drawSquare (200)


def horizontalLine (x1, x2, y):
    """Using turtle graphics, draw a horizontal line segment.
    
    Params:
        x1 (float): x-coordinate of first endpoint of line segment
        x2 (float): x-coordinate of second endpoint of line segment
        y (float): y-coordinate of both endpoints of line segment
    """
    
    up ()
    goto (x1,y)
    down ()
    goto (x2, y)
    up ()
    
#horizontalLine (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))


def verticalLine (x, y1, y2):
    """Using turtle graphics, draw a vertical line segment.
    
    Params:
        x (float): x-coordinate of both endpoints of line segment
        y1 (float): y-coordinate of first endpoint of line segment
        y2 (float): y-coordinate of second endpoint of line segment
    """
    
    up ()
    goto (x,y1)
    down ()
    goto (x, y2)
    up ()
    
#verticalLine (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

def fillRect (q,r,s,t,c):
    """Using turtle graphics, draw color-filled rectangle.
    
    Params:
        q (int 2-tuple): coordinates first corner of rectangle
        r (int 2-tuple): coordinates second corner of rectangle
        s (int 2-tuple): coordinates third corner of rectangle
        t (int 2-tuple): coordinates fourth corner of rectangle
        c (str): fill color of rectangle
    """
   
    up ()
    goto (q)
    down ()
    fillcolor (c)
    begin_fill()
    goto (r)
    goto (s)
    goto (t)
    goto (q)
    end_fill ()


def art (w):
    """Using turtle graphics, create art in the style of Mondrian.
    
    Params: 
        w (int): painting should fit in the square with corners [+-w, +-w]
    """
    
    speed (0)
    pensize (5)
    drawSquare (w)
    horizontal = []
    for i in range (random.randint(5,10)):
        z = random.randint(-w,w)
        horizontal.append(z)
        horizontalLine (w, -w, z)
    vertical = []
    for i in range (random.randint(5,10)):
        z = random.randint(-w,w)
        vertical.append(z)
        verticalLine (z, w, -w)
    colors = ['red', 'yellow', 'blue']
    for i in range(3):
        y1 = horizontal[random.randint(1, len(horizontal)-1)]
        horizontal.remove(y1)
        y2 = horizontal[random.randint(1, len(horizontal)-1)]
        x1 = vertical[random.randint(1, len(vertical)-1)]
        vertical.remove(x1)
        x2 = vertical[random.randint(1, len(vertical)-1)]
        fillRect ((x1,y1),(x1,y2),(x2,y2),(x2,y1),colors[i])
        
    
art (300)
done ()         
