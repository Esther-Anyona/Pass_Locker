class User:
    """
    This is a class for generating new instances of users
    """
    userList = []
    def __init__(self, firstName, lastName, userName, password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password

    def save_user(self): #saves a user object to userList
        User.userList.append(self)

    def delete_user(self): #deletes a user object
        User.userList.remove(self)

    @classmethod
    def find_by_name(cls, name):
        """
        Method for finding users from the user list
        """
        for User in cls.userList:
            if User.userName == name:
                return User

    @classmethod
    def display_user(cls):
        """
        A class method to display existing accounts
        """
        return cls.userList

    @classmethod
    def user_exists(cls, userName):
        """
        Method for checking whether a certain account exists using username
        """
        for User in cls.userList:
            if User.userName == userName:
                return True
        return False
