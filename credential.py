import string
import random

global credential_list 
class Credential:
    """
    Class that generates new instances of user.
    """
    credential_list = [] # Empty credential list
    

    def __init__(self,account,acc_username,acc_password):
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credential (self):
        '''
        save credential method saves credentials
        '''
        Credential.credential_list.append(self)

    @classmethod
    def find_account_by_username(cls,acc_username):
       

        for credential in cls.credential_list:
            if credential.acc_username == acc_username:
                return credential    

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
    
   

    def gen_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		
		   gen_pass=''.join(random.choice(char) for _ in range(size))
		   return gen_pass

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    
    @classmethod
    def credential_exist(cls,acc_username):
        '''
        Method that checks if a credential exists from credential list
        '''
        for credential in cls.credential_list:
            if credential.acc_username == acc_username:
                return True

        return False

    @classmethod
    def display_credential(cls,acc_username):
        '''
        Method that returns the credential list
        '''
        return cls.credential_list
