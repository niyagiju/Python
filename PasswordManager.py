
def add():
    name=input("Account Name: ")
    pwd1=input("Password: ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd1 + "\n")
    
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("Account Name:",user,"| Password:",passw)

pwd=input("What is the master password?:" )
if pwd=="masterpassword":
    print("Access granted.") 
    while True:
        mode=input("Add new password or view existing ones or quit? (add/view) ").lower()
        if mode=="add":
            add()
        elif mode=="view":
            view()
        elif mode=="quit":
            break
        else:
            print("Invalid mode.")
            continue
else:
    print("Access denied.")
