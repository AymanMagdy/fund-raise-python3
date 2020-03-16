import re
import json


def valid_password(**kwargs):
    password = kwargs["password"]
    conf_password = kwargs["conf_password"]

    if password == conf_password and (password and conf_password):
        return True
    return False


def validate_email(email):
    matcher = re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)
    if matcher:
        return True
    return False


def valid_phone(mobile_phone):
    matcher = re.search('^(010|011|015|012)([0-9]{8})', mobile_phone)
    if matcher:
        return True
    return False


def valid_to_register(**kwargs):
    email_to_validate = kwargs["email_to_validate"]
    password = kwargs["password"]
    conf_password = kwargs["conf_password"]
    mobile_phone = kwargs["mobile_phone"]

    if valid_password(password=password, conf_password=conf_password) and \
            valid_phone(mobile_phone) and \
            validate_email(email_to_validate):
        return True
    return False


def sign_up(**kwargs):
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    email = kwargs["email"]
    password = kwargs["password"]
    conf_passowrd = kwargs["conf_passowrd"]
    mobile_phone = kwargs["mobile_phone"]
    sign_up_flag = False

    if valid_to_register(password=password, conf_password=conf_passowrd, mobile_phone=mobile_phone, email_to_validate=email):
        sign_up_flag = True
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "conf_password": conf_passowrd,
            "mobile_phone": mobile_phone
        }
        sign_up_file_path = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/signup.txt'
        with open(sign_up_file_path, 'r') as outfile:
            users = json.load(outfile)
            users.append(user_data)

        with open(sign_up_file_path, 'w') as outfile:
            json.dump(users, outfile)
            return sign_up_flag
    else:
        return sign_up_flag