import os
from qbay.cli import *
import sys
sys.path.append("..")


def main():
    user = None
    while True:
        if user is not None:
            choice = input('\nYou have %d balance in your account.\n'
                           'Please Select options\n'
                           '1 to update profile\n'
                           '2 to create a product\n'
                           '3 to check your on sale products\n'
                           '4 to browse others\' on sale products.\n'
                           '5 to check past orders\n'
                           '6 to log out:'
                           % (user.balance))
            if choice == '1':
                update_profile(user)
            elif choice == '2':
                create_page(user.email)
            elif choice == '3':
                update_product(user)
            elif choice == '4':
                checkProduct(user)
                pass
            elif choice == '5':
                # Check past orders
                # User can see what he bought and sold
                # Filter by transactions
                pass
            elif choice == '6':
                user = None
                print("You have logged out!")
        else:
            selection = input(
                '\nWelcome.Please Input 1 to login, 2 to register, 3 to quit:')
            selection = selection.strip()
            if not selection.isnumeric():
                print('Please enter a number!')
            else:
                if selection == '1':
                    user = login_page()
                    if user is False:
                        user = None
                        continue
                    elif user is None:
                        continue
                    else:
                        print(f'\nWelcome {user.username}')
                        continue
                elif selection == '2':
                    reg_user = regsiter_page()
                    if reg_user is False:
                        continue
                elif selection == '3':
                    break
                else:
                    print('Please enter a valid number!')


main()
