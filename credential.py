class Credential:
    """
    Class that generates new instances of user.
    """
    credential_list = [] # Empty contact list

    def __init__(self,account,acc_username,acc_password):
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password
