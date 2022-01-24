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
        Credentials.credentialsList.append(self)

    def delete_account(self):
        Credentials.credentialsList.remove(self)

    # @classmethod
    # def find_by_username(cls, username):
    #     for Credentials in cls.credentialsList:
    #         if Credentials.username == username:
    #             return username

    @classmethod
    def display_account(cls):
        return cls.credentialsList

    @classmethod
    def account_exists(cls, account):
        for Credentials in cls.credentialsList:
            if Credentials.account == account:
                return account
        return False 
