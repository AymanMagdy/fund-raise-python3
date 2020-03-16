import json
import datetime


def validate_date(date):
    date_format = '%Y-%m-%d'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False


def validate_target(total_target):
    if total_target and int(total_target):
        return True
    return False


def create_project(**kwargs):
    email = kwargs["logged_in_email"]
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    total_target = input("Enter the project's total target: ")
    date = input("Enter the date: ")

    projects_file = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/projects.txt'
    if validate_date(date):
        with open(projects_file, 'r') as outfile:
            projects = json.load(outfile)

        project_id = len(projects)+1
        new_project = {
            "id": project_id,
            "email": email,
            "title": title,
            "details": details,
            "total_target": total_target,
            "date": date
        }
        projects.append(new_project)

        with open(projects_file, 'w') as outfile:
            json.dump(projects, outfile)

        print("The project has been created. -> ", title)
    else:
        print("Incorrect data format, should be YYYY-MM-DD. Or Incorrect target data")