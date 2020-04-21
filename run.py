#!/usr/bin/env python3.6

from user import User

from credential import Credential 

#==== create user account ======
def create_user(f_name,s_name):
    '''
    Function to create a new user
    '''
    new_user = User(f_name,s_name)
    return new_user

#===== save the newly created account ====
def save_user(user):
    '''
    Function to save user
    '''
    User.save_user(user)

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

#==== verify existing user ==============
def check_existing_users(f_name):
    '''
    Function that checks if a user exists with that name and return boolean
    '''

    return User.user_exist(f_name)

#====== create a credential =====
def create_credential(account,acc_username,acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,acc_username,acc_password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()

def gen_password():
    '''
    Function that generates a password
    '''
    gen_pass = Credential.gen_password()
    return gen_pass

#===== delete an obsolete credential =======
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(acc_username):
    '''
    Function that finds a credential
    '''
    return Credential.find_account_by_username(acc_username)


#======= checking for existing credential =======
def check_existing_credentials(acc_username):
    '''
    Function that checks if a credential exists
    '''
    return Credential.credential_exist(acc_username)

#======= view/display all credentials =======
def display_credential(acc_username):
    '''
    Function that returns all saved credentials
    '''
    return Credential.display_credential(acc_username)

def main():
    print("Hello.Please Input your name : ")
    your_name = input()
    print(f"Hey there {your_name}! Welcome to Password Locker. ")
    print(' ')
    print('\n')

    while True:
        print('Welcome!')
        print(' ')
        print('''Let's explore these Password Locker Options: - Select from: 
              1 - Create a password Locker account
              2 - Log into an existing password locker account
              3 - Create new credential
              4 - Display credential
              5 - Find a credential
              6 - Delete credential
              x - Exit the credential display mode''')



        short_code = input("input a password locker option :").lower().strip()
        if short_code == "x":
            break 
            
        elif short_code == '1':
            print("-" * 10)
            print("New Password locker account")
            print("-" * 10)

            f_name = input("input your first name : ").strip()
            s_name = input("input your second name : ").strip()

            save_user(create_user(f_name,s_name)) #create and save new user
            print ("")
            print (f"new password locker account for: {f_name}  {s_name} created")
            
        elif short_code == '2':
            print ("-" *40)
            print(' ')
            print(f"Fill in your details to log into your account")

            f_name = input("input your first name : ").strip()
            s_name = input("input your second name : ").strip()

            for user in User.user_list:
                if user == f_name and  s_name :
                    print ("You are already registered")
                else :
                    print("You are already logged in to the account")
                break 
                
            
        elif short_code == '3':
            print(' ')
            print("Create new credential")
            print("-"*100)
            account= input(" Enter the Account name : ").strip()
            acc_username = input ("Enter your prefered Account username : ").strip()

            while True:
                print(' ')
                print("-" *60)
                print("Please choose one of these:")
                print("a - Enter password")
                print("b - Generate password")
                password_choice = input("Enter your choice").lower().strip()
                print("-"*60)
                if password_choice == 'a':
                    print(" ")
                    acc_password = input("Enter your password : " ).strip
                    break
                elif password_choice == 'b':
                    password_choice= gen_password()
                    break
                else:
                    print("Please try again")

            save_credential(create_credential(account,acc_username,acc_password)) #create and save new credentials
            print ('')
            print(f"New Credential is  {account}, [ {acc_username} ]  [ {acc_password} ] ")
            print('')
            
        elif short_code == '4':
            print(' ')
            if display_credential(acc_username):
                print("Here is a list of all your credentials") .lower().strip()
                print(' ')

                for credential in display_credential(acc_username):
                    print(f"Account: {credential.account} Account Username{credential.acc_username} Account Password:{credential.acc_password}")
                    print(' ')
            else:
                print(' ')
                print("There are no credentials saved")
                print(' ')
            
        elif short_code == '5':
            print("Enter your account username:")

            search_accountusername = input()
            if check_existing_credentials (search_accountusername):
                found_username = find_credential(search_accountusername)
                print(' ')
                print("Here are your saved credentials")
                print(f'Account:{found_username.account}, Account username:{found_username.acc_username}, Account Password: {found_username.acc_password}')
                print(' ')
            else:
                print("That username does not exist")
                print(' ')
        elif short_code == '6':
            print( 'Delete a credential you no longer need')
            print( ' ')
            to_delete = input('Search for the account to delete:')
            if check_existing_credentials(to_delete):
                search_accountusername = find_credential(to_delete)
                print(' ')
                confirm = input("Confirm delete: yes or no")
                if confirm == 'yes':
                    del_credential(search_accountusername)
                    print('Delete successful')
                    print(' ')
                    break
                elif confirm == 'no':
                    continue
                else:
                    print('Credential does not exist')
                    print(' ')
                    break 
        elif short_code == 'x':
            print(' ')
            print("Thank you for your time.Goodbye!")
            print(' ')
            break
        else:
            print("Sorry,I didn't quite catch that, Please use the given short codes.")

if __name__ == '__main__':
    main()

    



                

                

                

