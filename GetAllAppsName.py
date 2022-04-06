import os
import re


def check_if_directory_exist(specific_directory_path):
    try:
        return bool(os.path.exists(specific_directory_path))
    except Exception as err:
        print(err)
        return False


def get_all_apps(full_path):
    try:
        t_f = check_if_directory_exist(full_path)
        if t_f:
            with open(full_path, 'r') as file:
                results_from_txt = file.read()
            return re.findall(r"(?<=name = )(.*)", results_from_txt)[0].replace("'", "")
    except Exception as err:
        print(err)


def main(root_path, not_search_folders):
    apps_name = []
    for path_to_file, folders, files in os.walk(root_path):
        for folder in folders:
            if folder.split("\\")[-1] not in not_search_folders:
                if app_name := get_all_apps(f'{root_path}\\{folder}\\apps.py'):
                    apps_name.append(app_name)
                else:
                    continue
    apps_name = ' '.join(apps_name)

    print(f'\npython manage.py makemigrations {apps_name}')
    print('\npython manage.py migrate')


if __name__ == '__main__':
    # pycharm_projects = os.path.realpath(f'{os.path.join(os.path.dirname(__file__)).split("PycharmProjects")[0]}\\PycharmProjects')
    ROOT_PATH = f'{os.path.realpath(os.path.join(os.path.dirname(__file__)))}'
    # print(f'\n\nThe root path is: {ROOT_PATH}')

    NOT_SEARCH_FOLDERS = ['ProjectName', 'venv', '.run', '.git', '.idea']

    main(ROOT_PATH, NOT_SEARCH_FOLDERS)
