
class User:
    """
    Class that generates new instances of user.
    """
    user_list = [] # Empty user list

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user (self):
        '''
        save user method saves contact
        '''
        User.user_list.append(self)