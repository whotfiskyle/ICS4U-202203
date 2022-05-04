"""
#Q1
#user-defined class
import udf
obj=udf.udefined()
obj.subtract(12,4)
#libraries
import math
A=16
print(math.sqrt(A))
#modules
import calculate
calculate.add(12,4)
#Q2

list=[]
for i in range(5):
    n=int(input("Enter an integer:"))
    list.append(n)
list.sort()
print("This is your list:",list)

#linear search
print("Will commence linear search")
u=int(input("What integer would u like to search in the list?"))
located=False
for p in range(len(list)):
    if u==list[p]:
        located=True
        break
if located==True:
    print("Your item is found")
else:
    print("Your item is not in the list")

#binary search
print("Will commence binary search")
l=int(input("What integer would u like to search in the list?"))
start=0
end=len(list)-1
located=False
while start <= end and located==False:
    mid=start+end//2
    if l==list[mid]:
        located=True
    elif l >list[mid]:
        start=mid+1
    elif l <list[mid]:
        end=mid-1
if located==True:
    print("Your item is found")
else:
    print("Your item is not in the list")

#Q3

#polymorphism
#same function that can be used for different types

#built in polymorphic functions
print(len("Hi"))
print(len([12,15,18]))
#len can be used for both strings and lists

#creating a function to show polymorphism
def add(x,y,z=0):
    return print(x+y+z)
add(12,4)
add(12,4,5)

#method overloading
#a way of defining a method in a way that there are multiple ways to call it and specifying a method or function's parameters ourselves
#example
def speak(name=None):
    if name==None:
        print("Hello")
    else:
        print("Hello my name is", name)

speak("Kyle")
speak()

#inheritance
#capability of the properties in one class to be re- used in another class
class person:
    name=""
    def __init__(self,name):
        self.name=name
    def printname(self):
        print("Name:", self.name)
class driver(person):
    def driving(self):
       print("Driving")
obj1=person("Kyle")
obj1.printname()
obj2=driver("Rosa")
obj2.printname()
obj2.driving()

#encapsulation
#preventing the data from being accidently modified
class human:
    __legs=2
    __name="Kyle"
    def __int__(self):
        self.__legs=0
        self.__name="Diane"
        self.__walk()
    def person(self):
        print(self.__name,"has",self.__legs,"legs")
    def walk(self):
        print("walking")
obj1=human()
obj1.person()
obj1.__name="Samantha"
obj1.person()
obj1.walk()
"""

