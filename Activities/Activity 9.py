#Act 9
#first variable "q" stores a list of questions that're going to be asked
q=["First Name:","Last Name:","Birthplace:","School:","Favourite Subject:"]#"q" for questions

#second variable "ui" acts a list that stores user inputted answers
u=[]#"u" for user

for i in range(len(q)):

      #third variable used to temporarily store answers to questions
      inp=input(q[i])#"inp" for input

      #the answer is added to the empty list "ui" and stored there
      u.append(inp)


print("")
print( "To Whom This May Concern:")
print("My name is",u[0],u[1]+".I am originated from",u[2]+".I am currently attending\n"+u[3],"with my favourite courses as",u[4]+".")
print("")
print("Sincerely,")
print(u[0],u[1])