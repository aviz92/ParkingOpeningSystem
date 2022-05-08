import os
from datetime import datetime, timezone
import time

from PrivateInfrastructure.Logger_Infrastructure.Projects_Logger import ProjectsLogging
from PrivateInfrastructure.Git_Infrastructure.GitAction_Infrastructure import GitActions


def create_database_backup():
    try:
        current_date_time = datetime.now().strftime("%Y-%m-%d__%H_%M")
        backup_database_name = f'backup_database\\{current_date_time}_datadump.json'
        os.system(
            f'cd {os.path.realpath(os.path.join(os.path.dirname(__file__)))} && '
            f'.\\venv\\Scripts\\activate && '
            f'python manage.py dumpdata --natural-foreign --exclude=auth.permission --exclude=contenttypes --indent=4 > {backup_database_name}'
        )
    except Exception as err:
        print(err)


def main():
    try:
        g = GitActions()
        while True:
            create_database_backup()
            time.sleep(5)
            # git_commit_and_push(string_in_file='_datadump')
            g.git_add_commit_push()
            # time.sleep(2)
            time.sleep(3600 * 2)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    project_name = "Create a database backup, commit and push"
    print('')
    print('####################################')
    print(f'### Start {project_name} Process ###')
    print('####################################')
    print('')
    time.sleep(1)

    log_path = f'C:\\Python Logs\\{project_name}'
    log_file_name = f'{project_name}Logs'
    logger = ProjectsLogging(project_name=project_name, path=log_path, file_name=log_file_name).project_logging(timestamp=True)
    logger.info(f'Start {project_name} Process')
    time.sleep(1)

    main()
