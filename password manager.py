

master_p=input("what is the master password? ")

def view():
    with open("passwords.txt","r") as f:
        for line  in f.readlines():
            print(line.rstrip())
def add():
    name= input("Account name: ")
    p=input("password: ")
    with open("passwords.txt","a") as f:
        f.write(name + " " + p + "\n")
while True:
    mode=input("would you like to add new password or view existing ones (view,add)? or press q to quit ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid choice")
        continue


