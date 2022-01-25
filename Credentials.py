import random
import string
import pyperclip # module to enable the user to copy the system generated passcode

class Credentials:
    """
    Credentials class to generate instances of account credentials
    """
    def __init__(self,account, username, passcode):#properties for each credentials object
        self.account = account
        self.username = username
        self.passcode = passcode

    credentialsList =[] #Empty list for object credentials

    def save_account(self):
        """
        Method for saving newly created account credentials
        """
        Credentials.credentialsList.append(self)

    def delete_account(self):
        """
        Method for deleting existing account credentials
        """
        Credentials.credentialsList.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for Credentials in cls.credentialsList:
            if Credentials.username == username:
                return Credentials

    @classmethod
    def display_account(cls):
        """
        A class method to display existing accounts
        """
        return cls.credentialsList

    @classmethod
    def account_exists(cls, account):
        """
        A class method to check if a particular account exists using the account name
        """
        for Credentials in cls.credentialsList:
            if Credentials.account == account:
                return account
        return False 

    @classmethod
    def generate_passcode(self):
        """
        Method to generate a random passcode of mixed characters and length 10
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        generate_passcode = "".join(random.choice(characters) for i in range(10))
        pyperclip.copy(generate_passcode)
        return generate_passcode
