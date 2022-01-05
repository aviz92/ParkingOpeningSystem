import os
import shutil


def check_if_directory_exist(specific_directory_path):
    try:
        return bool(os.path.exists(specific_directory_path))
    except Exception as err:
        print(err)
        return False


def delete_all_files_in_folder(full_path, not_deleted_files):
    try:
        t_f = check_if_directory_exist(full_path)
        if t_f:
            for path, folders_to_remove, files_to_remove in os.walk(full_path):
                for file in files_to_remove:
                    if file.split("\\")[-1] not in not_deleted_files:
                        print(f'Remove file name: {file}')
                        os.remove(f'{path}\\{file}')
                        # os.remove(file)
                for folder_in_migrations in folders_to_remove:
                    if folder_in_migrations.split("\\")[-1] not in NOT_DELETED_FOLDERS:
                        print(f'Remove folder name: {folder_in_migrations}')
                        shutil.rmtree(f'{path}\\{folder_in_migrations}')
    except Exception as err:
        print(err)


def main(root_path, not_deleted_files, not_deleted_folders):
    for path_to_file, folders, files in os.walk(root_path):
        for folder in folders:
            if folder.split("\\")[-1] not in not_deleted_folders:
                delete_all_files_in_folder(f'{root_path}\\{folder}\\migrations', not_deleted_files)


if __name__ == '__main__':
    ROOT_PATH = f'{os.path.realpath(os.path.join(os.path.dirname(__file__)))}'
    NOT_DELETED_FILES = ['__init__', '__init__.py', '0001_initial.py']
    NOT_DELETED_FOLDERS = ['ProjectName', 'venv', '.run', '.git', '.idea']

    main(ROOT_PATH, NOT_DELETED_FILES, NOT_DELETED_FOLDERS)
