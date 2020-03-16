import re
import json


def sign_in(**kwargs):
    print("*******Login Success*******")
    email = kwargs["email"]
    password = kwargs["password"]
    login_flag = False
    users = []
    sign_in_file_path = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/signup.txt'
    with open(sign_in_file_path, 'r') as outfile:
        users = json.load(outfile)
        for user in users:
            if user['email'] == email and user['password'] == password:
                login_flag = True
                return login_flag
    return login_flag