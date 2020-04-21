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
        self.new_user = User("kevzzz","ximss") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''    
