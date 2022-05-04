#Q1 Write a program to convert string to interger
#assign a string to a variable
a="10"
#convert string to integer
b=int(a)
print(b,type(b))
#Q2 convert character to integer
#assign a character to a variable
c="A"
d=ord(c)
print(d,type(d))
#Q3 convert integer to character
#assign a ASCII value to a variable
e=68
f=chr(e)
print(f,type(f))
#Q4 convert floating point to integer
#assign a floating point a variable
import math
g=10.5
print("g=",g)
print("int(g)",int(g))
print("floor(g)",math.floor(g))#always round of the smallest integer
print("ceil(g)",math.ceil(g))# always rounds of to the larger integer
print("trunc(g)",math.trunc(g))#same as "int()"


