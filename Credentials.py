class Credentials:
    """
    Credentials class to generate instances of account credentials
    """
    def __init__(self,accountname, username, passcode):#properties for each credentials object
        self.accountname = accountname
        self.username = username
        self.passcode = passcode

    credentialsList =[] #Empty list for object credentials
