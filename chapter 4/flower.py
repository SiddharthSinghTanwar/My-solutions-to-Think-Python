import turtle
import math

# from inChapter_exercises import arc
bob = turtle.Turtle()

def arc(t, r, angle):
    circumference = 2 * 3.14 * r
    curve_len = circumference *angle / 360
    n = int(curve_len / 3) + 1
    length = curve_len / n
    ext_angle = angle / n
    for i in range(n):
        t.fd(length)
        t.lt(ext_angle)

def flower(f, r, angle, n):
    for i in range(n):
        for i in range(2):
            arc(f, r, angle)
            f.lt(180 - angle)
        f.lt(360 / n)

flower(bob, 140, 20, 10)

turtle.mainloop()