def createAccount():
    usr = input("Enter new username: ")
    pswd = input("Enter Password: ")
    with open("account_details.txt", 'a') as f:
        f.write(f"\n{usr}")
        f.write(f"\n{pswd}")
        
def login():
    usr = input("Username: ")
    
    with open("account_details.txt", 'r') as f:
        users = f.readlines()
    
    username = True
    userList = []
    passwords = []
    for i in users:
        if username == True:
            userList.append(i.strip())
            username = False
        elif username == False:
            passwords.append(i.strip())
            username = True
    
    if usr in userList:
        pswd = input("Password: ")
        if passwords[userList.index(usr)] == pswd:
            print("Logged in")
        else:
            print("password incorrect")
    else:
        print("Username not found")
