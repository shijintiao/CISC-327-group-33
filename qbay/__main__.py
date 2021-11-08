import os
from qbay.cli import *
import sys
sys.path.append("..")


def main():
    user = None
    while True:
        if user is not None:
            choice = input('\nWelcome. Please Enter 1 to update profile, '
                           '2 to create product, '
                           '3 to update product, '
                           '4 to logout.')
            if choice == '1':
                update_profile(user)
            elif choice == '2':
                create_page(user.email)
            elif choice == '3':
                update_product(user)
            elif choice == '4':
                user = None
                print("You have logged out!")
        else:
            selection = input(
                '\nWelcome.Please Input 1 to login, 2 to register, 3 to quit:')
            selection = selection.strip()
            if selection == '1':
                print('-----------------------------------------\n'
                      'Please enter your email'
                      'address and password here'
                      '\n-----------------------------------------\n')
                user = login_page()
                if user is False:
                    user = None
                    continue
                elif user is None:
                    continue
                else:
                    print(f'welcome {user.username}')
                    continue
            elif selection == '2':
                print('-------------------------------------------------'
                      '------------------------------------\n'
                      'Please read the follow requirements carefully!'
                      '\n-------------------------------------------------'
                      '------------------------------------\n'
                      '1.Your email address must follow the '
                      'RFC5322 standard.\n'
                      '2.Your password length must longer than 6 digits.\n'
                      '3.Your password must include both '
                      'upper letter and lower letters.')
                reg_user = regsiter_page()
                if reg_user is False:
                    continue
                else:
                    print('Congratulation! Your account has been created!')
            elif selection == '3':
                break


main()
