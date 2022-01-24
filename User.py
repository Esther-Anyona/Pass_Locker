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