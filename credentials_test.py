import unittest
from Credentials import Credentials


class TestCredentials(unittest.TestCase):
    def tearDown(self):
        """
        Cleans the credentialsList before every test
        """
        Credentials.credentialsList =[]

    def setUp(self):
        self.new_credentials = Credentials("twitter", "kays", "K321")

    def test_init(self):
        self.assertEqual(self.new_credentials.accountname, "twitter")
        self.assertEqual(self.new_credentials.username, "kays")    
        self.assertEqual(self.new_credentials.passcode, "K321")    
