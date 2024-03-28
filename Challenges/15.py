"""
Passwords are validated by comparing a user-provided
value with a known value that’s stored. Either it’s correct or
it’s not.
Create a simple program that validates userlogin credentials.
The program must prompt the user for a username and
password. The program should compare the password given
by the user to a known password. If the password matches,
the program should display “Welcome!” If it doesn’t match,
the program should display “I don’t know you.”

input: username, password
processes: compare password
output: message

Dependencies: pip install bcrypt==3.2.0

"""
import getpass
import bcrypt

#map
usuarios = {
    "axel": bcrypt.hashpw(b"luffy24", bcrypt.gensalt()),
    "andrade": bcrypt.hashpw(b"robin28", bcrypt.gensalt()),
    "villalobos": bcrypt.hashpw(b"yamato29", bcrypt.gensalt())
}

def login2(user, password):
    if user in usuarios and bcrypt.checkpw(password.encode('utf-8'), usuarios[user]):
        print("Welcome!")
    else:
        print("I don't know you.")

def login(user, password):
    if user == "admin" and password == "12345":
        print("Welcome!")
    else:
        print("I don't know you.")


user = input("Insert your username: ")
password = getpass.getpass("Insert your password: ")

login2(user,password)