t=input("What are your three integers:")
a,b,c= t.split(",")
a=int(a)
b=int(b)
c=int(c)
if a==b and b==c and a==c:
    print("3")
elif a==b and b!=c:
    print("2")
else:
    print("0")

