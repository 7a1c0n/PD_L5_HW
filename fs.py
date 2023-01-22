# file system
import os
import shutil


def list_dir(path, file_or_folder=''):
    lst = os.scandir(path)
    if file_or_folder == 'folder':
        print('\nТолько папки текущей директории:')
        for n in lst:
            if n.is_dir():
                print(n.name)
    elif file_or_folder == 'file':
        print('\nТолько файлы текущей директории:')
        for n in lst:
            if n.is_file():
                print(n.name)
    else:
        print('\nСодержимое текущей папки:')
        for n in lst:
            print(n.name)


def create_folder(path):
    isnamenotok = True
    while isnamenotok:
        name = input('Введите имя новой папки: ')
        new_path = os.path.join(path, name)
        if os.path.exists(new_path):
            print('Объект с таким именем существует в данной папке')
        else:
            os.mkdir(new_path)
            isnamenotok = False


def copy_object(path):
    obj_name = input('Что нужно скопировать? (имя файла/папки в рабочей директории): ')
    obj_path = os.path.join(path, obj_name)
    if os.path.isfile(obj_path):
        where_to_copy = input('Куда нужно скопировать? (Имя папки): ')
        shutil.copy(obj_path, where_to_copy)
    elif os.path.isdir(obj_path):
        where_to_copy = input('Куда нужно скопировать? (Имя папки, включая копируемую): ')
        shutil.copytree(obj_path, where_to_copy)


def del_object(path):
    obj_name = input('Что нужно удалить? (имя файла/папки в рабочей директории): ')
    obj_path = os.path.join(path, obj_name)
    if os.path.isfile(obj_path):
        os.remove(obj_path)
    elif os.path.isdir(obj_path):
        shutil.rmtree(obj_path)
