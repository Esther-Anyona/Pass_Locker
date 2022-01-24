#!/usr/bin/env python3.8
from User import User
from Credentials import Credentials

def create_useraccount(firstName, lastName, userName, password):
    """
    Function to create a new user account
    """
    new_user = User(firstName, lastName, userName, password)
    return new_user

def save_user(User):
    """
    Function to save the newly created user account
    """
    User.save_user()

def delete_user(User):
    """
    Function to delete existing user account
    """
    User.delete_user

def find_user(userName):
    """
    Function to find a user by username
    """
    return User.find_by_name(userName)

def display_user():
    """
    Function to display existing users
    """
    return User.display_user()

def isexist_user(userName):
    """
    Method to check whether a user exists
    """
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
        print("**"*10)
        print("Use: 1 - to sign up as a new user, 2 - to login, 3 - to find a user, 4 - to exit")

        code = int(input())
        if code == 1: #sign-up
            print("Create User Account")
            print("*"*10)

            print("Enter your First Name")
            firstName = input()

            print("Enter your Last Name")
            lastName = input()

            print("Enter your username")
            userName = input()

            print("Enter your password")
            password = input()
            print("\n")
            save_user(create_useraccount(firstName, lastName, userName, password))
            print("Your user account has been successfully created!")
            print("\n")
            while True:
                print(f"Welcome {userName}, use the following code options to proceed")
                print ("**"*10)
                print("1 - save new passcode, 2 - Delete passcode, 3 - Display saved passcodes, 4 - log out ")

                option = int(input())
                if option ==1:
                    print("New Credentials")
                    print("*"*10)

                    print("Account Name")
                    account = input()

                    print("username")
                    username = input()

                    print("password")
                    passcode = input()
                    print("\n")

                    save_account(create_accountcredentials(account, username, passcode))

                elif option ==2:
                    print("Enter the name of account to delete")
                    print("*"*10)

                    account = input()
                    if isexist_account(account):
                        remove_account(account)
                        delete_account(remove_account)

                    else:
                        print(f"{account} account cannot be found")

                elif option ==3:
                    if display_account():
                        for account in display_account():
                            print(f"{account.account}:{account.passcode}")
                    else:
                        print("No passcode saved for this account")

                elif option ==4:
                    break

        if code == 2: #user login
            print("Enter username")
            userName = input()

            print("Enter your password")
            password = input()

            User.userName = find_user(userName)
            if User.userName == userName and User.password == password:
                print("Login successful")
                while True:

                    print(f"Welcome {userName}, use the following code options to proceed")
                    print("**"*10)
                    print("1 - save password, 2 - delete password, 3 - display saved passwords, 4 - log out")



if __name__ == '__main__':

    main()

    