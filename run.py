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

def find_user(number):
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



    