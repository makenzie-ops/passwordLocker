import unittest # Importing the unittest module
from user import User
from credential import Credential # Importing the user and credential class
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("kevzzz","ximss") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''    
        self.assertEqual(self.new_user.f_name,"kevzzz")
        self.assertEqual(self.new_user.s_name,"ximss")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''    
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("name" ,"hey123")
        test_user.save_user()

        self.new_user.delete_user() #deleting a user
        self.assertEqual(len(User.user_list),1)   

    
class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("instagram" ,"african_beauty","selfcare3")
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []   
            User.user_list=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''    
        self.assertEqual(self.new_credential.account,"instagram")
        self.assertEqual(self.new_credential.acc_username,"african_beauty")
        self.assertEqual(self.new_credential.acc_password,"selfcare3")

    

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple contact
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","afroo","selfcare3") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2) 

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our cr4edential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("twitter","afroo","selfcare3")
        test_credential.save_credential()

        self.new_credential.delete_credential() #deleting a user
        self.assertEqual(len(Credential.credential_list),1)        

    def test_find_account_by_username(self):
        '''
        test to check if we can find an account by username and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("twitter","afroo","selfcare3") # new credential
        test_credential.save_credential()

        found_credential =Credential.find_account_by_username("afroo")

        self.assertEqual(found_credential.account,test_credential.acc_password,test_credential.acc_username)

    def test_display_credential(self):
        '''
        test whether one can view all the account credentials that they have created/saved
        '''
        self.new_credential.save_credential()
        account_2 = Credential("Facebook","Rihanna","mypassword")
        account_2.save_credential()
        credential_exists = Credential.display_credential("Facebook")
        self.assertEqual(credential_exists,account_2)
if __name__ == '__main__':
    unittest.main ()