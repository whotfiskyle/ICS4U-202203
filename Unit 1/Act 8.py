"""
#Q1
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
C = [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
for i in range(len(A)):
  for j in range(len(B[0])):
      for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
for r in C:
    print(r)

#Q2
n2={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",\
   6:"Six", 7:"Seven", 8:"Eight",9:"Nine",10:"Ten",\
    11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen",\
    15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",\
    19:"Nineteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",\
    60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",0:"Zero"}
p=int(input("Enter your number:"))
l=len(str(p))
if p<0 or l > 3:
    print("Number out of range")
elif n2.get(p) != None:
    print(n2[p])
elif l == 3:
    h=p//100#first digit of three
    m=p%100#2 digits
    if m==00:
        print(n2[h],"Hundred")
    else:
        t=m-(m%10)#tens from n2
        s=m%10#single digit
        if s==0:
            print(n2[h],"Hundred",n2[t])
        else:
            print(n2[h],"Hundred",n2[t],n2[s])
else:
    print(n2[p-p%10], n2[p%10])
#Q3




#Q4
t=int(input("how many Fibonacci numbers would you like:"))
n1=0
n2=1
print(n1,n2,end=" ")
for i in range(t-2):
    n3=n1+n2
    print(n3, end=" ")
    n1,n2=n2,n3

#Q5
#character to ASCII code
f=input("Enter your characters:")
for i in f:
    print(i,ord(i))
#ASCII to character
p=input("Enter your ASCII codes:")
codes=p.split(" ")
list=[]
for u in range(len(codes)):
    a=int(codes[u])
    list.append(a)
for l in list:
    print (chr(l), end=" ")
"""
