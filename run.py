#!/usr/bin/env python3.8
from User import User
from Credentials import Credentials

def create_useraccount(firstName, lastName, userName, password):
    new_user = User(firstName, lastName, userName, password)
    return new_user

def save_user(User):
    User.save_user()

def delete_user(User):
    User.delete_user

def find_user(name):
    return User.find_by_name()

def display_user():
    return User.display_user()

def isexist_user(userName):
    return User.user_exists(userName)


def create_accountcredentials(account, username, passcode):
    new_account = Credentials (account, username, passcode)
    return new_account

def save_account(Credentials):
    Credentials.save_account()

def delete_account(Credentials):
    Credentials.delete_account()

def display_account():
    return Credentials.display_account()

def isexist_account(account):
    return Credentials.account_exists(account)



def main():
    while True:
        print("Hey, Welcome to Password Locker!")
        print("Use: 1 - to sign up as a new user, 2 - to login, 3 - to find a user, 4 - to exit")

        code = int(input())
        if code == 1:
            print("Create Account")
            print("*"*10)

            print("Enter your First Name")
            firstName = input()

            print("Enter your Last Name")
            lastName = input()

            print("Enter your username")
            userName = input()

            print("Enter your password")
            password = input()
            print("*"*10)

            save_user(create_useraccount(firstName, lastName, userName, password))

            print("Your user account has been successfully created!")
            print("*"*10)


        # elif code == 2:
        #     print("Enter your username")
        #     username = input()

        #     print("Enter your password")
        #     password = input()

        #     account = find_user(name)
        #     if account.name == username and account.password == password:
        #         print("Login successful")
            
        #     if 

if __name__ == '__main__':

    main()

    