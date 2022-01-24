import unittest
from Credentials import Credentials
import string


class TestCredentials(unittest.TestCase):
    def tearDown(self):
        """
        Cleans the credentialsList before every test
        """
        Credentials.credentialsList =[]

    def setUp(self):
        self.new_credentials = Credentials("twitter", "kays", "K321")

    def test_init(self):
        self.assertEqual(self.new_credentials.account, "twitter")
        self.assertEqual(self.new_credentials.username, "kays")    
        self.assertEqual(self.new_credentials.passcode, "K321") 

    def test_save_account(self):
        self.new_credentials.save_account()
        self.assertEqual(len(Credentials.credentialsList), 1)   

    def test_save_multiple_accounts(self):
        self.new_credentials.save_account()
        test_account = Credentials("facebook", "fbkay", "fb321")
        test_account.save_account()
        self.assertEqual(len(Credentials.credentialsList),2)

    def test_delete_account(self):
        self.new_credentials.save_account()
        test_account = Credentials("facebook", "fbkay", "fb321")
        test_account.save_account()
        self.new_credentials.delete_account()
        self.assertEqual(len(Credentials.credentialsList),1)

    # def test_find_account_by_name(self):
    #     self.new_credentials.save_account()
    #     test_account = Credentials("facebook", "fbkay", "fb321")
    #     test_account.save_account()
    #     found_account = Credentials.find_by_name('fbkay')
    #     self.assertEqual(found_account.username, test_account.username)

    def test_display_account(self):
        self.assertEqual(Credentials.display_account(), Credentials.credentialsList)

    def test_account_exists(self):
        self.new_credentials.save_account()
        test_account = Credentials("facebook", "fbkay", "fb321")
        test_account.save_account()
        account_exists = Credentials.account_exists('facebook')
        self.assertTrue(account_exists)



if __name__ == '__main__':
    unittest.main()
