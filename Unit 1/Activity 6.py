"""
#Q1
list=[]
for i in range(4):
    n=int(input("Enter the integers you want in a list:"))
    list.append(n)
print("this is your list:",list)
q=int(input("Which index would u like to remove:"))
list.remove(q)
print("this is your new list:", list)

#Q2
#linear search
list=[3,5,17,69]
l=len(list)
located=False
locate=int(input("What number do you want to search:"))
for i in range(l):
    if locate == list[i]:
        located= True
        break
if located==True:
    print("Your number has been found")
else:
    print("Your number couldn't be found")

#binary search
list=[5,16,17,20,69,420]
list.sort()
n=len(list)
locate=int(input("Enter the integer you want to search:"))
start=0
end=n-1
located=False
while start <= end and located==False:
    mid=(start+end)//2
    if locate==list[mid]:
        located=True
    elif locate > list[mid]:
        start =  mid + 1
    else:
        end= mid - 1
if located==True:
    print("found")
else:
    print("not found")

#Q3
#bubble sort
list=[19,12,15,16,69,42,1]
n=len(list)
for i in range(n):
    print("Pass:",i,list)
    swap = False
    for j in range(n-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            swap = True
    if swap == False:
        break

#insertion sort
A = [5,17,14,3,1]
for i in range(1,len(A)):
    j = i
    while A[j-1] > A[j] and j>0:
        A[j-1],A[j]=A[j],A[j-1]
        j -= 1

print(A)
#selection sort
B=[6,17,13,69,70,40]
n=len(B)
for i in range(n):
    minpos=i
    for j in range(i+1,n):
        if B[j]<B[i]:
            minpos = j
    B[i],B[minpos]=B[minpos],B[i]
    print(B)
"""
#Q4
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("Enter your integer:"))
print("The factorial of",num,"is",fact(num))



