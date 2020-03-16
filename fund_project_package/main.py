# importing the files for the signup and signin for now and all the files for the other functions..

import os
import sys

from Fund_raise_ayman_soliman.fund_project_cli.sign_up import sign_up
from Fund_raise_ayman_soliman.fund_project_cli.sign_in import sign_in
from Fund_raise_ayman_soliman.fund_project_cli.create_project import create_project
from Fund_raise_ayman_soliman.fund_project_cli.edit_project import edit_project
from Fund_raise_ayman_soliman.fund_project_cli.remove_project import remove_project
from Fund_raise_ayman_soliman.fund_project_cli.user_projects import user_projects


print("*******Welcome to Ayman Soliman fund raise system using Python********")

while True:
    print("1) Signup")
    print("2) sign in")

    user_selection = input()

    if int(user_selection) == 1:
        first_name = input("Enter your first name:")
        last_name = input("Enter last name:")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        conf_passowrd = input("Confirm your password: ")
        mobile_phone = input("Enter your phone number: ")

        if sign_up(first_name=first_name, last_name=last_name, email=email, password=password,
                   conf_passowrd=conf_passowrd, mobile_phone=mobile_phone):
            print("*******Sign up Success*******")
        else:
            print("Error, whilst signing up. Check your inputs and try again, please!")

    elif int(user_selection) == 2:
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        if sign_in(email=email, password=password):
            while True:
                os.system('clear')
                print("1) Create a project fund raise")
                print("2) List projects")
                print("3) Edit current project")
                print("4) Delete your project")

                logged_in_user_selection = input("Enter your selection: ")
                logged_in_user_email = email

                if int(logged_in_user_selection) == 1:
                    create_project(logged_in_email=email)
                elif int(logged_in_user_selection) == 2:
                    user_projects(logged_in_email=email)
                elif int(logged_in_user_selection) == 3:
                    edit_project(logged_in_email=email)
                elif int(logged_in_user_selection) == 4:
                    remove_project(logged_in_email=email)
            else:
                print("Wrong username or password..")