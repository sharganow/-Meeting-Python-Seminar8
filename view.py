main_menu = [
    '---\nСписок возможных действий с телефонным справочником: ',
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход.\n---'
]


def show_menu(lst: list):
    print(f'{lst[0]}')
    for i, d in enumerate(lst[1:]):
        s = ';' if i < len(lst) - 2 else ' '
        print(f'\t{i + 1}. {d}{s}')


def get_user_choice(lst: list) -> str:
    choise = 0
    show_menu(lst)
    while True:
        try:
            choice = int(input('Выберите пункт из приведённого выше списка: '))
            if 0 < choice < len(lst):
                break
            else:
                print('Ваш выбор выходит за пределы возможных вариантов')
                show_menu(lst)
        except:
            print('Значение должно быть целым числом из диапазона возможных вариантов')
            show_menu(lst)
    return lst[choice]
