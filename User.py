class User:
"""
This is a class for generating new instances of users
"""
userList = []
def _init_(self, firstName, lastName, userName, password):
    self.firstName = firstName
    self.lastName = lastName
    self.userName = userName
    self.password = password