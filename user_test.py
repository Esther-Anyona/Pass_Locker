import unittest # Python test framework

from User import User

class TestUser(unittest.TestCase):
    """
    subclass to define test cases for the user class behaviors
    """
    def tearDown(self):
        User.userList = []

    def setUp(self):
        self.new_user =User("Esther", "Anyona", "Star", "Es123" )

    def test_init(self):
        self.assertEqual(self.new_user.firstName, "Esther")
        self.assertEqual(self.new_user.lastName, "Anyona")
        self.assertEqual(self.new_user.userName, "Star")
        self.assertEqual(self.new_user.password, "Es123")

    def test_save_user(self):#method for saving new user object
        self.new_user.save_user()
        self.assertEqual(len(User.userList),1)

    def test_save_multiple_user(self):#To check whether one can save multiple user objects in the userList
        self.new_user.save_user()
        test_user = User("John", "Doe", "Jodo", "JD123")#New user for testing
        test_user.save_user()
        self.assertEqual(len(User.userList),2)

    def test_delete_user(self): #Test to check if a user can be deleted from the userList
        test_user = User ("John", "Doe", "Jodo", "JD123")
        self.new_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.userList),0)
        
    def test_find_user_by_name(self):
        self.new_user.save_user()
        test_user = User ("John", "Doe", "Jodo", "JD123")
        test_user.save_user()
        found_user =User.find_by_name("Jodo")
        self.assertEqual(found_user.userName, test_user.userName)




if __name__ == '__main__':
    unittest.main()

