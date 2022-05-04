
#a=int(input("first integer:"))
#b=int(input("second integer:"))
#c=int(input("third integer:"))
#if a==b and a==c and b==c:
    #print(3)
#elif a==b and b!=c:
    #print(2)
#elif b==c and a!=b:
    #print(2)
#else:
    #print(0)

#i=int(input("Enter an integer:"))
#if i%5==0 and i%3==0:
    #print("It is divisible by both 3 and 5")
#elif i%5==0:
    #print("It is divisible by 5")
#elif i%3==0:
    #print("It is divisible by 3")
#else:
    #print("It is not divisible by both 3 and 5")

speed=int(input("What is the speed:"))
if speed<=70:
    print("OK")
else:
    pts=(speed-70)//5
    print("Points:",pts)
    if pts>12:
        print("License suspended")




