import unittest # Python test framework

from User import User

class TestUser(unittest.TestCase):
    """
    subclass to define test cases for the user class behaviors
    """
    def setUp(self):
        self.new_user =User("Esther", "Anyona", "Star", "Es123" )

    def test_init(self):
        self.assertEqual(self.new_user.firstName, "Esther")
        self.assertEqual(self.new_user.lastName, "Anyona")
        self.assertEqual(self.new_user.userName, "Star")
        self.assertEqual(self.new_user.password, "Es123")

if __name__ == '__main__':
    unittest.main()
