import math
import turtle
bob = turtle.Turtle()

def spuare(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# spuare(bob, 100)

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polygon(bob, 10, 60)


def rawCircle(t, r):
    n = 70
    length = (2 * 3.14 * r) / n
    polygon(t, length, n)

# rawCircle(bob, 30)

def circle(t, r):
    circumference = 2 * 3.14 * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

# circle(bob, 40)

def arc(t, r, angle):
    circumference = 2 * 3.14 * r
    curve_len = circumference *angle / 360
    n = int(curve_len / 3) + 1
    length = curve_len / n
    ext_angle = angle / n
    for i in range(n):
        t.fd(length)
        t.lt(ext_angle)

arc(bob, 200, 120)

#to generalize no. of sides, divide curve length by 3 and  add 3.
# to calculate steplength divide curve length by n
#the step length always comes approx 3
turtle.mainloop()
