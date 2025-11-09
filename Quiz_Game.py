print("Welcome to Quiz!")
playing=input("Do you want to play? ")

if playing.lower() !="yes" :
    quit()

print("Okay! Let's play :")
print("(Type your answers in lowercase letters)")
score=0
answer=input("What is the full form of ROM ? ").lower()
if answer == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is Read Only Memory.")

answer=input("What is the full form of CPU? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")

answer=input("What is the full form of RAM? ").lower()
if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is Random Access Memory.")

answer=input("What is the full form of HTML? ").lower()
if answer == "hyper text markup language":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is Hyper Text Markup Language.")

answer=input("What is the full form of GPU? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is Graphics Processing Unit.")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score/5)*100) + "%")
