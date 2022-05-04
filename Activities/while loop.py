"""
#program that calculates the total and average for the input numbers
t= True
list=[]
while t==True:
    num=int(input("Enter a number:"))
    list.append(num)
    ask=input("Do you want to add more?(Yes/No):")
    if ask=="Yes" or ask=="yes":
        continue
    else:
        total=sum(list)
        avg=total/len(list)
        print("total:", total)
        print("average:", avg)
        t= False
"""
u= True
list=[]
while u== True:
    n=int(input("Enter your number:"))
    list.append(n)
    if n==0:
        print(list)
        print("Total:", sum(list))
        print("Avg:", sum(list)/len(list))
        u= False







