import pyperclip

global user_list
class User:
    """
    Class that generates new instances of user.
    """
    user_list = [] # Empty user list

    def __init__(self,f_name,s_name):
        self.f_name = f_name
        self.s_name = s_name

    def save_user (self):
        '''
        save user method saves contact
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)   

    @classmethod
    def user_exist(cls,f_name):
        current_user = ''
        for user in cls.user_list:
            if user.f_name == f_name:
                current_user = user.f_name
            return current_user

        