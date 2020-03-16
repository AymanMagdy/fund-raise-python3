from .create_project import create_project
import json


def edit_project(**kwargs):
    logged_in_user_email = kwargs["logged_in_email"]
    projects_file = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/projects.txt'
    with open(projects_file, 'r') as outfile:
        projects = json.load(outfile)
    for project in projects:
        if project['email'] == logged_in_user_email and (project['id'] != -1):
            print(project)
    project_id_to_edit = input("Enter the id of the project you would want to edit: ")
    for project in projects:
        if project['id'] == int(project_id_to_edit):
            projects.remove(project)
            with open(projects_file, 'w') as outfile:
                json.dump(projects, outfile)
            create_project(logged_in_email=logged_in_user_email)