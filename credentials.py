#!/usr/bin/env python3.6
from user import User
from user import Account
def create_user(first_name, last_name, login_username, password):
    new_user = User(first_name, last_name, login_username, password)
    return new_user
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(username):
    return User.find_by_username(username)
def find_password(userpassword):
    return User.find_by_userpassword(userpassword)
def display_user():
    return User.display_userInfo()
def create_account(account_name,account_username,account_password):
    new_account = Account(account_name,account_username,account_password)
    return new_account
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def display_account_credentials():
    return Account.display_accounts()
def find_account_credentials(account_name):
    return Account.find_by_accountName(account_name)
def main():
    print("Enter your name")
    name = input()
    print(f"Hey {name} choose one of the options below:")
    print('\n')
    while True:
        print("Use the following code to signup: su - SignUp, lg - login, nw - Add New Account, da - Display Accounts, vw -View Account Details, dl - Delete Account Detaiils")
        user_choice = input().lower()
        if user_choice == "su":
            print("Create an account")
            print("-"*8)
            print("Enter Username:")
            username = input()
            print("Enter password")
            password = input()
            account_name = input()
            save_account(create_account(username, account_name, password))
            print('\n')
            print(f"New user {username} has been created.You can now proceed to login with your credentials.")
            print('\n')
        elif user_choice == "lg":
            print("Enter your Username:")
            login_username = input()
            print("Enter your password:")
            login_password = input()
            if find_user(username) and find_password(login_password):
                print('\n')
                print("Welcome! To continue please choose any of the options below:")
                print("-"*8)
                print("nw - Add New Account, da - Display Accounts, vw -View Account Details, dl - Delete Account Detaiils")
        account_choice = input().lower()
        if account_choice == "nw":
            print("Enter Account Name:")
            account_name = input()
            print("Enter Account Username:")
            account_username = input()
            print("Enter Account Password:")
            account_password = input()
            save_account(create_account(account_name,account_username,account_password))
            print(f"Account Name:{account_name}, Account Username:{account_username}, Account Password:{account_password} has been created")
        elif account_choice == "da":
                    if display_account_credentials():
                        print("List of all your accounts: ")
                        print('\n')
                        for account in display_account_credentials():
                            print(f"Account Name:{account.account_name}")
                    else:
                        print("invalid choice")
        elif account_choice == "vw":
                    print("Enter an Account Name:")
                    account_choiceName = input()
                    if display_account_credentials():
                        account_choiceName = find_account_credentials(account_choiceName)
                        print(f"Account Username:{account_choiceName.account_userName}   Password:{account_choiceName.account_password}")
                    else:
                        print(f"{account_choiceName} does not exist")
        elif account_choice == "dl":
                    print("Enter Account Name:")
                    delete_acc = input()
                    if delete_account(delete_acc):
                        return delete_account(delete_acc)
                    else:
                        print(f"delete_account:{delete_acc} does not exist")
                    # else:
                    # print("Wrong username or password. Please try again.")
                    # print('\n')
                    # else:
            # print("Incorrect Option. Please choose from the ones listed")
            # print('\n')
if __name__ == '__main__':
    main()