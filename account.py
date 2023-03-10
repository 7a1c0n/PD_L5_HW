"""
Модуль "Банковский счет"
Описание работы модуля:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

account = 0  # Сумма на счету
history = [['  ПОКУПКА', 'СУММА']]  # История покупок


def refill():
    global account
    account += int(input('Сумма пополнения счета:'))


def shopping():
    global account
    pay = int(input('\nСтоимость покупки: '))
    if pay > account:
        print('Недостаточно средств на счете')
    else:
        item = input('Название покупки: ')
        account -= pay
        history.append([item, pay])


def show_history():
    if len(history) > 1:
        for waste_of_money in history:
            print(waste_of_money[0].ljust(40), waste_of_money[1])
    else:
        print('Вы еще не совершали покупок')


def money():
    while True:
        print(f'\nНа счету: {account}\n')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('\nВыберите пункт меню: ')
        if choice == '1':
            refill()
        elif choice == '2':
            shopping()
        elif choice == '3':
            show_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
