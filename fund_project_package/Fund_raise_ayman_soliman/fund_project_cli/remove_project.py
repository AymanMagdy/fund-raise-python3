import json


def remove_project(**kwargs):
    logged_in_user_email = kwargs["logged_in_email"]
    projects_file = '/usr/src/app/Fund_raise_ayman_soliman/fund_project_cli/projects.txt'
    with open(projects_file, 'r') as outfile:
        projects = json.load(outfile)
    for project in projects:
        if project['email'] == logged_in_user_email and (project['id'] != -1):
            print(project)

    project_id_to_remove = input("Enter the id of the project you would want to remove: ")
    for project in projects:
        if project['id'] == int(project_id_to_remove):
            projects.remove(project)
            with open(projects_file, 'w') as outfile:
                json.dump(projects, outfile)
            print("Done removing the project")