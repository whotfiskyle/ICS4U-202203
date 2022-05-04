#Q1
#1D array
oneDarray=[2,4,5,6]
#2D array
twoDarray=[ [4,7,8,9],
           [3,8,3,6],
           [1,10,44,55]
           ]
print(oneDarray)
print(twoDarray)
print(twoDarray[1][2])

#Q2
data=[]
for i in range(5):
    n=int(input("Enter your integer:"))
    data.append(n)
data.reverse()
print(data)

#Q3
arrayA=[2,4,5]
arrayB=[6,7,8]
arrayC=[]

for o in range(3):
    arrayC.append(arrayA[o] + arrayB[o])
print(arrayA, "+", arrayB , "=", arrayC)

#Q4
arrayP=[]
product=1

import random
for y in range(20):
    c=random.randint(1,10)
    arrayP.append(c)
print(arrayP)
for j in arrayP:
    product = product * j
print(product)




