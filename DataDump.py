import os
import datetime
import time

from InfrastructureSVG.Logger_Infrastructure.Projects_Logger import ProjectsLogging


def create_database_backup():
    try:
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d__%H_%M")

        os.system(
            f'cd {os.path.realpath(os.path.join(os.path.dirname(__file__)))} && '
            f'.\\venv\\Scripts\\activate && '
            f'python manage.py dumpdata --natural-foreign --exclude=auth.permission --exclude=contenttypes --indent=4 > db.json'
        )
    except Exception as err:
        print(err)

    # try:
    #     logger.info('Create a new database backup1')
    # except Exception as e:
    #     print('Create a new database backup2')


def main():
    try:
        while True:
            create_database_backup()
            time.sleep(3600 * 2)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    project_name = "DatabaseBackup"
    print('')
    print('####################################')
    print(f'### Start {project_name} Process ###')
    print('####################################')
    print('')
    time.sleep(1)

    log_path = f'C:\\Python Logs\\{project_name}'
    log_file_name = f'{project_name}Logs'
    logger = ProjectsLogging(project_name=project_name, path=log_path, file_name=log_file_name).project_logging()
    logger.info(f'Start {project_name} Process')
    time.sleep(1)

    main()
