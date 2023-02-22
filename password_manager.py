#Store password
from cryptography.fernet import  Fernet

#Key creation/loading
""" def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) """

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

""" create_key() """

#Creation of the master password
master_pwd = input("Please input your master password: ")
confirmation_pwd = input("Please confirm the password: ")

while master_pwd != confirmation_pwd:
    print("Oh! Your passwords don't match!")
    master_pwd = input("Please input your master password: ")
    confirmation_pwd = input("Please confirm the master password: ")

#Encryptation key + master password
key = load_key() + master_pwd.encode()
fer = Fernet(key)


#Menu logic for the app
def add():
    name_place = input("Name for the password: ")
    username = input("Account name/email: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name_place + "|" + username + "|" + fer.encrypt(password.encode()).decode() + "\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            nm, usr, pwd = data.split("|")
            print("Name:", nm, "\nUsername:", usr + "\n" + "Password:", fer.decrypt(pwd.encode()).decode())
        

print("--------------- MENU ---------------")
print("1. Add new password")
print("2. View current passwords")
print("3. Exit")
print("-------------------------------------")

while True:
    mode = input("\nType the number of the option: ")
    if mode == '3':
        break

    if mode == '1':
        add()
    elif mode == '2':
        view()
    else:
        print("Invalid option.")
        continue



print("\nThank you for using this password manager! :)\n")