import unittest # Importing the unittest module
from user import User
from credential import Credential # Importing the user and credential class

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
        self.assertEqual(self.new_user.user_name,"kevzzz")
        self.assertEqual(self.new_user.password,"ximss")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''    
        self.new_user.save_user()
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

if __name__ == '__main__':
    unittest.main ()