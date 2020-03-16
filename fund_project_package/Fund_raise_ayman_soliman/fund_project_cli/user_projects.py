import json


def user_projects(**kwargs):
    logged_in_user_email = kwargs["logged_in_email"]
    projects_file = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/projects.txt'
    with open(projects_file, 'r') as outfile:
        projects = json.load(outfile)
    for project in projects:
        if project['email'] == logged_in_user_email and (project['id'] != -1):
            print(project)
