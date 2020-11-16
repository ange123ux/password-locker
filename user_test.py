import unittest
from user import User
from user import Account
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Angel", "Uwimana", "Angel", "angel2020")
    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Angel")
        self.assertEqual(self.new_user.last_name, "Uwimana")
        self.assertEqual(self.new_user.login_username, "Angel")
        self.assertEqual(self.new_user.password, "angel2020")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user listed
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Doria", "Igiraneze","Doria", "Doria2020")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Angelique", "Mizero", "Angelique","Angelique2020")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display information
        '''
        self.new_user.save_user()
        test_user = User("Angelique", "Mizero", "Angelique", "Angelique2020")
        test_user.save_user()
        found_user = User.find_by_login_username("Angelique")
        
        self.assertEqual(find_user.login_username,test_user.login_username)
    
    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by their password
        '''
        self.new_user.save_user()
        test_user = User("Ange", "Uwimana", "Ange", "ange2020")
        test_user.save_user()
        found_password = User.find_by_userpassword("ange2020")
        self.assertEqual(found_password.password,"ange2020")

    def test_display_user_information(self):
        '''
        test to check if we can be able to display users saved in user_list
        '''
        self.assertEqual(User.display_userInfo(),User.user_list)

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("Instagram", "Uwimana", "ange2020")
    def test_init(self):
        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.account_username,"Uwimana")
        self.assertEqual(self.new_account.account_password,"ange2020")
    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        Account.account_list = []
    def test_display_account_credentials(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("Twitter", "angeange", "angeange2020")
        test_account.save_account()
        test_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_name(self):
        self.new_account.save_account()
        test_account = Account("Facebook", "uwimana", "1234567")
        test_account.save_account()
        found_account = Account.find_by_accountName("Facebook")
        self.assertEqual(found_account.account_name,"Facebook")
if __name__ == '__main__':
    unittest.main()



























