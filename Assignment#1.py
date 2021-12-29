#1

print('''Twinkle, twinkle, little star,
               How I wonder what you are!
                       Up above the world so high,
                       Like a diamond in the sky.
Twinkle, twinkle, little star,
               How I wonder what you are''')

#2
from platform import python_version
print(python_version())

#3
from datetime import datetime
current_date_time=datetime.now()
print(current_date_time)

#4
import math

radius=input("enter the radius of the circle (It must be a number): ")
r=int(radius)
area=2*math.pi*r
print(area)

#5

A=input("enter your name's first letter ")
B=input("enter your name's last letter ")
print(B+" "+A)

#6

v1=input("enter first number ")
v2=input("enter 2nd number ")
print(int(v1)+int(v2))


