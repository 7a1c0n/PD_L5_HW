import os
import platform

from quiz import game
from account import money
import fs  # file system

path = os.getcwd()

while True:
    print(f'\nТекущая папка: {path}\n')
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')

    choice = input('\nВыберите пункт меню: ')
    if choice == '1':
        # Создание папки
        fs.create_folder(path)
    elif choice == '2':
        # Удаление папки/файла
        fs.del_object(path)
    elif choice == '3':
        # Копирование папки/файла
        fs.copy_object(path)
    elif choice == '4':
        # Вывод содержимого текущей папки
        fs.list_dir(path)
    elif choice == '5':
        # Просмотр только папок
        fs.list_dir(path, 'folder')
    elif choice == '6':
        # Просмотр только файлов
        fs.list_dir(path, 'file')
    elif choice == '7':
        print('Ваша операционная система:')
        print(platform.platform())
    elif choice == '8':
        print('Автор программы - Феликс Соколов')
    elif choice == '9':
        # Викторина
        game()
    elif choice == '10':
        # Банковский счет
        money()
    elif choice == '11':
        # Выход из программы
        break
    else:
        print('Неверный пункт меню')

    input('\nНажмите Enter, чтобы вернуться в главное меню')